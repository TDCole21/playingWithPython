import RPS 

def test_answerClean():
    incorrect = "wrong"
    correct = ["right","wrong"]
    assert RPS.answerClean(incorrect,correct) == "wrong"

def test_scoring():
    user1 = RPS.Player(1,"Tom","rock")
    user2 = RPS.Player(1,"Tom","rock")
    RPS.scoring(user1,user2)
    assert RPS.PvPScores["player1"] == 1