import React from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import Link from 'next/link'
import { TestType } from '@/lib/types'
import { testInfo } from '@/lib/test-data'

interface TestCardProps {
  testType: TestType
  completed?: boolean
  lastTaken?: string
}

export function TestCard({ testType, completed, lastTaken }: TestCardProps) {
  const info = testInfo[testType]

  return (
    <Link href={`/tests/${testType}`}>
      <Card className="hover:shadow-lg transition-shadow duration-200 cursor-pointer h-full">
        <CardHeader>
          <CardTitle className="text-lg">{info.name}</CardTitle>
          <CardDescription>{info.description}</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <p className="text-muted-foreground">Questions</p>
              <p className="font-semibold text-foreground">{info.questions}</p>
            </div>
            <div>
              <p className="text-muted-foreground">Duration</p>
              <p className="font-semibold text-foreground">{info.duration}</p>
            </div>
          </div>
          {completed && (
            <div className="pt-2 border-t border-border">
              <p className="text-xs text-muted-foreground">
                Last taken: {lastTaken}
              </p>
            </div>
          )}
          <Button className="w-full mt-4">
            {completed ? 'Retake Test' : 'Start Test'}
          </Button>
        </CardContent>
      </Card>
    </Link>
  )
}
