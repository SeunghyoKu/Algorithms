# 베스트앨범 - 해시
# https://programmers.co.kr/learn/courses/30/lessons/42579

# 딕셔너리 안에 딕셔너리를 넣어서 풀어보았습니다

def solution(genres, plays):
    song_dict = {}
    for i in range(len(genres)):
        if genres[i] not in song_dict:
            song_dict[genres[i]] = {
                    'total': plays[i],
                    'play': [(plays[i], i)],
                }
        else:
            song_dict[genres[i]]['total'] += plays[i]
            song_dict[genres[i]]['play'].append((plays[i], i))
            song_dict[genres[i]]['play'].sort(reverse=True)
    
    popular = []
    answer = []
    
    for genre in song_dict.keys():
        if len(popular) < len(song_dict.keys()):
            popular.append((song_dict[genre]['total'], genre))

    popular.sort(reverse=True)
    
    for n, genre in popular:
        song = song_dict[genre]['play']
        answer.append(song[0][1])
        if len(song) >= 2:
            answer.append(song[1][1])
            if song[0][0] == song[1][0] and answer[-1] < answer[-2]:
                answer[-1], answer[-2] = answer[-2], answer[-1]
                
    return answer

