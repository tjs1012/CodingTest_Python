from collections import deque

def solution(cacheSize, cities) :
    answer = 0
    cache = deque()
    city_lower = []
    for city in cities :
        city_lower.append(city.lower())

    for city in city_lower :
        if cacheSize == 0 :
            answer += 5 * len(city_lower)
            break
        elif city not in cache and len(cache) < cacheSize :
            cache.append(city)
            answer += 5
        elif city not in cache and len(cache) == cacheSize :
            cache.popleft()
            cache.append(city)
            answer += 5
        else :
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer