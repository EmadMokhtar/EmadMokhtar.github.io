Title: Code Kata: Fizz Buzz Game
Date: 2011-12-20 22:50
Author: EmadMokhtar
Category: Developer
Tags: code, coding, game, kata, programmer, programming

I stared to practice recently after reading more about how practicing is important for programmer to become professional and one way of practicing is  [Coding Kata]({filename}/Coding Kata.md). I found a lot of problem to implement to practice and perform coding kata.

This post I'll talk about Fizz Buzz Game a.k.a. Bizz Buzz Game, it's numerical/math game, if the number is divisible by 3 replace it with fizz, or if number divisible by 5 replace it with buzz, or if number is divisible by 3 and 5 replace it with fizzbuzz. For example if we count from 1 to 20 it'll be like this: 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz, 16, 17, fizz, 19, buzz.

So how to code this game:

First I thought I can solve this game by:

If (this number is divisible by 3 and not divisible by 5)  return fizz

else if (this number is not divisible by 3 and divisible by 5)  return
buzz

else if (this number is divisible by 3 and divisible by 5)  return
buzzfizz

else if(this number is not divisible by 3 and not divisible by 5)  
return the number

```csharp
        /// <summary>
        /// Solve fizz buzz problem
        /// if number divisible by 3 and not by 5 return fizz
        /// if number divisible by 5 and not by 3 return buzz
        /// if number divisible by 15 return fizzbuzz
        /// </summary>
        /// <param name="number">The number.</param>
        /// <returns>fizz, buzz, or fizzbuzz</returns>
        static public string FizzBuzz(int number)
        {
            string returnString = string.Empty;

            if (number % 3 == 0 && number % 5 != 0)
            {
                returnString = "fizz";
            }
            if (number % 3 != 0 && number % 5 == 0)
            {
                returnString = "buzz";
            }
            if (number % 3 == 0 && number % 5 == 0)
            {
                returnString = "fizzbuzz";
            }
            if (number % 3 != 0 && number % 5 != 0)
            {
                returnString = number.ToString();
            }
            return returnString;
        }
```

But when I look at the code I feel like I can optimize it more by remove
the and between two logical conditions, as the following.

```csharp
        /// <summary>
        /// Solve fizz buzz problem
        /// if number divisible by 3 and not by 5 return fizz
        /// if number divisible by 5 and not by 3 return buzz
        /// if number divisible by 15 return fizzbuzz
        /// </summary>
        /// <param name="number">The number.</param>
        /// <returns>fizz, buzz, or fizzbuzz</returns>
        static public string FizzBuzz(int number)
        {
            string returnString = string.Empty;

                       if (number % 3 == 0)
            {
                if (number % 5 == 0)
                {
                    returnString = "fizzbuzz";

                }
                else if (number % 5 != 0)
                {
                    returnString = "fizz";
                }
            }
            else
            {
                if (number % 5 == 0)
                {
                    returnString = "buzz";
                }
                else if (number % 5 != 0)
                {
                    returnString = number.ToString();
                }
            }
            return returnString;
        }
```

After observing the results, I found that fizzbuzz only appears when the number is divisible by 15, so I rewrite my pseudocodecode

If (this number is divisible by 15)  return buzfizz

else if (this number is divisible by 3)  return fizz

else if (this number is divisible by 5)  return buzz

else  return the number

```csharp
        /// <summary>
        /// Solve fizz buzz problem
        /// if number divisible by 3 and not by 5 return fizz
        /// if number divisible by 5 and not by 3 return buzz
        /// if number divisible by 15 return fizzbuzz
        /// </summary>
        /// <param name="number">The number.</param>
        /// <returns>fizz, buzz, or fizzbuzz</returns>
        static public string FizzBuzz(int number)
        {
            string returnString = string.Empty;

                       if (number % 15 == 0)
            {
                returnString = "fizzbuzz";
            }
            else if (number % 3 == 0)
            {
                returnString = "fizz";
            }
            else if (number % 5 == 0)
            {
                returnString = "buzz";
            }
            else
            {
                returnString = number.ToString();
            }
            return returnString;
        }
```

![output]({filename}/images/fizzbuzzoutput.png)

This Coding Kate done, I've enjoyed it as taook me to collage day's when
having fun solving small problems, I hope you enjoyed it as well. See
you next Coding Kata.
