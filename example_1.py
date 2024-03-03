"""Butun sonlar massivi va butun sonli maqsadni hisobga olgan holda, ikkita raqamning indekslarini maqsadni qo'shadigan qilib qaytaring.

Siz har bir kirishda aynan bitta yechim bo'ladi deb taxmin qilishingiz mumkin va siz bir xil elementni ikki marta ishlata olmaysiz.

Javobni istalgan tartibda qaytarishingiz mumkin."""
# example 1

# bu dasturda hohlagan bir targetni kiritsak listdagi 2 ta elementni yig'indisi targetga teng
# bo'lsa ularni indeksini ekranga choq etadi


def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] + nums[i] == target:
                print(f"[{i}:{j}]")
    return " "


nums = [2, 11, 15, 4, 5, 7, 23, 21, 10]
target = int(input("Enter target number: "))
data = twosum(nums, target)
print("example_2")
nums = [3, 2, 4]
target = 6
data_1 = twosum(nums, target)

