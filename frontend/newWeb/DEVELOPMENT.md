# Development Guide - MindWell Platform

## Architecture Overview

### Tech Stack
- **Frontend Framework**: React 18 + Next.js 16
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui components
- **Forms**: React Hook Form + Zod validation
- **HTTP Client**: Axios
- **State Management**: Context API + useState
- **Icons**: Lucide React

### Folder Structure

```
project-root/
├── app/                    # Next.js app directory
│   ├── auth/              # Authentication pages
│   │   ├── login/
│   │   ├── signup/
│   │   └── forgot-password/
│   ├── tests/[testType]/  # Dynamic test pages
│   ├── dashboard/         # Main dashboard
│   ├── profile/           # User profile
│   ├── layout.tsx         # Root layout with providers
│   ├── page.tsx           # Landing page
│   └── globals.css        # Theme & global styles
│
├── lib/                   # Utilities and logic
│   ├── types.ts          # TypeScript interfaces
│   ├── schemas.ts        # Zod validation schemas
│   ├── test-data.ts      # Questions & scoring logic
│   ├── auth-context.tsx  # Auth state management
│   └── api-client.ts     # Axios instance
│
├── components/
│   ├── ui/               # shadcn/ui components
│   ├── form-field.tsx    # Custom form wrapper
│   ├── test-card.tsx     # Test selection card
│   └── result-card.tsx   # Results display
│
├── public/               # Static assets
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.mjs
```

## Core Concepts

### Type System

All types are defined in `lib/types.ts` for consistency:

```typescript
// Test types
export type TestType = 'phq9' | 'bdi2' | 'cesd' | 'ai-test'

// Test structure
export interface TestQuestion {
  id: string
  text: string
  options: { value: number; label: string }[]
}

// Scoring result
export interface TestResult {
  score: number
  interpretation: string
  category: 'minimal' | 'mild' | 'moderate' | 'moderately-severe' | 'severe'
  recommendations: string[]
  severity: 'low' | 'moderate' | 'elevated' | 'high'
}
```

### Validation

All forms use **Zod schemas** with **React Hook Form**:

```typescript
// Define schema
const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(1)
})

// Use in component
const { register, formState: { errors } } = useForm({
  resolver: zodResolver(loginSchema)
})
```

**Important**: Always validate on both frontend AND backend.

### State Management

**Global State** (Auth):
```typescript
// In AuthProvider
const [user, setUser] = useState<UserProfile | null>(null)
const [isAuthenticated, setIsAuthenticated] = useState(false)

// Use in components
const { user, login, logout } = useAuth()
```

**Local State** (Forms/UI):
```typescript
// Form responses during test
const [currentAnswers, setCurrentAnswers] = useState({})

// UI state
const [isLoading, setIsLoading] = useState(false)
```

**Never use Redux** - keep it simple with Context + useState.

## Adding New Features

### Add a New Test Type

1. **Update Types** (`lib/types.ts`):
```typescript
export type TestType = 'phq9' | 'bdi2' | 'cesd' | 'ai-test' | 'new-test'
```

2. **Add Questions** (`lib/test-data.ts`):
```typescript
export const testQuestions: Record<TestType, TestQuestion[]> = {
  // ... existing tests
  'new-test': [
    {
      id: 'new_1',
      text: 'Question text here',
      options: [
        { value: 0, label: 'Never' },
        { value: 1, label: 'Sometimes' },
        // ... more options
      ]
    }
    // ... more questions
  ]
}
```

3. **Add Scoring Logic** (in `calculateTestScore()`):
```typescript
case 'new-test': {
  // Scoring logic based on score range
  if (score <= 10) {
    category = 'minimal'
    severity = 'low'
    interpretation = '...'
    recommendations = [...]
  }
  // ... more conditions
  break
}
```

4. **Add Test Info**:
```typescript
export const testInfo = {
  // ... existing
  'new-test': {
    name: 'New Test Name',
    description: 'Description of test',
    duration: '5-10 minutes',
    questions: 10,
  }
}
```

5. **No page changes needed!** The dynamic route `app/tests/[testType]/page.tsx` handles all tests.

### Add a New Form Page

1. **Create Zod Schema** (`lib/schemas.ts`):
```typescript
export const myFormSchema = z.object({
  field1: z.string().min(1, 'Required'),
  field2: z.string().email('Invalid email'),
})

export type MyFormInput = z.infer<typeof myFormSchema>
```

2. **Create Component** (`app/my-form/page.tsx`):
```typescript
'use client'

import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { myFormSchema, MyFormInput } from '@/lib/schemas'

export default function MyFormPage() {
  const { register, handleSubmit, formState: { errors } } = useForm<MyFormInput>({
    resolver: zodResolver(myFormSchema)
  })

  async function onSubmit(data: MyFormInput) {
    // Handle submission
  }

  return (
    // JSX with form
  )
}
```

### Add a New API Endpoint Integration

1. **Create API function** (in `lib/api-client.ts` or new file):
```typescript
export async function fetchTestHistory(userId: string) {
  const response = await apiClient.get(`/tests/history?userId=${userId}`)
  return response.data
}
```

2. **Use in component**:
```typescript
const [history, setHistory] = useState([])
const [loading, setLoading] = useState(false)

useEffect(() => {
  const loadHistory = async () => {
    setLoading(true)
    try {
      const data = await fetchTestHistory(user.id)
      setHistory(data)
    } catch (error) {
      console.error('Failed to load history:', error)
    } finally {
      setLoading(false)
    }
  }
  
  loadHistory()
}, [user.id])
```

3. **Handle errors gracefully**:
```typescript
// Don't expose internal API errors to user
const message = error.response?.data?.message || 'Failed to load data'
setError(message)
```

## Styling Guidelines

### Color System

All colors are in `app/globals.css` as CSS custom properties:

```css
--primary: oklch(0.455 0.166 258.9)    /* Medical Blue */
--secondary: oklch(0.547 0.136 142.456) /* Calming Green */
--accent: oklch(0.7 0.15 205.4)         /* Cyan */
```

Use semantic class names:
```html
<!-- ✅ Good -->
<div className="bg-primary text-primary-foreground">

<!-- ❌ Bad -->
<div className="bg-[#0066FF] text-white">
```

### Component Patterns

All components follow consistent patterns:

```typescript
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

export function MyComponent() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Title</CardTitle>
      </CardHeader>
      <CardContent>
        {/* Content */}
      </CardContent>
    </Card>
  )
}
```

### Responsive Design

Mobile-first approach with Tailwind breakpoints:

```html
<!-- Starts mobile, expands on larger screens -->
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
```

Breakpoints:
- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px

## Accessibility Requirements

Every interactive element must have:

1. **Labels** - Associated with inputs
```tsx
<FormField label="Email" error={errors.email} required>
  <Input {...register('email')} />
</FormField>
```

2. **Focus States** - Visible outline
```css
:focus {
  outline: 2px solid var(--ring);
}
```

3. **ARIA Labels** - When semantic HTML insufficient
```jsx
<button aria-label="Close dialog">×</button>
```

4. **Keyboard Navigation** - Tab through all elements
- Test with Tab key
- Check focus order makes sense
- No focus traps

5. **Contrast** - WCAG AA minimum
- Text vs background: 4.5:1 (normal text)
- Large text: 3:1
- Use `Skeleton` for loading states

## Testing

### Manual Testing Checklist

- [ ] **Authentication Flow**
  - [ ] Sign up creates account
  - [ ] Login with correct credentials works
  - [ ] Incorrect credentials show error
  - [ ] Forgot password flow completes
  - [ ] Logout clears session

- [ ] **Assessment Flow**
  - [ ] All tests load questions correctly
  - [ ] Progress bar updates
  - [ ] All answers required validation works
  - [ ] Results calculate immediately
  - [ ] Interpretations are appropriate

- [ ] **Responsive Design**
  - [ ] Mobile (375px width)
  - [ ] Tablet (768px width)
  - [ ] Desktop (1024px+ width)
  - [ ] Touch targets are ≥44x44px

- [ ] **Accessibility**
  - [ ] Tab navigation works throughout
  - [ ] Focus indicators visible
  - [ ] Form errors associated with inputs
  - [ ] No keyboard traps
  - [ ] Images have alt text

- [ ] **Security**
  - [ ] Passwords not in console/network
  - [ ] Token managed securely
  - [ ] Protected routes require auth
  - [ ] CORS configured correctly

## Performance Tips

### Optimize Components

**Use React.memo for expensive components:**
```typescript
const TestCard = React.memo(({ test }: Props) => {
  return <Card>{/* ... */}</Card>
})
```

**Lazy load pages:**
```typescript
const Dashboard = lazy(() => import('@/app/dashboard'))

<Suspense fallback={<LoadingSpinner />}>
  <Dashboard />
</Suspense>
```

**Avoid unnecessary re-renders:**
```typescript
// ✅ Dependency array is correct
useEffect(() => {
  fetchData(userId)
}, [userId])

// ❌ Runs on every render
useEffect(() => {
  fetchData(userId)
}) // Missing dependency array!
```

### Bundle Size

- Check with `next/bundle-analyzer`
- Remove unused imports
- Use dynamic imports for heavy libraries

## Database Integration

### Expected API Endpoints

When implementing backend, create these endpoints:

**Authentication:**
- `POST /api/auth/signup` - Create account
- `POST /api/auth/login` - Authenticate user
- `GET /api/auth/me` - Get current user
- `POST /api/auth/logout` - Logout
- `POST /api/auth/forgot-password` - Start password reset
- `POST /api/auth/reset-password` - Complete password reset

**Tests:**
- `POST /api/tests/submit` - Submit test response
- `GET /api/tests/history` - Get past results
- `GET /api/tests/:id` - Get single result

**Profile:**
- `GET /api/profile` - Get profile
- `PUT /api/profile` - Update profile
- `PUT /api/profile/password` - Change password

### Database Schema

**Users Table:**
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR UNIQUE NOT NULL,
  username VARCHAR UNIQUE NOT NULL,
  password_hash VARCHAR NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
)
```

**Test Results Table:**
```sql
CREATE TABLE test_results (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  test_type VARCHAR NOT NULL,
  score INT NOT NULL,
  responses JSONB,
  created_at TIMESTAMP DEFAULT NOW()
)
```

## Deployment

### Environment Variables

Create `.env.local` with:
```
NEXT_PUBLIC_API_URL=your_api_url
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your_google_id
```

### Build & Deploy

```bash
# Build for production
pnpm run build

# Test production build
pnpm start

# Deploy to Vercel (recommended)
vercel deploy
```

## Common Issues & Solutions

### Form Values Not Updating
**Problem**: React Hook Form values not reflecting in component
```typescript
// ✅ Correct - Use Controller for custom components
<Controller
  name="answer"
  control={control}
  render={({ field }) => <RadioGroup {...field} />}
/>

// ❌ Wrong - Missing Controller
<RadioGroup {...register('answer')} />
```

### Validation Not Working
**Problem**: Zod schemas not validating properly
```typescript
// ✅ Frontend validation
const { errors } = useForm({
  resolver: zodResolver(schema)
})

// 🔴 MISSING: Backend validation (required!)
// Always validate server-side too!
```

### Test Results Not Calculating
**Problem**: Score not appearing after submission
```typescript
// Ensure calculateTestScore is imported
import { calculateTestScore } from '@/lib/test-data'

// Call it with responses
const result = calculateTestScore(testType, formData)
```

### Auth Context Not Available
**Problem**: `useAuth()` throws "must be used within AuthProvider"
```typescript
// Ensure AuthProvider wraps children in layout.tsx
<AuthProvider>
  {children}
</AuthProvider>
```

## Code Style Rules

### Naming Conventions
```typescript
// ✅ Descriptive, clear names
const handleFormSubmit = () => {}
const userAuthenticationStatus = 'logged-in'
const testResultInterpretation = '...'

// ❌ Vague names
const handleSubmit = () => {} // Too generic
const x = 'logged-in'
const result = '...'
```

### File Organization
- 1 component per file (unless very small)
- Keep files under 300 lines
- Extract reusable logic to utilities

### Comments
```typescript
// ✅ Explain WHY, not WHAT
// We fetch user data on mount only if authenticated
useEffect(() => {
  if (isAuthenticated) fetchUserData()
}, [isAuthenticated])

// ❌ Comment what code already says
// Set user to null
setUser(null)
```

## Resources

- [Next.js Docs](https://nextjs.org/docs)
- [React Docs](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [shadcn/ui Components](https://ui.shadcn.com)
- [Zod Validation](https://zod.dev)
- [React Hook Form](https://react-hook-form.com)

## Questions?

Review the code comments and existing patterns before implementing new features. When in doubt, follow the established patterns in similar components.
