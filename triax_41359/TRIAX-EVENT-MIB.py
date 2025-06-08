# SNMP MIB module (TRIAX-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/triax_41359/TRIAX-EVENT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:41:28 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class TriaxPerceivedEventSeverityType(Integer32):
    """Custom type TriaxPerceivedEventSeverityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("indeterminate", 1),
          ("info", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )





class TriaxEventCategoryType(Integer32):
    """Custom type TriaxEventCategoryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("GUI", 1),
          ("other", 2),
          ("equipment", 3),
          ("environmental", 4))
    )





class TriaxEventProbableCause(Integer32):
    """Custom type TriaxEventProbableCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("None", 1),
          ("PowerOn", 2),
          ("LossOfPower", 3),
          ("Reset", 4),
          ("Failure", 5),
          ("SystemWasResetFromGUI", 6),
          ("WatchdogReset", 7),
          ("SoftwareReset", 8),
          ("AssertFailure", 9),
          ("HWWatchdogTriggeredNoAssertsFound", 10),
          ("SystemMainsWasRemoved", 11),
          ("BackendRestarted", 12),
          ("FrontendRestarted", 13),
          ("InterlinkDisconnected", 14),
          ("VideoDecodingError", 15),
          ("CIDescramblingError", 16),
          ("CICommunicationDown", 17),
          ("InterlinkConnected", 18),
          ("CIDescramblingOK", 19),
          ("CICommunicationUp", 20),
          ("VideoDecodingOK", 21),
          ("PSUNoLongerWorks", 22),
          ("SDCorruptionDetected", 23))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Triax_ObjectIdentity = ObjectIdentity
triax = _Triax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41359)
)
_He_ObjectIdentity = ObjectIdentity
he = _He_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41359, 1)
)
_EventTraps_ObjectIdentity = ObjectIdentity
eventTraps = _EventTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0)
)
_EventMIB_ObjectIdentity = ObjectIdentity
eventMIB = _EventMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2)
)
_CurrentEventTable_Object = MibTable
currentEventTable = _CurrentEventTable_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1)
)
if mibBuilder.loadTexts:
    currentEventTable.setStatus("mandatory")
_CurrentEventEntry_Object = MibTableRow
currentEventEntry = _CurrentEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1)
)
currentEventEntry.setIndexNames(
    (0, "TRIAX-EVENT-MIB", "triaxSequenceNumber"),
)
if mibBuilder.loadTexts:
    currentEventEntry.setStatus("mandatory")
_TriaxManagedObjectClass_Type = DisplayString
_TriaxManagedObjectClass_Object = MibTableColumn
triaxManagedObjectClass = _TriaxManagedObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 1),
    _TriaxManagedObjectClass_Type()
)
triaxManagedObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxManagedObjectClass.setStatus("mandatory")
_TriaxManagedObjedctInstanceClass_Type = DisplayString
_TriaxManagedObjedctInstanceClass_Object = MibTableColumn
triaxManagedObjedctInstanceClass = _TriaxManagedObjedctInstanceClass_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 2),
    _TriaxManagedObjedctInstanceClass_Type()
)
triaxManagedObjedctInstanceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxManagedObjedctInstanceClass.setStatus("mandatory")
_TriaxSequenceNumber_Type = Unsigned32
_TriaxSequenceNumber_Object = MibTableColumn
triaxSequenceNumber = _TriaxSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 3),
    _TriaxSequenceNumber_Type()
)
triaxSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxSequenceNumber.setStatus("mandatory")
_TriaxPerceivedSeverity_Type = TriaxPerceivedEventSeverityType
_TriaxPerceivedSeverity_Object = MibTableColumn
triaxPerceivedSeverity = _TriaxPerceivedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 4),
    _TriaxPerceivedSeverity_Type()
)
triaxPerceivedSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxPerceivedSeverity.setStatus("mandatory")
_TriaxEventTime_Type = DisplayString
_TriaxEventTime_Object = MibTableColumn
triaxEventTime = _TriaxEventTime_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 5),
    _TriaxEventTime_Type()
)
triaxEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxEventTime.setStatus("mandatory")
_TriaxEventType_Type = TriaxEventCategoryType
_TriaxEventType_Object = MibTableColumn
triaxEventType = _TriaxEventType_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 6),
    _TriaxEventType_Type()
)
triaxEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxEventType.setStatus("mandatory")
_TriaxProbableCause_Type = TriaxEventProbableCause
_TriaxProbableCause_Object = MibTableColumn
triaxProbableCause = _TriaxProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 41359, 1, 2, 1, 1, 7),
    _TriaxProbableCause_Type()
)
triaxProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    triaxProbableCause.setStatus("current")

# Managed Objects groups


# Notification objects

triaxPowerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 1)
)
triaxPowerUpTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxPowerUpTrap.setStatus(
        "current"
    )

triaxLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 2)
)
triaxLoginTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxLoginTrap.setStatus(
        "current"
    )

triaxLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 3)
)
triaxLogoutTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxLogoutTrap.setStatus(
        "current"
    )

triaxTimeOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 4)
)
triaxTimeOutTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxTimeOutTrap.setStatus(
        "current"
    )

triaxFailedLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 5)
)
triaxFailedLoginTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxFailedLoginTrap.setStatus(
        "current"
    )

triaxRestartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 6)
)
triaxRestartTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxRestartTrap.setStatus(
        "current"
    )

triaxInputErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 7)
)
triaxInputErrorTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxInputErrorTrap.setStatus(
        "current"
    )

triaxCIInsertionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 8)
)
triaxCIInsertionTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCIInsertionTrap.setStatus(
        "current"
    )

triaxCIRemovalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 9)
)
triaxCIRemovalTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCIRemovalTrap.setStatus(
        "current"
    )

triaxModuleInsertionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 10)
)
triaxModuleInsertionTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxModuleInsertionTrap.setStatus(
        "current"
    )

triaxModuleRemovalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 11)
)
triaxModuleRemovalTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxModuleRemovalTrap.setStatus(
        "current"
    )

triaxCIDecramblingErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 12)
)
triaxCIDecramblingErrorTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCIDecramblingErrorTrap.setStatus(
        "current"
    )

triaxCICommunicationDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 13)
)
triaxCICommunicationDownTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCICommunicationDownTrap.setStatus(
        "current"
    )

triaxVideoDecodingFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 14)
)
triaxVideoDecodingFailureTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxVideoDecodingFailureTrap.setStatus(
        "current"
    )

triaxInterlinkDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 15)
)
triaxInterlinkDisconnectTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxInterlinkDisconnectTrap.setStatus(
        "current"
    )

triaxConfigurationChangeAppliedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 16)
)
triaxConfigurationChangeAppliedTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxConfigurationChangeAppliedTrap.setStatus(
        "current"
    )

triaxInputOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 17)
)
triaxInputOKTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxInputOKTrap.setStatus(
        "current"
    )

triaxCIDescramblingOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 18)
)
triaxCIDescramblingOKTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCIDescramblingOKTrap.setStatus(
        "current"
    )

triaxCICommunicationUPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 19)
)
triaxCICommunicationUPTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxCICommunicationUPTrap.setStatus(
        "current"
    )

triaxVideoDecodingOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 20)
)
triaxVideoDecodingOKTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxVideoDecodingOKTrap.setStatus(
        "current"
    )

triaxInterlinkConnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 21)
)
triaxInterlinkConnectTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxInterlinkConnectTrap.setStatus(
        "current"
    )

triaxPSUNoLongerWorksTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 22)
)
triaxPSUNoLongerWorksTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxPSUNoLongerWorksTrap.setStatus(
        "current"
    )

triaxSDCorruptionDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41359, 1, 0, 23)
)
triaxSDCorruptionDetectedTrap.setObjects(
      *(("TRIAX-EVENT-MIB", "triaxManagedObjectClass"),
        ("TRIAX-EVENT-MIB", "triaxManagedObjedctInstanceClass"),
        ("TRIAX-EVENT-MIB", "triaxSequenceNumber"),
        ("TRIAX-EVENT-MIB", "triaxPerceivedSeverity"),
        ("TRIAX-EVENT-MIB", "triaxEventTime"),
        ("TRIAX-EVENT-MIB", "triaxEventType"),
        ("TRIAX-EVENT-MIB", "triaxProbableCause"))
)
if mibBuilder.loadTexts:
    triaxSDCorruptionDetectedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIAX-EVENT-MIB",
    **{"DisplayString": DisplayString,
       "TriaxPerceivedEventSeverityType": TriaxPerceivedEventSeverityType,
       "TriaxEventCategoryType": TriaxEventCategoryType,
       "TriaxEventProbableCause": TriaxEventProbableCause,
       "org": org,
       "dod": dod,
       "internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "triax": triax,
       "he": he,
       "eventTraps": eventTraps,
       "triaxPowerUpTrap": triaxPowerUpTrap,
       "triaxLoginTrap": triaxLoginTrap,
       "triaxLogoutTrap": triaxLogoutTrap,
       "triaxTimeOutTrap": triaxTimeOutTrap,
       "triaxFailedLoginTrap": triaxFailedLoginTrap,
       "triaxRestartTrap": triaxRestartTrap,
       "triaxInputErrorTrap": triaxInputErrorTrap,
       "triaxCIInsertionTrap": triaxCIInsertionTrap,
       "triaxCIRemovalTrap": triaxCIRemovalTrap,
       "triaxModuleInsertionTrap": triaxModuleInsertionTrap,
       "triaxModuleRemovalTrap": triaxModuleRemovalTrap,
       "triaxCIDecramblingErrorTrap": triaxCIDecramblingErrorTrap,
       "triaxCICommunicationDownTrap": triaxCICommunicationDownTrap,
       "triaxVideoDecodingFailureTrap": triaxVideoDecodingFailureTrap,
       "triaxInterlinkDisconnectTrap": triaxInterlinkDisconnectTrap,
       "triaxConfigurationChangeAppliedTrap": triaxConfigurationChangeAppliedTrap,
       "triaxInputOKTrap": triaxInputOKTrap,
       "triaxCIDescramblingOKTrap": triaxCIDescramblingOKTrap,
       "triaxCICommunicationUPTrap": triaxCICommunicationUPTrap,
       "triaxVideoDecodingOKTrap": triaxVideoDecodingOKTrap,
       "triaxInterlinkConnectTrap": triaxInterlinkConnectTrap,
       "triaxPSUNoLongerWorksTrap": triaxPSUNoLongerWorksTrap,
       "triaxSDCorruptionDetectedTrap": triaxSDCorruptionDetectedTrap,
       "eventMIB": eventMIB,
       "currentEventTable": currentEventTable,
       "currentEventEntry": currentEventEntry,
       "triaxManagedObjectClass": triaxManagedObjectClass,
       "triaxManagedObjedctInstanceClass": triaxManagedObjedctInstanceClass,
       "triaxSequenceNumber": triaxSequenceNumber,
       "triaxPerceivedSeverity": triaxPerceivedSeverity,
       "triaxEventTime": triaxEventTime,
       "triaxEventType": triaxEventType,
       "triaxProbableCause": triaxProbableCause}
)
