def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    skill_trees_list = []
    for skill_tree in skill_trees:
        temp = []
        for s in skill_tree:
            if s in skill_list:
                temp.append(s)
        skill_trees_list.append(temp)
    
    for skill_tree in skill_trees_list:
        length = len(skill_tree)
        if ''.join(skill_tree) == skill[:len(skill_tree)]:
            answer += 1
        
    return answer
  
  # 다른 사람의 풀이
  '''
  for else: for 문에서 break 없이 빠져나온 경우 else에서 처리하게 된다.
  '''
  def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer
