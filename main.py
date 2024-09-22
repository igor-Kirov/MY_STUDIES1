
kol_do_dz = 12
kol_use_time = 1.5
name_kurs = 'Python'
ave_time= kol_use_time/kol_do_dz
print("Курс: "+name_kurs+", всего задач:"+str(kol_do_dz)+", затрвчено часов: "+str(kol_use_time)+", среднее время выполнения "+str(kol_use_time/kol_do_dz) +" часа")
print("Курс: {}. всего задач:{}, затрвчено часов: {}, среднее время выполнения {} часа".format( name_kurs, kol_do_dz, kol_use_time, ave_time))
print(f"Курс: {name_kurs}, всего задач:{kol_do_dz}, затрвчено часов: {kol_use_time}, среднее время выполнения {kol_use_time/kol_do_dz} часа")