from yasirapi import YasirPediaApi

req = YasirPediaApi()

print(req.google("Mengapa cewek susah dimengerti."))
"""
{
  "info": "Join telegram channel @YasirPediaChannel for updates.",
  "result": [
    {
      "link": "...",
      "snippet": "...",
      "title": "...",
    }
  ],
  "success": ...,
  "creator": "Yasir Aris M"
}
"""
