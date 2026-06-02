// 'use client';

// import React, { useState, useEffect } from 'react';
// import { Card } from './ui/card';
// import Link from 'next/link';
// import { ChevronLeft, ChevronRight } from 'lucide-react';

// interface AssessmentTest {
//   id: string;
//   title: string;
//   emoji: string;
//   description: string;
//   questions: number;
//   duration: string;
//   href: string;
//   gradient?: boolean;
// }

// const TESTS: AssessmentTest[] = [
//   {
//     id: 'phq9',
//     title: 'PHQ-9',
//     emoji: '😔',
//     description: 'Patient Health Questionnaire - assess depression levels',
//     questions: 9,
//     duration: '~5 min',
//     href: '/test/phq9',
//   },
//   {
//     id: 'bdi2',
//     title: 'BDI-2',
//     emoji: '🌧️',
//     description: 'Beck Depression Inventory - comprehensive assessment',
//     questions: 21,
//     duration: '~10 min',
//     href: '/test/bdi2',
//   },
//   {
//     id: 'cesd',
//     title: 'CES-D',
//     emoji: '😟',
//     description: 'Center for Epidemiologic Studies - quick screening',
//     questions: 20,
//     duration: '~8 min',
//     href: '/test/cesd',
//   },
//   {
//     id: 'all59',
//     title: 'Complete Assessment',
//     emoji: '⭐',
//     description: 'All 59 questions for the most comprehensive AI-powered analysis',
//     questions: 59,
//     duration: '~30 min',
//     href: '/test/all59',
//     gradient: true,
//   },
// ];

// export function AssessmentCarousel() {
//   const [currentIndex, setCurrentIndex] = useState(1); // Start at BDI-2 (middle)
//   const [isAutoPlay, setIsAutoPlay] = useState(true);

//   // Auto-play carousel
//   useEffect(() => {
//     if (!isAutoPlay) return;

//     const timer = setInterval(() => {
//       setCurrentIndex((prev) => (prev + 1) % TESTS.length);
//     }, 5000);

//     return () => clearInterval(timer);
//   }, [isAutoPlay]);

//   const goToPrevious = () => {
//     setIsAutoPlay(false);
//     setCurrentIndex((prev) => (prev - 1 + TESTS.length) % TESTS.length);
//   };

//   const goToNext = () => {
//     setIsAutoPlay(false);
//     setCurrentIndex((prev) => (prev + 1) % TESTS.length);
//   };

//   const goToSlide = (index: number) => {
//     setIsAutoPlay(false);
//     setCurrentIndex(index);
//   };

//   const getCardPosition = (index: number) => {
//     const distance = (index - currentIndex + TESTS.length) % TESTS.length;

//     if (distance === 0) {
//       return { scale: 1, opacity: 1, x: 0, zIndex: 30 };
//     } else if (distance === 1 || distance === TESTS.length - 1) {
//       const isRight = distance === 1;
//       return {
//         scale: 0.7,
//         opacity: 0.6,
//         x: isRight ? 300 : -300,
//         zIndex: 20,
//       };
//     } else {
//       return { scale: 0.5, opacity: 0.3, x: 0, zIndex: 10 };
//     }
//   };

//   return (
//     <div className="relative w-full py-12">
//       {/* Carousel Container */}
//       <div className="relative h-96 flex items-center justify-center overflow-hidden">
//         {/* Cards */}
//         <div className="relative w-full h-full">
//           {TESTS.map((test, index) => {
//             const position = getCardPosition(index);
//             const isCenter = index === currentIndex;

//             return (
//               <div
//                 key={test.id}
//                 className="absolute inset-0 flex items-center justify-center transition-all duration-500 ease-out"
//                 style={{
//                   transform: `translateX(${position.x}px) scale(${position.scale})`,
//                   opacity: position.opacity,
//                   zIndex: position.zIndex,
//                 }}
//               >
//                 {isCenter ? (
//                   <Link
//                     href={test.href}
//                     className="w-80 h-full flex transition-all duration-300 cursor-pointer"
//                   >
//                     <Card
//                       className={`w-full border-0 shadow-lg hover:shadow-xl transition-all cursor-pointer overflow-hidden group flex flex-col ${
//                         test.gradient
//                           ? 'bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-200'
//                           : 'bg-white'
//                       }`}
//                     >
//                       <div className="p-8 flex flex-col h-full">
//                         <div className="text-5xl mb-6 group-hover:scale-125 transition-transform duration-300">
//                           {test.emoji}
//                         </div>
//                         <h3 className="text-2xl font-bold text-gray-900 mb-3">
//                           {test.title}
//                         </h3>
//                         <p className="text-gray-600 text-sm mb-6 flex-grow leading-relaxed">
//                           {test.description}
//                         </p>
//                         <div className="flex items-center justify-between pt-6 border-t border-gray-100">
//                           <span className="text-xs font-semibold text-gray-600">
//                             {test.questions} Questions
//                           </span>
//                           <span className="text-xs text-gray-500">{test.duration}</span>
//                         </div>
//                       </div>
//                     </Card>
//                   </Link>
//                 ) : (
//                   <div
//                     className="w-80 h-full flex transition-all duration-300 cursor-pointer"
//                     onClick={() => goToSlide(index)}
//                   >
//                     <Card
//                       className={`w-full border-0 shadow-lg hover:shadow-xl transition-all cursor-pointer overflow-hidden group flex flex-col ${
//                         test.gradient
//                           ? 'bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-200'
//                           : 'bg-white'
//                       }`}
//                     >
//                       <div className="p-8 flex flex-col h-full">
//                         <div className="text-5xl mb-6 group-hover:scale-125 transition-transform duration-300">
//                           {test.emoji}
//                         </div>
//                         <h3 className="text-2xl font-bold text-gray-900 mb-3">
//                           {test.title}
//                         </h3>
//                         <p className="text-gray-600 text-sm mb-6 flex-grow leading-relaxed">
//                           {test.description}
//                         </p>
//                         <div className="flex items-center justify-between pt-6 border-t border-gray-100">
//                           <span className="text-xs font-semibold text-gray-600">
//                             {test.questions} Questions
//                           </span>
//                           <span className="text-xs text-gray-500">{test.duration}</span>
//                         </div>
//                       </div>
//                     </Card>
//                   </div>
//                 )}
//               </div>
//             );
//           })}
//         </div>
//       </div>

//       {/* Navigation Arrows */}
//       <div className="flex items-center justify-center gap-4 mt-8">
//         <button
//           onClick={goToPrevious}
//           className="p-3 rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
//           aria-label="Previous assessment"
//         >
//           <ChevronLeft className="w-6 h-6" />
//         </button>

//         {/* Dot Indicators */}
//         <div className="flex gap-2">
//           {TESTS.map((_, index) => (
//             <button
//               key={index}
//               onClick={() => goToSlide(index)}
//               className={`w-3 h-3 rounded-full transition-all duration-300 ${
//                 index === currentIndex
//                   ? 'bg-blue-600 w-8'
//                   : 'bg-gray-300 hover:bg-gray-400'
//               }`}
//               aria-label={`Go to slide ${index + 1}`}
//             />
//           ))}
//         </div>

//         <button
//           onClick={goToNext}
//           className="p-3 rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
//           aria-label="Next assessment"
//         >
//           <ChevronRight className="w-6 h-6" />
//         </button>
//       </div>

//       {/* Hint Text */}
//       <div className="text-center mt-6 text-gray-600 text-sm">
//         Click the card to start this assessment or use arrows to explore
//       </div>
//     </div>
//   );
// }
"use client";

import React, { useState, useEffect } from 'react';
import { Card } from './ui/card';
import Link from 'next/link';
import { ChevronLeft, ChevronRight, Clock, ListChecks } from 'lucide-react';

interface AssessmentTest {
  id: string;
  title: string;
  icon: string;
  description: string;
  questions: number;
  duration: string;
  href: string;
  gradient?: boolean;
  color: string;
}

const TESTS: AssessmentTest[] = [
  {
    id: 'phq9',
    title: 'PHQ-9',
    icon: '●',
    description: 'Patient Health Questionnaire - assess depression levels',
    questions: 9,
    duration: '~5 min',
    href: '/test/phq9',
    color: 'blue',
  }, 
  {
    id: 'bdi2',
    title: 'BDI-2',
    icon: '◆',
    description: 'Beck Depression Inventory - comprehensive assessment',
    questions: 21,
    duration: '~10 min',
    href: '/test/bdi2',
    color: 'indigo',
  },
  {
    id: 'cesd',
    title: 'CES-D',
    icon: '▲',
    description: 'Center for Epidemiologic Studies - quick screening',
    questions: 20,
    duration: '~8 min',
    href: '/test/cesd',
    color: 'purple',
  },
  {
    id: 'all59',
    title: 'Complete Assessment',
    icon: '★',
    description: 'All 59 questions for the most comprehensive AI-powered analysis',
    questions: 59,
    duration: '~30 min',
    href: '/test/all59',
    gradient: true,
    color: 'gradient',
  },
];

export function AssessmentCarousel() {
  const [currentIndex, setCurrentIndex] = useState(1);
  const [isAutoPlay, setIsAutoPlay] = useState(true);

  useEffect(() => {
    if (!isAutoPlay) return;

    const timer = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % TESTS.length);
    }, 5000);

    return () => clearInterval(timer);
  }, [isAutoPlay]);

  const goToPrevious = () => {
    setIsAutoPlay(false);
    setCurrentIndex((prev) => (prev - 1 + TESTS.length) % TESTS.length);
  };

  const goToNext = () => {
    setIsAutoPlay(false);
    setCurrentIndex((prev) => (prev + 1) % TESTS.length);
  };

  const goToSlide = (index: number) => {
    setIsAutoPlay(false);
    setCurrentIndex(index);
  };

  const getCardPosition = (index: number) => {
    const distance = (index - currentIndex + TESTS.length) % TESTS.length;

    if (distance === 0) {
      return { scale: 1, opacity: 1, x: 0, zIndex: 30 };
    } else if (distance === 1 || distance === TESTS.length - 1) {
      const isRight = distance === 1;
      return {
        scale: 0.7,
        opacity: 0.6,
        x: isRight ? 300 : -300,
        zIndex: 20,
      };
    } else {
      return { scale: 0.5, opacity: 0.3, x: 0, zIndex: 10 };
    }
  };

  const getColorClasses = (color: string, isCenter: boolean) => {
    if (color === 'gradient') {
      return isCenter
        ? 'bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-300 shadow-xl'
        : 'bg-gradient-to-br from-blue-50 to-indigo-50 border-2 border-blue-200';
    }
    
    const colorMap: Record<string, string> = {
      blue: isCenter 
        ? 'bg-gradient-to-br from-blue-50 to-blue-100 border-2 border-blue-400 shadow-xl' 
        : 'bg-gradient-to-br from-blue-50 to-blue-100 border-2 border-blue-200',
      indigo: isCenter
        ? 'bg-gradient-to-br from-indigo-50 to-indigo-100 border-2 border-indigo-400 shadow-xl'
        : 'bg-gradient-to-br from-indigo-50 to-indigo-100 border-2 border-indigo-200',
      purple: isCenter
        ? 'bg-gradient-to-br from-purple-50 to-purple-100 border-2 border-purple-400 shadow-xl'
        : 'bg-gradient-to-br from-purple-50 to-purple-100 border-2 border-purple-200',
    };
    
    return colorMap[color] || 'bg-white';
  };

  const getIconColor = (color: string) => {
    const colorMap: Record<string, string> = {
      blue: 'text-blue-600',
      indigo: 'text-indigo-600',
      purple: 'text-purple-600',
      gradient: 'text-blue-600',
    };
    return colorMap[color] || 'text-gray-600';
  };

  return (
    <div className="relative w-full py-12">
      <div className="relative h-96 flex items-center justify-center overflow-hidden">
        <div className="relative w-full h-full">
          {TESTS.map((test, index) => {
            const position = getCardPosition(index);
            const isCenter = index === currentIndex;

            return (
              <div
                key={test.id}
                className="absolute inset-0 flex items-center justify-center transition-all duration-500 ease-out"
                style={{
                  transform: `translateX(${position.x}px) scale(${position.scale})`,
                  opacity: position.opacity,
                  zIndex: position.zIndex,
                }}
              >
                {isCenter ? (
                  <Link
                    href={test.href}
                    className="w-80 h-full flex transition-all duration-300 cursor-pointer"
                  >
                    <Card
                      className={`w-full border-0 overflow-hidden group flex flex-col ${getColorClasses(test.color, true)}`}
                    >
                      <div className="p-8 flex flex-col h-full">
                        <div className={`w-14 h-14 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300 ${getIconColor(test.color)} bg-current opacity-10`}>
                          <span className="text-3xl font-bold">{test.icon}</span>
                        </div>
                        <h3 className="text-2xl font-bold text-gray-900 mb-3">
                          {test.title}
                        </h3>
                        <p className="text-gray-600 text-sm mb-6 flex-grow leading-relaxed">
                          {test.description}
                        </p>
                        <div className="flex items-center justify-between pt-6 border-t border-gray-200/50">
                          <div className="flex items-center gap-2 text-xs font-semibold text-gray-700">
                            <ListChecks className="w-4 h-4" />
                            {test.questions} Questions
                          </div>
                          <div className="flex items-center gap-2 text-xs text-gray-500">
                            <Clock className="w-4 h-4" />
                            {test.duration}
                          </div>
                        </div>
                      </div>
                    </Card>
                  </Link>
                ) : (
                  <div
                    className="w-80 h-full flex transition-all duration-300 cursor-pointer"
                    onClick={() => goToSlide(index)}
                  >
                    <Card
                      className={`w-full border-0 overflow-hidden group flex flex-col ${getColorClasses(test.color, false)}`}
                    >
                      <div className="p-8 flex flex-col h-full">
                        <div className={`w-14 h-14 rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300 ${getIconColor(test.color)} bg-current opacity-10`}>
                          <span className="text-3xl font-bold">{test.icon}</span>
                        </div>
                        <h3 className="text-2xl font-bold text-gray-900 mb-3">
                          {test.title}
                        </h3>
                        <p className="text-gray-600 text-sm mb-6 flex-grow leading-relaxed">
                          {test.description}
                        </p>
                        <div className="flex items-center justify-between pt-6 border-t border-gray-200/50">
                          <div className="flex items-center gap-2 text-xs font-semibold text-gray-700">
                            <ListChecks className="w-4 h-4" />
                            {test.questions} Questions
                          </div>
                          <div className="flex items-center gap-2 text-xs text-gray-500">
                            <Clock className="w-4 h-4" />
                            {test.duration}
                          </div>
                        </div>
                      </div>
                    </Card>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

      <div className="flex items-center justify-center gap-4 mt-8">
        <button
          onClick={goToPrevious}
          className="p-3 rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
          aria-label="Previous assessment"
        >
          <ChevronLeft className="w-6 h-6" />
        </button>

        <div className="flex gap-2">
          {TESTS.map((_, index) => (
            <button
              key={index}
              onClick={() => goToSlide(index)}
              className={`w-3 h-3 rounded-full transition-all duration-300 ${
                index === currentIndex
                  ? 'bg-blue-600 w-8'
                  : 'bg-gray-300 hover:bg-gray-400'
              }`}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>

        <button
          onClick={goToNext}
          className="p-3 rounded-full bg-blue-600 text-white hover:bg-blue-700 transition-colors shadow-lg hover:shadow-xl"
          aria-label="Next assessment"
        >
          <ChevronRight className="w-6 h-6" />
        </button>
      </div>

      <div className="text-center mt-6 text-gray-600 text-sm">
        Click the card to start this assessment or use arrows to explore
      </div>
    </div>
  );
}