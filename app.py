from prompt_shield import PromptShieldEngine
from datetime import datetime
import os

engine = PromptShieldEngine()

prompt = "hii"

result = engine.scan(prompt)

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
WHITE = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"

print("\n")
print(f"{CYAN}{'═'*70}{RESET}")
print(f"{BOLD}🛡️  PROMPT SHIELD SECURITY REPORT{RESET}")
print(f"{CYAN}{'═'*70}{RESET}")

print(f"\n📅 Timestamp : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"💻 Host      : {os.uname().nodename}")

print(f"\n📝 Input Prompt:")
print(f'   "{prompt}"')

print(f"\n🔍 Threat Analysis")

if "BLOCK" in str(result.action):
    print(f"   Status      : {RED}{BOLD}🚨 THREAT DETECTED{RESET}")
    print(f"   Decision    : {RED}{BOLD}BLOCKED{RESET}")
else:
    print(f"   Status      : {GREEN}{BOLD}✅ SAFE REQUEST{RESET}")
    print(f"   Decision    : {GREEN}{BOLD}ALLOWED{RESET}")

print(f"   Risk Score  : {YELLOW}{result.overall_risk_score:.2f}/1.00{RESET}")

print(f"\n🧠 Triggered Security Engines")

for detection in result.detections:
    if detection.detected:
        print(
            f"   {RED}▶{RESET} {WHITE}{detection.detector_id}{RESET}"
        )

print(f"\n📊 Security Verdict")

if "BLOCK" in str(result.action):
    print(
        f"   {RED}Prompt injection attempt neutralized before reaching the AI model.{RESET}"
    )
else:
    print(
        f"   {GREEN}No malicious indicators detected.{RESET}"
    )

print(f"\n{CYAN}{'═'*70}{RESET}")
print(f"{MAGENTA}Prompt Shield • Detect. Redact. Protect.{RESET}")
print(f"{CYAN}{'═'*70}{RESET}")