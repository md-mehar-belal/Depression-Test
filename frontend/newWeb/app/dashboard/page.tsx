'use client'

import React from 'react'
import { useAuth } from '@/lib/auth-context'
import { useRouter } from 'next/navigation'
import { Skeleton } from '@/components/ui/skeleton'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { TestCard } from '@/components/test-card'
import { LogOut, User, BarChart3, History } from 'lucide-react'
import Link from 'next/link'

export default function DashboardPage() {
  const { user, loading, logout } = useAuth()
  const router = useRouter()

  React.useEffect(() => {
    if (!loading && !user) {
      router.push('/auth/login?from=/dashboard')
    }
  }, [user, loading, router])

  const handleLogout = async () => {
    await logout()
    router.push('/')
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-background">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <Skeleton className="h-12 w-48 mb-8" />
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <Skeleton className="h-32" />
            <Skeleton className="h-32" />
            <Skeleton className="h-32" />
            <Skeleton className="h-32" />
          </div>
        </div>
      </div>
    )
  }

  if (!user) {
    return null
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-background to-muted">
      {/* Header */}
      <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-foreground">Dashboard</h1>
              <p className="text-muted-foreground">Welcome back, {user.username}</p>
            </div>
            <div className="flex items-center gap-4">
              <Link href="/profile">
                <Button variant="outline" size="sm" className="gap-2">
                  <User className="h-4 w-4" />
                  Profile
                </Button>
              </Link>
              <Button variant="outline" size="sm" onClick={handleLogout} className="gap-2">
                <LogOut className="h-4 w-4" />
                Sign Out
              </Button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Quick Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Total Tests Completed</p>
                  <p className="text-3xl font-bold text-primary">0</p>
                </div>
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center">
                  <BarChart3 className="h-6 w-6 text-primary" />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Last Assessment</p>
                  <p className="text-lg font-semibold text-foreground">—</p>
                </div>
                <div className="h-12 w-12 rounded-lg bg-secondary/10 flex items-center justify-center">
                  <History className="h-6 w-6 text-secondary" />
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="pt-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-muted-foreground mb-1">Member Since</p>
                  <p className="text-lg font-semibold text-foreground">
                    {new Date(user.createdAt).toLocaleDateString()}
                  </p>
                </div>
                <div className="h-12 w-12 rounded-lg bg-accent/10 flex items-center justify-center">
                  <User className="h-6 w-6 text-accent" />
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Tests Section */}
        <div className="mb-12">
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-foreground mb-2">Available Assessments</h2>
            <p className="text-muted-foreground">
              Choose an assessment to understand your emotional well-being
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <TestCard testType="phq9" />
            <TestCard testType="bdi2" />
            <TestCard testType="cesd" />
            <TestCard testType="ai-test" />
          </div>
        </div>

        {/* Recent Activity */}
        <div>
          <div className="mb-8">
            <h2 className="text-3xl font-bold text-foreground mb-2">Recent Results</h2>
            <p className="text-muted-foreground">No assessments completed yet</p>
          </div>

          <Card>
            <CardContent className="pt-6">
              <div className="text-center py-12">
                <p className="text-muted-foreground mb-4">
                  Start your first assessment to track your progress and get personalized insights.
                </p>
                <Link href="/tests/phq9">
                  <Button>Take Your First Assessment</Button>
                </Link>
              </div>
            </CardContent>
          </Card>
        </div>
      </main>
    </div>
  )
}
