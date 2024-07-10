import GA

if __name__ == '__main__':

    drivers = ["H430","M200","M2631","M452356","K510","N232631","P2652","T520","W420"]
    #drivers = ["W420"]

    path = ''


    final = []
    for driver in drivers:
        results = []
        print ("driver", driver)
        MR = GA.GenerateMatrix(path+str(driver)+"_distance.txt")
        if len(MR) < 100:
            # Aumentar tamaño de la población, tasa de mutación y número de generaciones
            results.append(GA.main(MR, 150, 15, 15, 0.7, 3000, 3000))
            MS = GA.GenerateMatrix(path + str(driver) + "_matrix_with_speed.txt")
            results.append(GA.main(MS, 150, 15, 15, 0.7, 3000, 3000))
            MG = GA.GenerateMatrix(path + str(driver) + "_matrix_with_load_gradient.txt")
            results.append(GA.main(MG, 150, 15, 15, 0.7, 3000, 3000))
            ME = GA.GenerateMatrix(path + str(driver) + "_EU_2020.txt")
        print (results)
        table = []
        for sol in results:
            table.append((GA.CostCalculation(sol[0][1],MR),GA.CostCalculation(sol[0][1],ME),GA.CostCalculation(sol[0][1],MS),GA.CostCalculation(sol[0][1],MG)))
        final.append(table)
