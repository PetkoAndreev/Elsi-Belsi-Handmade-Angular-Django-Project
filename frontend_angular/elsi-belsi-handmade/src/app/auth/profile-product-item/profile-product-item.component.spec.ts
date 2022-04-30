import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileProductItemComponent } from './profile-product-item.component';

describe('ProfileProductItemComponent', () => {
  let component: ProfileProductItemComponent;
  let fixture: ComponentFixture<ProfileProductItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProfileProductItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfileProductItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
