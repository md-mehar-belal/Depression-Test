'use client'

import React, { useState } from 'react'
import { useAuth } from '@/lib/auth-context'
import { useRouter } from 'next/navigation'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { updateProfileSchema, UpdateProfileInput } from '@/lib/schemas'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { FormField } from '@/components/form-field'
import { Skeleton } from '@/components/ui/skeleton'
import { ArrowLeft, User, Mail, Calendar, LogOut } from 'lucide-react'
import Link from 'next/link'

export default function ProfilePage() {
  const { user, loading, logout } = useAuth()
  const router = useRouter()
  const [isSaving, setIsSaving] = useState(false)

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm<UpdateProfileInput>({
    resolver: zodResolver(updateProfileSchema),
    values: {
      username: user?.username || '',
      email: user?.email || '',
    },
  })

  React.useEffect(() => {
    if (!loading && !user) {
      router.push('/auth/login?from=/profile')
    }
  }, [user, loading, router])

  const onSubmit = async (data: UpdateProfileInput) => {
    setIsSaving(true)
    try {
      // Simulate API call to update profile
      await new Promise((resolve) => setTimeout(resolve, 1000))
      reset()
    } catch (error) {
      console.error('Error updating profile:', error)
    } finally {
      setIsSaving(false)
    }
  }

  const handleLogout = async () => {
    await logout()
    router.push('/')
  }

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

  return (
    <div className="min-h-screen bg-gradient-to-b from-background to-muted">
      <div className="max-w-2xl mx-auto px-4 py-8">
        <Link href="/dashboard" className="flex items-center gap-2 text-primary hover:underline mb-8">
          <ArrowLeft className="h-4 w-4" />
          Back to Dashboard
        </Link>

        {/* Profile Info Card */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle className="text-3xl">My Profile</CardTitle>
            <CardDescription>Manage your account information</CardDescription>
          </CardHeader>
          <CardContent className="space-y-6">
            {/* Display Current Info */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="flex items-center gap-4 p-4 bg-muted rounded-lg">
                <div className="h-10 w-10 rounded-full bg-primary/10 flex items-center justify-center">
                  <User className="h-5 w-5 text-primary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Username</p>
                  <p className="font-semibold text-foreground">{user.username}</p>
                </div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-muted rounded-lg">
                <div className="h-10 w-10 rounded-full bg-secondary/10 flex items-center justify-center">
                  <Mail className="h-5 w-5 text-secondary" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Email</p>
                  <p className="font-semibold text-foreground">{user.email}</p>
                </div>
              </div>

              <div className="flex items-center gap-4 p-4 bg-muted rounded-lg">
                <div className="h-10 w-10 rounded-full bg-accent/10 flex items-center justify-center">
                  <Calendar className="h-5 w-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted-foreground">Member Since</p>
                  <p className="font-semibold text-foreground">
                    {new Date(user.createdAt).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                    })}
                  </p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Edit Profile Card */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Update Profile</CardTitle>
            <CardDescription>Modify your account settings</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
              <FormField label="Username" error={errors.username}>
                <Input
                  {...register('username')}
                  placeholder="your_username"
                  disabled={isSaving}
                />
              </FormField>

              <FormField label="Email Address" error={errors.email}>
                <Input
                  {...register('email')}
                  type="email"
                  placeholder="name@example.com"
                  disabled={isSaving}
                />
              </FormField>

              <Button type="submit" disabled={isSaving} size="lg" className="w-full">
                {isSaving ? 'Saving...' : 'Save Changes'}
              </Button>
            </form>
          </CardContent>
        </Card>

        {/* Security Card */}
        <Card className="mb-6">
          <CardHeader>
            <CardTitle>Security</CardTitle>
            <CardDescription>Manage your account security</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <Button variant="outline" className="w-full" disabled>
              Change Password
            </Button>
            <Button variant="outline" className="w-full" disabled>
              Enable Two-Factor Authentication
            </Button>
          </CardContent>
        </Card>

        {/* Sign Out Card */}
        <Card className="border-destructive/20 bg-destructive/5">
          <CardHeader>
            <CardTitle className="text-destructive">Sign Out</CardTitle>
            <CardDescription>End your current session</CardDescription>
          </CardHeader>
          <CardContent>
            <Button
              onClick={handleLogout}
              className="w-full bg-destructive hover:bg-destructive/90"
              size="lg"
            >
              <LogOut className="h-4 w-4 mr-2" />
              Sign Out
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
