import matplotlib.pyplot as plt

year = [1950,1970,1990,2010, 2030, 2050]
pop = [2.538,2.57,2.62,10.85, 33.55, 20.45]

# Add more data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year,pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0 ,2, 4, 6, 8, 10],
			['0', '2B', '4B', '6B', '8B', '10B'])
plt.show()

