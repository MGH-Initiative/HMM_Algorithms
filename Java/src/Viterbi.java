

public class Viterbi {


    public double HMM_Viterbi(char state, int timeCourse){
        if (state == 'B' && timeCourse == 0)
            return 1;
        if (timeCourse == 0)
            return 0;

        return 0.0;
    }
}
