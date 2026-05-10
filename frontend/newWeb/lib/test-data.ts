import { TestQuestion, TestResult, TestType } from './types'

export const testQuestions: Record<TestType, TestQuestion[]> = {
  'phq9': [
    {
      id: 'phq9_1',
      text: 'Little interest or pleasure in doing things',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_2',
      text: 'Feeling down, depressed, or hopeless',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_3',
      text: 'Trouble falling or staying asleep, or sleeping too much',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_4',
      text: 'Feeling tired or having little energy',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_5',
      text: 'Poor appetite or overeating',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_6',
      text: 'Feeling bad about yourself—or that you are a failure or have let your family down',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_7',
      text: 'Trouble concentrating on things, such as reading the newspaper or watching television',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_8',
      text: 'Moving or speaking so slowly that others have noticed, or the opposite—being so fidgety or restless that you have been moving around a lot more than usual',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
    {
      id: 'phq9_9',
      text: 'Thoughts that you would be better off dead or of hurting yourself in some way',
      options: [
        { value: 0, label: 'Not at all' },
        { value: 1, label: 'Several days' },
        { value: 2, label: 'More than half the days' },
        { value: 3, label: 'Nearly every day' },
      ],
    },
  ],
  'bdi2': [
    {
      id: 'bdi2_1',
      text: 'Sadness',
      options: [
        { value: 0, label: 'I do not feel sad' },
        { value: 1, label: 'I feel sad much of the time' },
        { value: 2, label: 'I am sad all the time' },
        { value: 3, label: "I am so sad or unhappy that I can't stand it" },
      ],
    },
    {
      id: 'bdi2_2',
      text: 'Pessimism',
      options: [
        { value: 0, label: 'I am not discouraged about my future' },
        { value: 1, label: 'I feel more discouraged about my future than I used to' },
        { value: 2, label: 'I do not expect things to work out for me' },
        { value: 3, label: 'I feel my future is hopeless and will only get worse' },
      ],
    },
    {
      id: 'bdi2_3',
      text: 'Past Failure',
      options: [
        { value: 0, label: 'I do not feel like a failure' },
        { value: 1, label: 'I have failed more than I should have' },
        { value: 2, label: 'As I look back on my life, I see a lot of failures' },
        { value: 3, label: 'I feel I am a total failure as a person' },
      ],
    },
    {
      id: 'bdi2_4',
      text: 'Loss of Pleasure',
      options: [
        { value: 0, label: 'I get as much pleasure as I ever did from the things I enjoy' },
        { value: 1, label: 'I don\'t enjoy things as much as I used to' },
        { value: 2, label: 'I get very little pleasure from the things that I used to enjoy' },
        { value: 3, label: 'I can\'t get any pleasure from the things I used to enjoy' },
      ],
    },
    {
      id: 'bdi2_5',
      text: 'Guilty Feelings',
      options: [
        { value: 0, label: 'I don\'t feel particularly guilty' },
        { value: 1, label: 'I feel guilty over many things I have done or should have done' },
        { value: 2, label: 'I feel quite guilty most of the time' },
        { value: 3, label: 'I feel guilty all of the time' },
      ],
    },
    {
      id: 'bdi2_6',
      text: 'Punishment Feelings',
      options: [
        { value: 0, label: 'I don\'t feel I am being punished' },
        { value: 1, label: 'I feel I may be punished' },
        { value: 2, label: 'I expect to be punished' },
        { value: 3, label: 'I feel I am being punished' },
      ],
    },
    {
      id: 'bdi2_7',
      text: 'Self-Dislike',
      options: [
        { value: 0, label: 'I feel the same about myself as ever' },
        { value: 1, label: 'I have lost confidence in myself' },
        { value: 2, label: 'I am disappointed in myself' },
        { value: 3, label: 'I dislike myself' },
      ],
    },
    {
      id: 'bdi2_8',
      text: 'Self-Accusation',
      options: [
        { value: 0, label: 'I don\'t criticize or blame myself more than usual' },
        { value: 1, label: 'I am more critical of myself than I used to be' },
        { value: 2, label: 'I criticize myself for all of my faults' },
        { value: 3, label: 'I blame myself for everything bad that happens' },
      ],
    },
    {
      id: 'bdi2_9',
      text: 'Suicidal Thoughts or Wishes',
      options: [
        { value: 0, label: 'I don\'t have any thoughts of killing myself' },
        { value: 1, label: 'I have thoughts of killing myself but would not carry them out' },
        { value: 2, label: 'I would like to kill myself' },
        { value: 3, label: 'I would kill myself if I had the chance' },
      ],
    },
    {
      id: 'bdi2_10',
      text: 'Crying',
      options: [
        { value: 0, label: 'I don\'t cry anymore than I used to' },
        { value: 1, label: 'I cry more now than I used to' },
        { value: 2, label: 'I cry over every little thing' },
        { value: 3, label: 'I feel like crying but can\'t' },
      ],
    },
    {
      id: 'bdi2_11',
      text: 'Agitation',
      options: [
        { value: 0, label: 'I am no more irritated now than I ever am' },
        { value: 1, label: 'I am more irritated now than I usually am' },
        { value: 2, label: 'I am much more irritated now than I usually am' },
        { value: 3, label: 'I am irritated all the time' },
      ],
    },
    {
      id: 'bdi2_12',
      text: 'Loss of Interest',
      options: [
        { value: 0, label: 'I have not lost interest in other people or activities' },
        { value: 1, label: 'I am less interested in other people or things than before' },
        { value: 2, label: 'I have lost most of my interest in other people or things' },
        { value: 3, label: 'It\'s hard to get interested in anything' },
      ],
    },
    {
      id: 'bdi2_13',
      text: 'Indecisiveness',
      options: [
        { value: 0, label: 'I make decisions about as well as I ever could' },
        { value: 1, label: 'I find it more difficult to make decisions than usual' },
        { value: 2, label: 'I have much greater difficulty in making decisions than I used to' },
        { value: 3, label: 'I can\'t make any decisions at all anymore' },
      ],
    },
    {
      id: 'bdi2_14',
      text: 'Worthlessness',
      options: [
        { value: 0, label: 'I do not feel worthless' },
        { value: 1, label: 'I don\'t consider myself as worthwhile and useful as I used to' },
        { value: 2, label: 'I feel more worthless as compared to other people' },
        { value: 3, label: 'I feel utterly worthless' },
      ],
    },
    {
      id: 'bdi2_15',
      text: 'Loss of Energy',
      options: [
        { value: 0, label: 'I have as much energy as ever' },
        { value: 1, label: 'I have less energy than I used to have' },
        { value: 2, label: 'I don\'t have enough energy to do very much' },
        { value: 3, label: 'I don\'t have enough energy to do anything' },
      ],
    },
    {
      id: 'bdi2_16',
      text: 'Changes in Sleep Pattern',
      options: [
        { value: 0, label: 'I haven\'t experienced any change in my sleeping pattern' },
        { value: 1, label: 'I sleep somewhat more than usual' },
        { value: 2, label: 'I sleep a lot more than usual' },
        { value: 3, label: 'I sleep most of the day' },
      ],
    },
    {
      id: 'bdi2_17',
      text: 'Irritability',
      options: [
        { value: 0, label: 'I am no more irritable than usual' },
        { value: 1, label: 'I am more irritable than usual' },
        { value: 2, label: 'I am much more irritable than usual' },
        { value: 3, label: 'I am irritable all the time' },
      ],
    },
    {
      id: 'bdi2_18',
      text: 'Changes in Appetite',
      options: [
        { value: 0, label: 'I haven\'t experienced any change in my appetite' },
        { value: 1, label: 'My appetite is somewhat less than usual' },
        { value: 2, label: 'My appetite is much less than before' },
        { value: 3, label: 'I have no appetite at all anymore' },
      ],
    },
    {
      id: 'bdi2_19',
      text: 'Concentration Difficulty',
      options: [
        { value: 0, label: 'I can concentrate as well as ever' },
        { value: 1, label: 'I can\'t concentrate as well as usual' },
        { value: 2, label: 'It\'s hard to keep my mind on anything for very long' },
        { value: 3, label: 'I find I can\'t concentrate on anything' },
      ],
    },
    {
      id: 'bdi2_20',
      text: 'Tiredness or Fatigue',
      options: [
        { value: 0, label: 'I am no more tired or fatigued than usual' },
        { value: 1, label: 'I get tired or fatigued more easily than usual' },
        { value: 2, label: 'I am too tired or fatigued to do a lot of the things I used to do' },
        { value: 3, label: 'I am too tired or fatigued to do most of the things I used to do' },
      ],
    },
    {
      id: 'bdi2_21',
      text: 'Loss of Interest in Sex',
      options: [
        { value: 0, label: 'I have not noticed any recent change in my interest in sex' },
        { value: 1, label: 'I am less interested in sex than I used to be' },
        { value: 2, label: 'I am much less interested in sex now' },
        { value: 3, label: 'I have lost interest in sex completely' },
      ],
    },
  ],
  'cesd': [
    {
      id: 'cesd_1',
      text: 'I was bothered by things that usually don\'t bother me',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_2',
      text: 'I did not feel like eating; my appetite was poor',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_3',
      text: 'I felt I could not shake off the blues even with help from my family or friends',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_4',
      text: 'I felt I was just as good as other people',
      options: [
        { value: 3, label: 'Rarely or none of the time' },
        { value: 2, label: 'Some or a little of the time' },
        { value: 1, label: 'Occasionally or a moderate amount' },
        { value: 0, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_5',
      text: 'I had trouble keeping my mind on what I was doing',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_6',
      text: 'I felt depressed',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_7',
      text: 'I felt that everything I did was an effort',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_8',
      text: 'I felt hopeful about the future',
      options: [
        { value: 3, label: 'Rarely or none of the time' },
        { value: 2, label: 'Some or a little of the time' },
        { value: 1, label: 'Occasionally or a moderate amount' },
        { value: 0, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_9',
      text: 'I thought my life had been a failure',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_10',
      text: 'I felt fearful',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_11',
      text: 'My sleep was restless',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_12',
      text: 'I was happy',
      options: [
        { value: 3, label: 'Rarely or none of the time' },
        { value: 2, label: 'Some or a little of the time' },
        { value: 1, label: 'Occasionally or a moderate amount' },
        { value: 0, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_13',
      text: 'I talked less than usual',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_14',
      text: 'I felt lonely',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_15',
      text: 'People were unfriendly',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_16',
      text: 'I enjoyed life',
      options: [
        { value: 3, label: 'Rarely or none of the time' },
        { value: 2, label: 'Some or a little of the time' },
        { value: 1, label: 'Occasionally or a moderate amount' },
        { value: 0, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_17',
      text: 'I had crying spells',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_18',
      text: 'I felt sad',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_19',
      text: 'I felt that people disliked me',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
    {
      id: 'cesd_20',
      text: 'I could not get "going"',
      options: [
        { value: 0, label: 'Rarely or none of the time' },
        { value: 1, label: 'Some or a little of the time' },
        { value: 2, label: 'Occasionally or a moderate amount' },
        { value: 3, label: 'Most or all of the time' },
      ],
    },
  ],
  'ai-test': [
    {
      id: 'ai_1',
      text: 'How often do you experience persistent feelings of sadness or emptiness?',
      options: [
        { value: 0, label: 'Never' },
        { value: 1, label: 'Rarely' },
        { value: 2, label: 'Sometimes' },
        { value: 3, label: 'Often' },
      ],
    },
    {
      id: 'ai_2',
      text: 'Do you have difficulty enjoying activities you previously found pleasurable?',
      options: [
        { value: 0, label: 'No difficulty' },
        { value: 1, label: 'Mild difficulty' },
        { value: 2, label: 'Moderate difficulty' },
        { value: 3, label: 'Severe difficulty' },
      ],
    },
    {
      id: 'ai_3',
      text: 'How would you rate your overall energy levels recently?',
      options: [
        { value: 3, label: 'Very low' },
        { value: 2, label: 'Low' },
        { value: 1, label: 'Moderate' },
        { value: 0, label: 'High' },
      ],
    },
    {
      id: 'ai_4',
      text: 'How often do you feel isolated or disconnected from others?',
      options: [
        { value: 0, label: 'Never' },
        { value: 1, label: 'Rarely' },
        { value: 2, label: 'Sometimes' },
        { value: 3, label: 'Often' },
      ],
    },
    {
      id: 'ai_5',
      text: 'Have you experienced changes in your sleep patterns?',
      options: [
        { value: 0, label: 'No changes' },
        { value: 1, label: 'Mild changes' },
        { value: 2, label: 'Moderate changes' },
        { value: 3, label: 'Significant changes' },
      ],
    },
    {
      id: 'ai_6',
      text: 'How often do you experience feelings of worthlessness or guilt?',
      options: [
        { value: 0, label: 'Never' },
        { value: 1, label: 'Rarely' },
        { value: 2, label: 'Sometimes' },
        { value: 3, label: 'Often' },
      ],
    },
    {
      id: 'ai_7',
      text: 'Do you find it difficult to concentrate or make decisions?',
      options: [
        { value: 0, label: 'No difficulty' },
        { value: 1, label: 'Mild difficulty' },
        { value: 2, label: 'Moderate difficulty' },
        { value: 3, label: 'Severe difficulty' },
      ],
    },
    {
      id: 'ai_8',
      text: 'How would you rate your motivation for daily activities?',
      options: [
        { value: 3, label: 'Very low' },
        { value: 2, label: 'Low' },
        { value: 1, label: 'Moderate' },
        { value: 0, label: 'High' },
      ],
    },
  ],
}

export function calculateTestScore(
  testType: TestType,
  responses: Record<string, number>
): TestResult {
  const questions = testQuestions[testType]
  const score = Object.values(responses).reduce((sum, val) => sum + val, 0)
  const maxScore = questions.length * 3

  let category: TestResult['category']
  let severity: TestResult['severity']
  let interpretation: string
  let recommendations: string[] = []

  switch (testType) {
    case 'phq9': {
      // PHQ-9: 0-27 scale
      if (score <= 4) {
        category = 'minimal'
        severity = 'low'
        interpretation =
          'Minimal depressive indicators detected. You are maintaining relatively good emotional well-being.'
        recommendations = [
          'Continue healthy lifestyle habits',
          'Stay connected with supportive relationships',
          'Engage in regular physical activity',
        ]
      } else if (score <= 9) {
        category = 'mild'
        severity = 'moderate'
        interpretation =
          'Mild depressive indicators detected. Consider taking steps to support your emotional health.'
        recommendations = [
          'Practice stress management techniques',
          'Maintain regular social connections',
          'Engage in activities you enjoy',
          'Consider talking to someone you trust',
        ]
      } else if (score <= 14) {
        category = 'moderate'
        severity = 'moderate'
        interpretation =
          'Moderate depressive indicators detected. Professional support may be beneficial.'
        recommendations = [
          'Consider speaking with a mental health professional',
          'Establish a daily routine',
          'Prioritize self-care and rest',
          'Connect with support groups or communities',
        ]
      } else if (score <= 19) {
        category = 'moderately-severe'
        severity = 'elevated'
        interpretation =
          'Moderately severe depressive indicators detected. Professional mental health support is recommended.'
        recommendations = [
          'Schedule an appointment with a mental health professional',
          'Consider evidence-based treatments like therapy or counseling',
          'Build a support network',
          'Reach out to a trusted friend, family member, or counselor',
        ]
      } else {
        category = 'severe'
        severity = 'high'
        interpretation =
          'Severe depressive indicators detected. Professional mental health support is important. Please reach out to a healthcare provider.'
        recommendations = [
          'Contact a mental health professional immediately',
          'Reach out to a crisis helpline if needed',
          'Talk to your doctor about treatment options',
          'Build a strong support network around you',
        ]
      }
      break
    }

    case 'bdi2': {
      // BDI-II: 0-63 scale
      if (score <= 13) {
        category = 'minimal'
        severity = 'low'
        interpretation =
          'Minimal depressive indicators detected. Your emotional state appears stable.'
        recommendations = [
          'Maintain current coping strategies',
          'Continue supportive relationships',
          'Practice regular self-care',
        ]
      } else if (score <= 19) {
        category = 'mild'
        severity = 'moderate'
        interpretation =
          'Mild depressive indicators detected. Consider supporting your emotional well-being.'
        recommendations = [
          'Implement relaxation techniques',
          'Maintain social connections',
          'Engage in physical activity',
          'Consider journaling or reflection',
        ]
      } else if (score <= 28) {
        category = 'moderate'
        severity = 'moderate'
        interpretation =
          'Moderate depressive indicators detected. Professional consultation may be helpful.'
        recommendations = [
          'Consult with a mental health professional',
          'Develop a structured daily routine',
          'Explore therapy options',
          'Connect with support resources',
        ]
      } else if (score <= 42) {
        category = 'moderately-severe'
        severity = 'elevated'
        interpretation =
          'Moderately severe depressive indicators detected. Professional mental health support is recommended.'
        recommendations = [
          'Schedule an appointment with a therapist or counselor',
          'Explore treatment options with a healthcare provider',
          'Build or strengthen your support system',
          'Reach out to trusted individuals for support',
        ]
      } else {
        category = 'severe'
        severity = 'high'
        interpretation =
          'Severe depressive indicators detected. Please reach out to a healthcare professional promptly.'
        recommendations = [
          'Contact a mental health professional immediately',
          'Reach out to a crisis service if experiencing distress',
          'Consult with your doctor about treatment options',
          'Ensure you have emotional support available',
        ]
      }
      break
    }

    case 'cesd': {
      // CES-D: 0-60 scale
      if (score < 16) {
        category = 'minimal'
        severity = 'low'
        interpretation =
          'Minimal depressive indicators detected. You are experiencing good emotional health.'
        recommendations = [
          'Continue your current support systems',
          'Maintain healthy relationships',
          'Engage in regular self-care practices',
        ]
      } else if (score < 27) {
        category = 'mild'
        severity = 'moderate'
        interpretation =
          'Mild to moderate depressive indicators detected. Consider focusing on self-care.'
        recommendations = [
          'Prioritize activities that bring you joy',
          'Strengthen your social connections',
          'Practice stress-reduction techniques',
          'Consider talking with someone you trust',
        ]
      } else if (score < 38) {
        category = 'moderate'
        severity = 'elevated'
        interpretation =
          'Moderate depressive indicators detected. Speaking with a professional may be beneficial.'
        recommendations = [
          'Schedule a consultation with a mental health professional',
          'Develop healthy coping strategies',
          'Establish a regular routine',
          'Join a support group if interested',
        ]
      } else if (score < 50) {
        category = 'moderately-severe'
        severity = 'elevated'
        interpretation =
          'Moderately severe depressive indicators detected. Professional support is recommended.'
        recommendations = [
          'Contact a mental health provider for support',
          'Explore therapy or counseling options',
          'Build a strong support network',
          'Reach out to someone who can help',
        ]
      } else {
        category = 'severe'
        severity = 'high'
        interpretation =
          'Severe depressive indicators detected. Please connect with a healthcare professional.'
        recommendations = [
          'Reach out to a mental health professional immediately',
          'Contact a crisis helpline for support',
          'Speak with your doctor about your symptoms',
          'Ensure you have access to professional help',
        ]
      }
      break
    }

    case 'ai-test': {
      // AI Test: 0-24 scale
      if (score <= 6) {
        category = 'minimal'
        severity = 'low'
        interpretation =
          'Minimal depressive indicators detected. You appear to be managing well emotionally.'
        recommendations = [
          'Continue your current wellness practices',
          'Stay engaged with supportive people',
          'Maintain activities you enjoy',
        ]
      } else if (score <= 12) {
        category = 'mild'
        severity = 'moderate'
        interpretation =
          'Mild depressive indicators detected. It may help to focus on your emotional well-being.'
        recommendations = [
          'Engage in activities that lift your mood',
          'Reach out to friends and family',
          'Practice mindfulness or meditation',
          'Consider speaking with a counselor',
        ]
      } else if (score <= 16) {
        category = 'moderate'
        severity = 'moderate'
        interpretation =
          'Moderate depressive indicators detected. Professional guidance may be valuable.'
        recommendations = [
          'Consult with a mental health professional',
          'Explore therapy or counseling',
          'Create a supportive routine',
          'Connect with others who understand',
        ]
      } else if (score <= 20) {
        category = 'moderately-severe'
        severity = 'elevated'
        interpretation =
          'Moderately severe depressive indicators detected. Professional mental health support is recommended.'
        recommendations = [
          'Schedule an appointment with a therapist',
          'Discuss treatment options with a healthcare provider',
          'Build a strong support system',
          'Reach out for help and guidance',
        ]
      } else {
        category = 'severe'
        severity = 'high'
        interpretation =
          'Severe depressive indicators detected. Please seek professional mental health support.'
        recommendations = [
          'Contact a mental health professional right away',
          'Reach out to a crisis service if needed',
          'Speak with a doctor about your symptoms',
          'Ensure you have professional support available',
        ]
      }
      break
    }

    default:
      interpretation = 'Unable to calculate results'
      category = 'minimal'
      severity = 'low'
  }

  return {
    score,
    interpretation,
    category,
    severity,
    recommendations,
  }
}

export const testInfo = {
  'phq9': {
    name: 'PHQ-9 Test',
    description: 'Patient Health Questionnaire-9',
    duration: '5-10 minutes',
    questions: 9,
  },
  'bdi2': {
    name: 'BDI-II Test',
    description: 'Beck Depression Inventory-II',
    duration: '10-15 minutes',
    questions: 21,
  },
  'cesd': {
    name: 'CES-D Test',
    description: 'Center for Epidemiologic Studies Depression Scale',
    duration: '5-10 minutes',
    questions: 20,
  },
  'ai-test': {
    name: 'AI Depression Assessment',
    description: 'Comprehensive AI-Powered Assessment',
    duration: '5-10 minutes',
    questions: 8,
  },
}
