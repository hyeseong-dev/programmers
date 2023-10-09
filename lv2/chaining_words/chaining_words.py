def solution(people_number, words):
    used_words = set()                                          # 사용된 단어를 저장할 집합 초기화
    turn_count = {i: 0 for i in range(1, people_number + 1)}    # 각 플레이어별로 말한 횟수를 저장할 딕셔너리 초기화
    
    for order, word in enumerate(words, 1):                     # 말한 단어들을 순서대로 점검
        
        if order % people_number != 0:                          # 플레이어 번호 결정
            player = order % people_number
        else:
            player = people_number
      
        turn_count[player] += 1                                         # 해당 플레이어의 말한 횟수 1 증가
        

        is_used_word = word in used_words                               # 이미 사용된 단어인지 확인
        is_not_continued = order > 1 and words[order-2][-1] != word[0]  # 현재 단어가 이전 단어의 마지막 글자로 시작하는지 확인
        
        if is_used_word or is_not_continued:                            # 위의 두 조건 중 하나라도 만족하면 탈락
            return [player, turn_count[player]]

        used_words.add(word)

   
    return [0, 0]             

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])