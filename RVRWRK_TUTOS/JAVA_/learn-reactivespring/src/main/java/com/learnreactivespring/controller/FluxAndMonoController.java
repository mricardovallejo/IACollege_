package com.learnreactivespring.controller;

import io.micrometer.core.annotation.Timed;
import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.Gauge;
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

@RestController
@Timed
public class FluxAndMonoController {

    private final MeterRegistry meterRegistry;

    public FluxAndMonoController(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
    }

    @GetMapping("/flux")
    public Flux<Integer> returnFlux(){

        return Flux.just(1,2,3,4)
               // .delayElements(Duration.ofSeconds(1))
                .log();
    }

    @GetMapping("/mono")
    public Mono<Integer> returnMono(){

        return Mono.just(1)
                .log();

    }

   @GetMapping(value = "/delayedFlux1")
    public Flux<String> delayedFlux1() {

        List<String> names = Arrays.asList("adam1\n", "anna1\n", "jack1\n", "jenny1\n");

        Flux<String> namesFlux = Flux.fromIterable(names)
                .map(s -> processData2(s, 0, 20))
                .log();

        return  namesFlux;

    }

    @GetMapping(value = "/delayedFlux2")
    public Flux<String> delayedFlux2() {

        List<String> names = Arrays.asList("adam2\n", "anna2\n", "jack2\n", "jenny2\n");

        Flux<String> namesFlux = Flux.fromIterable(names)
                .map(s -> processData2(s,100,200))
                //.delayElements(Duration.ofMillis(1000))
                .log();

        return  namesFlux;

    }

    @GetMapping(value = "/delayedFlux3")
    public Flux<String> delayedFlux3() {

        List<String> names = Arrays.asList("adam3\n", "anna3\n", "jack3\n", "jenny3\n");

        Flux<String> namesFlux = Flux.fromIterable(names)
                .map(s -> processData2(s, 300,400))
                .log();

        return  namesFlux;



    }

    private String processData(String s)  {

        addLatency(0, 20);

        return s.toUpperCase();
    }

    private long addLatency(int minimumMs, int maximumMs) {
        long sleepDuration = ThreadLocalRandom.current().nextInt(minimumMs, maximumMs + 1);

        try {
            Thread.sleep(sleepDuration);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        return sleepDuration;
    }

    // Monitoring methods using io.micrometer

    private String processData2(String s, Integer mini, Integer maxi)  {

        //Define important observability parameters
        Counter counter = Counter
                .builder("my.counter")
                .description("counts something important")
                .tag("environment", "test")
                .tag("region", "us-east")
                .register(meterRegistry);

        long latency = addLatency(mini, maxi);

        Gauge.builder("my.gauge3", latency, Long::longValue)
                .description("processDataCall")
                .register(meterRegistry);

        counter.increment();


        return s.toUpperCase();
    }


//-----------------------------------------------------------------------------------------------------
    // Reactive transformations

    @GetMapping(value = "/tranformUsingMap")
    public Flux<String> tranformUsingMap() {

        List<String> names = Arrays.asList("adam", "anna", "jack", "jenny");

        Flux<String> namesFlux = Flux.fromIterable(names)
                .log()
                //.filter(s -> s.length()>4)
                .map(s -> s.toUpperCase()+"\n");

        return  namesFlux;

    }























/*    @GetMapping(value = "/tranformUsingMap2")
    public Flux<String> tranformUsingMap2() {

        List<String> names = Arrays.asList("adam", "anna", "jack", "jenny");

        Flux<String> namesFlux = Flux.fromIterable(names)
                //.filter(s -> s.length()>4)
                .map(s -> processData2(s))
                .subscribeOn(Schedulers.parallel())
                .log();

        return  namesFlux.log();

    }*/

/*
    @GetMapping(value = "/tranformUsingMap3")
    public Flux<String> tranformUsingMap3() {

        List<String> names = Arrays.asList("adam", "anna", "jack", "jenny");

        Flux<String> namesFlux = Flux.fromIterable(names)
                //.filter(s -> s.length()>4)
                .map(s -> processData2(s))
                .subscribeOn(Schedulers.parallel())
                .log();

        return  namesFlux.log();

    }

    @GetMapping(value = "/tranformUsingFlatMap")
    public Flux<String> tranformUsingFlatMap() {

        List<String> names = Arrays.asList("adam", "anna", "jack", "jenny");

        Flux<String> namesFlux = Flux.fromIterable(names)
                .log()
                .flatMap(value ->
                                Mono.just(processData2(value))
                                        .subscribeOn(Schedulers.parallel()),
                        2);

        return  namesFlux.log();

    }
*/




}
