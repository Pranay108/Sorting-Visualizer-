import streamlit as st
import random
import time

st.set_page_config(page_title="Sorting Visualizer", layout="wide")

st.title("Sorting Visualizer")
st.write("Visualize how different sorting algorithms work")

st.sidebar.header("Settings")
size = st.sidebar.slider("Array Size", 5, 100, 30)
speed = st.sidebar.slider("Speed", 0.001, 0.3, 0.05)
algo = st.sidebar.selectbox("Algorithm", 
                            ["Bubble Sort",
                             "Selection Sort",
                             "Insertion Sort",
                             "Merge Sort",
                             "Quick Sort"])
start = st.sidebar.button("Start")

array = [random.randint(10, 200) for _ in range(size)]
placeholder = st.empty()

def bubble_sort(arr):
    a = arr.copy()
    steps = []
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            steps.append(a.copy())
    return steps

def selection_sort(arr):
    a = arr.copy()
    steps = []
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        steps.append(a.copy())
    return steps

def insertion_sort(arr):
    a = arr.copy()
    steps = []
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            steps.append(a.copy())
        a[j + 1] = key
        steps.append(a.copy())
    return steps

def merge_sort(arr):
    steps = []
    a = arr.copy()
    
    def merge_sort_recursive(l, r):
        if r - l <= 1:
            return
        m = (l + r) // 2
        merge_sort_recursive(l, m)
        merge_sort_recursive(m, r)
        merge(l, m, r)
    
    def merge(l, m, r):
        left = a[l:m]
        right = a[m:r]
        i = j = 0
        for k in range(l, r):
            if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            steps.append(a.copy())
    
    merge_sort_recursive(0, len(a))
    return steps

def quick_sort(arr):
    steps = []
    list1 = arr.copy()
    
    def pivot_place(list1, first, last):
        pivot = list1[first]
        left = first + 1
        right = last

        while True:
            while left <= right and list1[left] <= pivot:
                left = left + 1

            while left <= right and list1[right] >= pivot:
                right = right - 1

            if right < left:
                break
            else:
                list1[left], list1[right] = list1[right], list1[left]
                steps.append(list1.copy())

        list1[first], list1[right] = list1[right], list1[first]
        steps.append(list1.copy())
        return right

    def quicksort(list1, first, last):
        if first < last:
            p = pivot_place(list1, first, last)
            quicksort(list1, first, p - 1)
            quicksort(list1, p + 1, last)
    
    quicksort(list1, 0, len(list1) - 1)
    return steps

def animate(steps, speed):
    for step in steps:
        placeholder.bar_chart(step)
        time.sleep(speed)

if not start:
    placeholder.bar_chart(array)

if start:
    if algo == "Bubble Sort":
        steps = bubble_sort(array)
    elif algo == "Selection Sort":
        steps = selection_sort(array)
    elif algo == "Insertion Sort":
        steps = insertion_sort(array)
    elif algo == "Merge Sort":
        steps = merge_sort(array)
    elif algo == "Quick Sort":
        steps = quick_sort(array)
    
    animate(steps, speed)
    st.write("Done!")
