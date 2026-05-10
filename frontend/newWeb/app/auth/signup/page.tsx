'use client'

import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { useRouter } from 'next/navigation'
import { signupSchema, SignupInput } from '@/lib/schemas'
import { useAuth } from '@/lib/auth-context'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { FormField } from '@/components/form-field'
import Link from 'next/link'

export default function SignupPage() {
  const router = useRouter()
  const { signup } = useAuth()
  const [isLoading, setIsLoading] = useState(false)
  const [globalError, setGlobalError] = useState<string | null>(null)

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignupInput>({
    resolver: zodResolver(signupSchema),
  })

  async function onSubmit(data: SignupInput) {
    setIsLoading(true)
    setGlobalError(null)

    try {
      await signup(data.email, data.username, data.password)
      router.push('/dashboard')
    } catch (error: any) {
      const message = error.response?.data?.message || 'Failed to create account. Please try again.'
      setGlobalError(message)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-background to-muted p-4">
      <Card className="w-full max-w-md border-2">
        <CardHeader className="space-y-2">
          <CardTitle className="text-2xl">Create Account</CardTitle>
          <CardDescription>Join our community to assess your emotional well-being</CardDescription>
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

            <FormField label="Username" error={errors.username} required>
              <Input
                {...register('username')}
                type="text"
                placeholder="your_username"
                disabled={isLoading}
              />
            </FormField>

            <FormField label="Password" error={errors.password} required>
              <Input
                {...register('password')}
                type="password"
                placeholder="••••••••"
                disabled={isLoading}
              />
              <p className="text-xs text-muted-foreground mt-2">
                At least 8 characters, one uppercase letter, and one number
              </p>
            </FormField>

            <FormField label="Confirm Password" error={errors.confirmPassword} required>
              <Input
                {...register('confirmPassword')}
                type="password"
                placeholder="••••••••"
                disabled={isLoading}
              />
            </FormField>

            <Button type="submit" className="w-full" disabled={isLoading} size="lg">
              {isLoading ? 'Creating account...' : 'Create account'}
            </Button>

            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-border" />
              </div>
              <div className="relative flex justify-center text-xs uppercase">
                <span className="bg-card px-2 text-muted-foreground">Or sign up with</span>
              </div>
            </div>

            <Button variant="outline" className="w-full" disabled={isLoading}>
              Sign up with Google
            </Button>

            <div className="text-center text-sm">
              <span className="text-muted-foreground">Already have an account? </span>
              <Link href="/auth/login" className="text-primary font-semibold hover:underline">
                Sign in
              </Link>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
