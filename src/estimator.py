def challenge1 (data):
      
  reportedCases = data.get("reportedCases")
  Impact_currentlyInfected = reportedCases * 10
  Severe_currentlyInfected = reportedCases  * 50


  periodType = data.get("periodType")
  timeToElapse = data.get("timeToElapse")

  if periodType == "days":
        pass
  elif periodType == "weeks":
        timeToElapse = timeToElapse * 7
  elif periodType == "months":
        timeToElapse = timeToElapse * 30


  factor = timeToElapse // 3
  Impact_infectionsByRequestedTime = Impact_currentlyInfected * (2 ** factor)

  Severe_infectionsByRequestedTime = Severe_currentlyInfected * (2 ** factor)

  
  impact = {"currentlyInfected":Impact_currentlyInfected, 
  "infectionsByRequestedTime":Impact_infectionsByRequestedTime}

  severeImpact = {"currentlyInfected": Severe_currentlyInfected,
  "infectionsByRequestedTime":Severe_infectionsByRequestedTime}


  result = {"data": data, "impact":impact, "severeImpact":severeImpact}
  return result


def estimator(data):

  resultChal1 = challenge1(data)
  

  return resultChal1


print("name")

if __name__ == "__main__":
  print("o")
  data = { "region": {
  "name": "Africa",
  "avgAge": 19.7,
  "avgDailyIncomeInUSD": 5,
  "avgDailyIncomePopulation": 0.71
  },
  "periodType": "days",
  "timeToElapse": 3,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
  }

  result = estimator(data)

  print(result)



