def rank_risk(data: dict):
    """
    Simple heuristic risk engine:
    - If org is empty -> medium Risk
    - If country is different from  yours -> Medium Risk
    - If city or region missing -> High Risk
    - Else low 
    """

    score = 0

    if not data.get("org"):
        score += 1

    if data.get("country") not in ["India", "IND", "IN"]:
        score += 1
    
    if not data.get("city") or not data.get("region"):
        score += 2

    if score == 0:
        return "Low Risk"
    elif score == 1:
        return "Medium Risk"
    else:
        return "High Risk"
    
