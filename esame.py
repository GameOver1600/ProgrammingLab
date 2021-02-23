def hourly_trend_changes(a):
    ora = 0
    prec=[a[0][0],a[0][1],'=']
    cha = []
    cha.append(0)
    for i in range(1, len(a)):
        if prec[0] // 3600 != a[i][0] // 3600:
            ora += 1
            cha.append(0)
        if prec[2] == '=':
            if a[i][1] != prec[1] and i != 1:
                cha[ora] += 1
        elif prec[2] == '>':
            if a[i][1] <= prec[1] and i != 1:
                cha[ora] += 1
        else:
            if a[i][1] >= prec[1] and i != 1:
                cha[ora] += 1
        if a[i][1] == prec[1]:
            prec = [a[i][0], a[i][1], '=']
        elif a[i][1] > prec[1]:
            prec = [a[i][0], a[i][1], '>']
        else:
            prec = [a[i][0], a[i][1], '<']
    return cha

class CSVTimeSeriesFile():

    to_clean = ["",""]
    lista = []

    def __init__ (self, name):
        self.name = name
    
    def get_data(self):
        try:
            with open(self.name) as file:
                read_data = file.read()
        except:
            raise ExamException('Impossibile aprire {}'.format(self.name))
            return None
        file = open(self.name, "r")
        i = 0
        for line in file:
            CSVTimeSeriesFile.to_clean = (line.replace("\n", "").split(","))
            if self.checks(i):
                CSVTimeSeriesFile.lista.append(CSVTimeSeriesFile.to_clean)
                i+=1
        return CSVTimeSeriesFile.lista
            
    def checks(self, line):
        for p in range(2):
            if CSVTimeSeriesFile.to_clean[p] != None and CSVTimeSeriesFile.to_clean[p] != '' :
                for i in range(len(CSVTimeSeriesFile.to_clean[p])):
                    if (ord(CSVTimeSeriesFile.to_clean[p][i]) < 48 or ord(CSVTimeSeriesFile.to_clean[p][i]) > 57) and (ord(CSVTimeSeriesFile.to_clean[p][i]) != 46):
                        return False
                if line==0:
                    if p == 0:
                        CSVTimeSeriesFile.to_clean[p] = round(float(CSVTimeSeriesFile.to_clean[p]))
                    else:
                        CSVTimeSeriesFile.to_clean[p] = float(CSVTimeSeriesFile.to_clean[p])
                elif CSVTimeSeriesFile.lista[line-1][0] < round(float(CSVTimeSeriesFile.to_clean[0])):
                    if p == 0:
                        CSVTimeSeriesFile.to_clean[p] = round(float(CSVTimeSeriesFile.to_clean[p]))
                    else:
                        CSVTimeSeriesFile.to_clean[p] = float(CSVTimeSeriesFile.to_clean[p])
                else:
                    raise ExamException('Epoch non crescenti o doppie')
                    return False
            else:
                return False
        return True

class ExamException(Exception):
        pass

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print (time_series)
print (hourly_trend_changes(time_series))