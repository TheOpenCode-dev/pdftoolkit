# OpenClaw Security Checklist

## Common Security Mistakes (from docs & community)

1. **Exposing Gateway to public internet** - Not binding to loopback, no auth token
2. **Open group/DM policies + elevated tools** - Anyone in a group can trigger high-impact actions via prompt injection
3. **Default/weak auth tokens** - Short or predictable tokens
4. **No plugin allowlists** - Untrusted extensions auto-load
5. **Running as root** - Full system compromise if exploited
6. **No sandboxing** - exec/browser tools run unsandboxed on host
7. **Sharing session keys** - Thinking sessionKey is auth (it's just routing)
8. **Mixing personal/company identities** on same runtime
9. **Logging sensitive data** - API keys, credentials in plain text logs
10. **Leaving SSH enabled with password auth** - Easy brute force target

---

# SECURITY ASSESSMENT: Kunal's Laptop

## 1. How Exposed Are We?

| Surface | Status | Notes |
|---------|--------|-------|
| Gateway ports | ✅ SECURE | Only bound to 127.0.0.1 (loopback) - not publicly accessible |
| Telegram DM | ✅ SECURE | `dmPolicy: "pairing"` - requires pairing |
| Telegram Groups | 🔴 CRITICAL | `groupPolicy: "open"` - anyone in group can message bot |
| Web access | ⚪ N/A | `web.search.enabled: false` |
| Tailscale | ⚪ OFF | Not exposed via Tailscale |

**Overall Exposure: MEDIUM** - Gateway is secure but open groups + elevated tools = high risk

## 2. What's Secured Correctly?

- ✅ Gateway bound to loopback (127.0.0.1), not LAN or public
- ✅ Gateway auth enabled with random token
- ✅ DM policy set to "pairing" (requires explicit approval)
- ✅ SSH is INACTIVE/not running
- ✅ Credentials directory has correct permissions (700, owner-only)
- ✅ No unnecessary database services (no postgres, mysql, mongodb, redis)
- ✅ No Docker exposing ports
- ✅ tools.profile = "messaging" (restricted by default)

## 3. Critical Issues (FIX IMMEDIATELY)

### CRITICAL #1: Open Group Policy + Elevated Tools
```
Issue: channels.telegram.groupPolicy = "open"
Risk: Anyone in a Telegram group with the bot can trigger elevated tools via prompt injection
Impact: With tools.elevated enabled, a compromised group = full system compromise
```

**FIX:**
```bash
openclaw config set channels.telegram.groupPolicy "allowlist"
# Then add allowed group IDs to channels.telegram.groupAllowlist
```

### CRITICAL #2: Dangerous Web Search Plugin
```
Issue: openclaw-web-search plugin contains:
  - Shell command execution (child_process)
  - Environment variable harvesting pattern

Risk: If plugin is malicious/exploited, can exfiltrate credentials
```

**FIX:**
```bash
# Remove the plugin
rm -rf ~/.openclaw/extensions/openclaw-web-search
# Or disable in config
openclaw config set plugins.entries.openclaw-web-search.enabled false
```

### CRITICAL #3: No Plugin Allowlist
```
Issue: plugins.allow is not set - any discovered plugin can load
```

**FIX:**
```bash
openclaw config set plugins.allow ["telegram"]  # or your trusted plugins
```

## 4. High Priority Issues

### HIGH #1: Elevated Tools Enabled
```
Issue: tools.elevated enabled with open group policy
Risk: Prompt injection in open group can execute privileged commands
```

**FIX:**
```bash
# Option A: Disable elevated tools (safer)
openclaw config set tools.elevated.enabled false

# Option B: If you need them, ensure groupPolicy is allowlist FIRST
```

### HIGH #2: Trusted Proxies Not Configured
```
Issue: Using reverse proxy but gateway.trustedProxies is empty
Risk: Local-client checks can be spoofed
```

**FIX:** (only if using reverse proxy)
```bash
openclaw config set gateway.trustedProxies ["YOUR_PROXY_IP"]
```

## 5. Medium Priority (Fix Later)

| Issue | Risk | Recommendation |
|-------|------|----------------|
| `gateway.nodes.denyCommands` has invalid entries | Ineffective restrictions | Use exact command names from docs |
| No explicit sandbox config | exec/browser run unsandboxed | Add `tools.exec.sandbox: true` when comfortable |
| Gateway token in config file | Token exposed if file leaked | Consider env-based auth |

## 6. Good Enough For Now

- ✅ Loopback-only Gateway binding
- ✅ Token-based authentication
- ✅ DM pairing policy
- ✅ No SSH exposure
- ✅ No unnecessary services
- ✅ Credentials properly protected

---

# HARDENING GUIDE (Step-by-Step)

## Priority 1: Fix Critical Issues NOW

```bash
# 1. Change group policy from "open" to "allowlist"
openclaw config set channels.telegram.groupPolicy "allowlist"

# 2. Disable or remove dangerous web search plugin
openclaw config set plugins.entries.openclaw-web-search.enabled false

# 3. Set plugin allowlist
openclaw config set plugins.allow ["telegram"]

# 4. Restart gateway to apply
openclaw gateway restart
```

## Priority 2: High Priority Fixes

```bash
# Consider disabling elevated tools if not needed
openclaw config set tools.elevated.enabled false

# Or tighten them significantly if needed
```

## Priority 3: Medium Term Improvements

```bash
# Enable sandbox for exec (when ready)
openclaw config set tools.exec.sandbox true

# Add workspace-only filesystem restriction
openclaw config set tools.fs.workspaceOnly true
```

---

# SUMMARY

| Severity | Count | Status |
|----------|-------|--------|
| CRITICAL | 2 | 🔴 Needs immediate fix |
| HIGH | 2 | ⚠️ Fix today |
| MEDIUM | 2 | 📅 Fix this week |
| SECURE | 7 | ✅ Already good |

**Bottom Line:** The open Telegram group policy with elevated tools is your biggest risk. Fix that first. The web search plugin is suspicious - remove or disable it.
