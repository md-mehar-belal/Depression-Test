export type TestType = 'phq9' | 'bdi2' | 'cesd' | 'ai-test'

export interface TestQuestion {
  id: string
  text: string
  options: {
    value: number
    label: string
  }[]
}

export interface TestResult {
  score: number
  interpretation: string
  category: 'minimal' | 'mild' | 'moderate' | 'moderately-severe' | 'severe'
  recommendations: string[]
  severity: 'low' | 'moderate' | 'elevated' | 'high'
}

export interface TestSubmission {
  testType: TestType
  responses: Record<string, number>
  score: number
  interpretation: string
  submittedAt: string
}

export interface UserProfile {
  id: string
  email: string
  username: string
  createdAt: string
}

export interface AuthContextType {
  user: UserProfile | null
  isAuthenticated: boolean
  loading: boolean
  login: (email: string, password: string) => Promise<void>
  signup: (email: string, username: string, password: string) => Promise<void>
  logout: () => Promise<void>
  googleLogin: (token: string) => Promise<void>
  forgotPassword: (email: string) => Promise<void>
  resetPassword: (email: string, code: string, password: string) => Promise<void>
}
