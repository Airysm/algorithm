from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre = defaultdict(int)
    song = defaultdict()
    
    for i in range(len(genres)):
        song[i] = [plays[i], genres[i]]
        genre[genres[i]] += plays[i]
    
    genre = sorted(genre.items(), key=lambda item:item[1], reverse=True)
    song  = sorted(song.items(), key=lambda item:item[1][0], reverse=True)
    
    for g in genre:
        count = 0
        for s in song:
            if count >= 2:
                break
            if g[0] == s[1][1]:
                answer.append(s[0])
                count += 1
                
    return answer