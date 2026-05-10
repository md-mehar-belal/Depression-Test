'use client'

import React, { useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth-context'
import { useForm, Controller } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { testResponseSchema, TestResponseInput } from '@/lib/schemas'
import {
  testQuestions,
  calculateTestScore,
  testInfo,
  TestType,
} from '@/lib/test-data'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Progress } from '@/components/ui/progress'
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group'
import { FormField } from '@/components/form-field'
import { Skeleton } from '@/components/ui/skeleton'
import { ArrowLeft, CheckCircle2 } from 'lucide-react'
import Link from 'next/link'

export default function TestPage() {
  const params = useParams()
  const router = useRouter()
  const { user, loading } = useAuth()
  const testType = params.testType as TestType
  const [step, setStep] = useState<'start' | 'questions' | 'results'>('start')
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [testResult, setTestResult] = useState<ReturnType<typeof calculateTestScore> | null>(null)

  const {
    control,
    handleSubmit,
    formState: { errors },
    watch,
  } = useForm<TestResponseInput>({
    resolver: zodResolver(testResponseSchema),
    mode: 'onChange',
  })

  React.useEffect(() => {
    if (!loading && !user) {
      router.push('/auth/login?from=' + router.pathname)
    }
  }, [user, loading, router])

  if (loading) {
    return (
      <div className="min-h-screen bg-background">
        <div className="max-w-2xl mx-auto px-4 py-8">
          <Skeleton className="h-8 w-48 mb-8" />
          <Skeleton className="h-96" />
        </div>
      </div>
    )
  }

  if (!user) {
    return null
  }

  if (!testQuestions[testType]) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <Card>
          <CardContent className="pt-6">
            <p className="text-destructive mb-4">Test not found</p>
            <Link href="/dashboard">
              <Button variant="outline">Back to Dashboard</Button>
            </Link>
          </CardContent>
        </Card>
      </div>
    )
  }

  const questions = testQuestions[testType]
  const info = testInfo[testType]
  const currentAnswers = watch()
  const answeredCount = Object.keys(currentAnswers).length
  const progress = (answeredCount / questions.length) * 100

  const onSubmit = async (data: TestResponseInput) => {
    setIsSubmitting(true)
    try {
      // Simulate API call
      await new Promise((resolve) => setTimeout(resolve, 500))

      const result = calculateTestScore(testType, data)
      setTestResult(result)
      setStep('results')
    } catch (error) {
      console.error('Error submitting test:', error)
    } finally {
      setIsSubmitting(false)
    }
  }

  // Start Screen
  if (step === 'start') {
    return (
      <div className="min-h-screen bg-gradient-to-b from-background to-muted">
        <div className="max-w-2xl mx-auto px-4 py-8">
          <Link href="/dashboard" className="flex items-center gap-2 text-primary hover:underline mb-8">
            <ArrowLeft className="h-4 w-4" />
            Back to Dashboard
          </Link>

          <Card>
            <CardHeader>
              <CardTitle className="text-3xl">{info.name}</CardTitle>
              <CardDescription className="text-base mt-2">{info.description}</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="bg-secondary/5 border border-secondary/20 rounded-lg p-6 space-y-4">
                <h3 className="font-semibold text-foreground">Test Information</h3>
                <div className="grid grid-cols-3 gap-4 text-sm">
                  <div>
                    <p className="text-muted-foreground">Questions</p>
                    <p className="font-semibold text-foreground">{info.questions}</p>
                  </div>
                  <div>
                    <p className="text-muted-foreground">Duration</p>
                    <p className="font-semibold text-foreground">{info.duration}</p>
                  </div>
                  <div>
                    <p className="text-muted-foreground">Type</p>
                    <p className="font-semibold text-foreground">Anonymous</p>
                  </div>
                </div>
              </div>

              <div className="bg-primary/5 border border-primary/20 rounded-lg p-6">
                <h3 className="font-semibold text-foreground mb-2">Important</h3>
                <p className="text-sm text-muted-foreground">
                  This assessment is designed to help you understand your emotional well-being. Your responses are confidential and will help provide personalized guidance and recommendations.
                </p>
              </div>

              <Button
                size="lg"
                className="w-full"
                onClick={() => setStep('questions')}
              >
                Start Assessment
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    )
  }

  // Results Screen
  if (step === 'results' && testResult) {
    return (
      <div className="min-h-screen bg-gradient-to-b from-background to-muted">
        <div className="max-w-2xl mx-auto px-4 py-8">
          <Link href="/dashboard" className="flex items-center gap-2 text-primary hover:underline mb-8">
            <ArrowLeft className="h-4 w-4" />
            Back to Dashboard
          </Link>

          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle className="text-3xl">{info.name} Results</CardTitle>
                  <CardDescription>Your assessment has been completed</CardDescription>
                </div>
                <div className="h-12 w-12 rounded-full bg-secondary/10 flex items-center justify-center">
                  <CheckCircle2 className="h-6 w-6 text-secondary" />
                </div>
              </div>
            </CardHeader>
            <CardContent className="space-y-6">
              <div>
                <p className="text-sm text-muted-foreground mb-2">Your Score</p>
                <p className="text-5xl font-bold text-primary">{testResult.score}</p>
              </div>

              <div className="bg-secondary/5 border border-secondary/20 rounded-lg p-6">
                <h3 className="font-semibold text-foreground mb-2">Interpretation</h3>
                <p className="text-muted-foreground">{testResult.interpretation}</p>
              </div>

              <div>
                <h3 className="font-semibold text-foreground mb-3">Recommended Next Steps</h3>
                <ul className="space-y-2">
                  {testResult.recommendations.map((rec, idx) => (
                    <li key={idx} className="flex gap-3 items-start">
                      <CheckCircle2 className="h-5 w-5 text-secondary flex-shrink-0 mt-0.5" />
                      <span className="text-muted-foreground">{rec}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="border-t border-border pt-6 space-y-3">
                <Link href="/dashboard" className="block">
                  <Button className="w-full">Back to Dashboard</Button>
                </Link>
                <Button
                  variant="outline"
                  className="w-full"
                  onClick={() => {
                    setStep('start')
                    setTestResult(null)
                  }}
                >
                  Take Another Test
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    )
  }

  // Questions Screen
  return (
    <div className="min-h-screen bg-gradient-to-b from-background to-muted">
      <div className="max-w-2xl mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <Link href="/dashboard" className="flex items-center gap-2 text-primary hover:underline mb-4">
            <ArrowLeft className="h-4 w-4" />
            Back to Dashboard
          </Link>
          <div className="flex items-center justify-between mb-4">
            <div>
              <h1 className="text-2xl font-bold text-foreground">{info.name}</h1>
              <p className="text-muted-foreground">
                Question {answeredCount + 1} of {questions.length}
              </p>
            </div>
            <div className="text-right">
              <p className="text-2xl font-bold text-primary">{Math.round(progress)}%</p>
            </div>
          </div>
          <Progress value={progress} className="h-2" />
        </div>

        {/* Questions */}
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          {questions.map((question, idx) => (
            <Card key={question.id}>
              <CardContent className="pt-6">
                <h3 className="text-lg font-semibold text-foreground mb-4">{question.text}</h3>
                <Controller
                  name={question.id}
                  control={control}
                  rules={{ required: 'Please select an answer' }}
                  render={({ field }) => (
                    <RadioGroup
                      value={field.value?.toString() || ''}
                      onValueChange={(value) => field.onChange(parseInt(value))}
                    >
                      <div className="space-y-3">
                        {question.options.map((option) => (
                          <label
                            key={option.value}
                            className="flex items-center space-x-3 cursor-pointer p-3 rounded-lg hover:bg-muted transition-colors"
                          >
                            <RadioGroupItem
                              value={option.value.toString()}
                              id={`${question.id}-${option.value}`}
                              className="mt-1"
                            />
                            <span className="flex-1 text-foreground">{option.label}</span>
                          </label>
                        ))}
                      </div>
                    </RadioGroup>
                  )}
                />
                {errors[question.id as keyof typeof errors] && (
                  <p className="text-sm text-destructive mt-2">
                    {errors[question.id as keyof typeof errors]?.message}
                  </p>
                )}
              </CardContent>
            </Card>
          ))}

          {/* Submit Button */}
          <div className="flex gap-4">
            <Button
              type="button"
              variant="outline"
              className="flex-1"
              onClick={() => setStep('start')}
            >
              Cancel
            </Button>
            <Button
              type="submit"
              className="flex-1"
              disabled={isSubmitting || answeredCount < questions.length}
              size="lg"
            >
              {isSubmitting ? 'Submitting...' : 'Submit Assessment'}
            </Button>
          </div>
        </form>
      </div>
    </div>
  )
}
