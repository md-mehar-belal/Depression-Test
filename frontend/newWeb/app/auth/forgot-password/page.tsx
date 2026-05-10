'use client'

import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { useRouter } from 'next/navigation'
import { forgotPasswordSchema, ForgotPasswordInput } from '@/lib/schemas'
import { useAuth } from '@/lib/auth-context'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { FormField } from '@/components/form-field'
import Link from 'next/link'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { CheckCircle2, ArrowLeft } from 'lucide-react'

export default function ForgotPasswordPage() {
  const router = useRouter()
  const { forgotPassword } = useAuth()
  const [isLoading, setIsLoading] = useState(false)
  const [globalError, setGlobalError] = useState<string | null>(null)
  const [submitted, setSubmitted] = useState(false)

  const {
    register,
    handleSubmit,
    formState: { errors },
    getValues,
  } = useForm<ForgotPasswordInput>({
    resolver: zodResolver(forgotPasswordSchema),
  })

  async function onSubmit(data: ForgotPasswordInput) {
    setIsLoading(true)
    setGlobalError(null)

    try {
      await forgotPassword(data.email)
      setSubmitted(true)
    } catch (error: any) {
      const message = error.response?.data?.message || 'Failed to send reset email. Please try again.'
      setGlobalError(message)
    } finally {
      setIsLoading(false)
    }
  }

  if (submitted) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-background to-muted p-4">
        <Card className="w-full max-w-md border-2">
          <CardHeader className="space-y-2 text-center">
            <div className="flex justify-center mb-4">
              <div className="h-12 w-12 rounded-full bg-secondary/10 flex items-center justify-center">
                <CheckCircle2 className="h-6 w-6 text-secondary" />
              </div>
            </div>
            <CardTitle className="text-2xl">Check Your Email</CardTitle>
            <CardDescription>
              We've sent a password reset link to {getValues('email')}
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            <Alert className="bg-secondary/5 border-secondary/20">
              <AlertDescription>
                Follow the link in the email to reset your password. The link will expire in 24 hours.
              </AlertDescription>
            </Alert>

            <Button
              onClick={() => router.push('/auth/login')}
              className="w-full"
              size="lg"
            >
              Back to Sign In
            </Button>
          </CardContent>
        </Card>
      </div>
    )
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-background to-muted p-4">
      <Card className="w-full max-w-md border-2">
        <CardHeader className="space-y-2">
          <CardTitle className="text-2xl">Reset Your Password</CardTitle>
          <CardDescription>
            Enter your email address and we'll send you a link to reset your password
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
            {globalError && (
              <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-3">
                <p className="text-sm text-destructive">{globalError}</p>
              </div>
            )}

            <FormField label="Email Address" error={errors.email} required>
              <Input
                {...register('email')}
                type="email"
                placeholder="name@example.com"
                disabled={isLoading}
              />
            </FormField>

            <Button type="submit" className="w-full" disabled={isLoading} size="lg">
              {isLoading ? 'Sending...' : 'Send Reset Link'}
            </Button>

            <Link
              href="/auth/login"
              className="flex items-center justify-center gap-2 text-sm text-primary hover:underline"
            >
              <ArrowLeft className="h-4 w-4" />
              Back to Sign In
            </Link>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
