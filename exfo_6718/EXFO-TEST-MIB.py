# SNMP MIB module (EXFO-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/exfo_6718/EXFO-TEST-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 22:54:13 2025
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

(eventManagedObjectInstance,
 eventTime) = mibBuilder.importSymbols(
    "EXFO-EVENT-MIB",
    "eventManagedObjectInstance",
    "eventTime")

(exfoCommonMib,
 exfoModules) = mibBuilder.importSymbols(
    "EXFO-SMI-REG",
    "exfoCommonMib",
    "exfoModules")

(ExfoSnmpType,) = mibBuilder.importSymbols(
    "EXFO-TC",
    "ExfoSnmpType")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

exfoTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 1, 1, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TestOutcome(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inconclusive", 0),
          ("pass", 1),
          ("fail", 2),
          ("timedOut", 3),
          ("prematureTermination", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Test_ObjectIdentity = ObjectIdentity
test = _Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4)
)
if mibBuilder.loadTexts:
    test.setStatus("current")
_TestConf_ObjectIdentity = ObjectIdentity
testConf = _TestConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1)
)
if mibBuilder.loadTexts:
    testConf.setStatus("current")
_TestGroups_ObjectIdentity = ObjectIdentity
testGroups = _TestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    testGroups.setStatus("current")
_TestCompls_ObjectIdentity = ObjectIdentity
testCompls = _TestCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    testCompls.setStatus("current")
_TestObjs_ObjectIdentity = ObjectIdentity
testObjs = _TestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2)
)
if mibBuilder.loadTexts:
    testObjs.setStatus("current")
_UncontrolledTestObjs_ObjectIdentity = ObjectIdentity
uncontrolledTestObjs = _UncontrolledTestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    uncontrolledTestObjs.setStatus("current")


class _UncontrolledTestNextIndex_Type(Unsigned32):
    """Custom type uncontrolledTestNextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UncontrolledTestNextIndex_Type.__name__ = "Unsigned32"
_UncontrolledTestNextIndex_Object = MibScalar
uncontrolledTestNextIndex = _UncontrolledTestNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 1),
    _UncontrolledTestNextIndex_Type()
)
uncontrolledTestNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestNextIndex.setStatus("current")
_UncontrolledTestTable_Object = MibTable
uncontrolledTestTable = _UncontrolledTestTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    uncontrolledTestTable.setStatus("current")
_UncontrolledTestEntry_Object = MibTableRow
uncontrolledTestEntry = _UncontrolledTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1)
)
uncontrolledTestEntry.setIndexNames(
    (0, "EXFO-TEST-MIB", "uncontrolledTestIndex"),
)
if mibBuilder.loadTexts:
    uncontrolledTestEntry.setStatus("current")


class _UncontrolledTestIndex_Type(Unsigned32):
    """Custom type uncontrolledTestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UncontrolledTestIndex_Type.__name__ = "Unsigned32"
_UncontrolledTestIndex_Object = MibTableColumn
uncontrolledTestIndex = _UncontrolledTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 1),
    _UncontrolledTestIndex_Type()
)
uncontrolledTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uncontrolledTestIndex.setStatus("current")
_UncontrolledTestRowStatus_Type = RowStatus
_UncontrolledTestRowStatus_Object = MibTableColumn
uncontrolledTestRowStatus = _UncontrolledTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 2),
    _UncontrolledTestRowStatus_Type()
)
uncontrolledTestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestRowStatus.setStatus("current")
_UncontrolledTestSessionIdlocal_Type = Unsigned32
_UncontrolledTestSessionIdlocal_Object = MibTableColumn
uncontrolledTestSessionIdlocal = _UncontrolledTestSessionIdlocal_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 3),
    _UncontrolledTestSessionIdlocal_Type()
)
uncontrolledTestSessionIdlocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestSessionIdlocal.setStatus("current")
_UncontrolledTestCategoryInformation_Type = AutonomousType
_UncontrolledTestCategoryInformation_Object = MibTableColumn
uncontrolledTestCategoryInformation = _UncontrolledTestCategoryInformation_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 4),
    _UncontrolledTestCategoryInformation_Type()
)
uncontrolledTestCategoryInformation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestCategoryInformation.setStatus("current")


class _UncontrolledTestTimeoutPeriodType_Type(Integer32):
    """Custom type uncontrolledTestTimeoutPeriodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("forever", 22),
          ("hours", 23),
          ("minutes", 24),
          ("seconds", 25),
          ("millisecs", 26),
          ("microsecs", 27),
          ("nanosecs", 28))
    )


_UncontrolledTestTimeoutPeriodType_Type.__name__ = "Integer32"
_UncontrolledTestTimeoutPeriodType_Object = MibTableColumn
uncontrolledTestTimeoutPeriodType = _UncontrolledTestTimeoutPeriodType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 5),
    _UncontrolledTestTimeoutPeriodType_Type()
)
uncontrolledTestTimeoutPeriodType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestTimeoutPeriodType.setStatus("current")
_UncontrolledTestTimeoutPeriodValue_Type = Integer32
_UncontrolledTestTimeoutPeriodValue_Object = MibTableColumn
uncontrolledTestTimeoutPeriodValue = _UncontrolledTestTimeoutPeriodValue_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 6),
    _UncontrolledTestTimeoutPeriodValue_Type()
)
uncontrolledTestTimeoutPeriodValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestTimeoutPeriodValue.setStatus("current")
_UncontrolledTestOutcome_Type = TestOutcome
_UncontrolledTestOutcome_Object = MibTableColumn
uncontrolledTestOutcome = _UncontrolledTestOutcome_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 7),
    _UncontrolledTestOutcome_Type()
)
uncontrolledTestOutcome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestOutcome.setStatus("current")
_UncontrolledTestProposedRepairAction_Type = DisplayString
_UncontrolledTestProposedRepairAction_Object = MibTableColumn
uncontrolledTestProposedRepairAction = _UncontrolledTestProposedRepairAction_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 8),
    _UncontrolledTestProposedRepairAction_Type()
)
uncontrolledTestProposedRepairAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestProposedRepairAction.setStatus("current")
_UncontrolledTestProposedAdditionalText_Type = DisplayString
_UncontrolledTestProposedAdditionalText_Object = MibTableColumn
uncontrolledTestProposedAdditionalText = _UncontrolledTestProposedAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 2, 1, 9),
    _UncontrolledTestProposedAdditionalText_Type()
)
uncontrolledTestProposedAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestProposedAdditionalText.setStatus("current")
_UncontrolledTestMortsTable_Object = MibTable
uncontrolledTestMortsTable = _UncontrolledTestMortsTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    uncontrolledTestMortsTable.setStatus("current")
_UncontrolledTestMortsEntry_Object = MibTableRow
uncontrolledTestMortsEntry = _UncontrolledTestMortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 3, 1)
)
uncontrolledTestMortsEntry.setIndexNames(
    (0, "EXFO-TEST-MIB", "uncontrolledTestIndex"),
    (0, "EXFO-TEST-MIB", "uncontrolledTestMortsIndex"),
)
if mibBuilder.loadTexts:
    uncontrolledTestMortsEntry.setStatus("current")
_UncontrolledTestMortsIndex_Type = Unsigned32
_UncontrolledTestMortsIndex_Object = MibTableColumn
uncontrolledTestMortsIndex = _UncontrolledTestMortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 3, 1, 1),
    _UncontrolledTestMortsIndex_Type()
)
uncontrolledTestMortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uncontrolledTestMortsIndex.setStatus("current")
_UncontrolledTestMortsReference_Type = VariablePointer
_UncontrolledTestMortsReference_Object = MibTableColumn
uncontrolledTestMortsReference = _UncontrolledTestMortsReference_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 3, 1, 2),
    _UncontrolledTestMortsReference_Type()
)
uncontrolledTestMortsReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uncontrolledTestMortsReference.setStatus("current")
_UncontrolledTestAddInformTable_Object = MibTable
uncontrolledTestAddInformTable = _UncontrolledTestAddInformTable_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    uncontrolledTestAddInformTable.setStatus("current")
_UncontrolledTestAddInformEntry_Object = MibTableRow
uncontrolledTestAddInformEntry = _UncontrolledTestAddInformEntry_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1)
)
uncontrolledTestAddInformEntry.setIndexNames(
    (0, "EXFO-TEST-MIB", "uncontrolledTestIndex"),
    (0, "EXFO-TEST-MIB", "uncontrolledTestAddInformIndex"),
)
if mibBuilder.loadTexts:
    uncontrolledTestAddInformEntry.setStatus("current")
_UncontrolledTestAddInformIndex_Type = Unsigned32
_UncontrolledTestAddInformIndex_Object = MibTableColumn
uncontrolledTestAddInformIndex = _UncontrolledTestAddInformIndex_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 1),
    _UncontrolledTestAddInformIndex_Type()
)
uncontrolledTestAddInformIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformIndex.setStatus("current")
_UncontrolledTestAddInformIdentifier_Type = VariablePointer
_UncontrolledTestAddInformIdentifier_Object = MibTableColumn
uncontrolledTestAddInformIdentifier = _UncontrolledTestAddInformIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 2),
    _UncontrolledTestAddInformIdentifier_Type()
)
uncontrolledTestAddInformIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformIdentifier.setStatus("current")
_UncontrolledTestAddInformSignificance_Type = TruthValue
_UncontrolledTestAddInformSignificance_Object = MibTableColumn
uncontrolledTestAddInformSignificance = _UncontrolledTestAddInformSignificance_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 3),
    _UncontrolledTestAddInformSignificance_Type()
)
uncontrolledTestAddInformSignificance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformSignificance.setStatus("current")
_UncontrolledTestAddInformValueType_Type = ExfoSnmpType
_UncontrolledTestAddInformValueType_Object = MibTableColumn
uncontrolledTestAddInformValueType = _UncontrolledTestAddInformValueType_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 4),
    _UncontrolledTestAddInformValueType_Type()
)
uncontrolledTestAddInformValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformValueType.setStatus("current")
_UncontrolledTestAddInformValueInteger_Type = Integer32
_UncontrolledTestAddInformValueInteger_Object = MibTableColumn
uncontrolledTestAddInformValueInteger = _UncontrolledTestAddInformValueInteger_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 5),
    _UncontrolledTestAddInformValueInteger_Type()
)
uncontrolledTestAddInformValueInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformValueInteger.setStatus("current")


class _UncontrolledTestAddInformValueString_Type(OctetString):
    """Custom type uncontrolledTestAddInformValueString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UncontrolledTestAddInformValueString_Type.__name__ = "OctetString"
_UncontrolledTestAddInformValueString_Object = MibTableColumn
uncontrolledTestAddInformValueString = _UncontrolledTestAddInformValueString_Object(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 2, 1, 4, 1, 6),
    _UncontrolledTestAddInformValueString_Type()
)
uncontrolledTestAddInformValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncontrolledTestAddInformValueString.setStatus("current")
_TestEvents_ObjectIdentity = ObjectIdentity
testEvents = _TestEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 3)
)
if mibBuilder.loadTexts:
    testEvents.setStatus("current")

# Managed Objects groups

uncontrolledTestRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 1, 1)
)
uncontrolledTestRequestGroup.setObjects(
      *(("EXFO-TEST-MIB", "uncontrolledTestRowStatus"),
        ("EXFO-TEST-MIB", "uncontrolledTestSessionIdlocal"),
        ("EXFO-TEST-MIB", "uncontrolledTestCategoryInformation"),
        ("EXFO-TEST-MIB", "uncontrolledTestTimeoutPeriodType"),
        ("EXFO-TEST-MIB", "uncontrolledTestTimeoutPeriodValue"))
)
if mibBuilder.loadTexts:
    uncontrolledTestRequestGroup.setStatus("current")

uncontrolledTestResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 1, 2)
)
uncontrolledTestResultGroup.setObjects(
      *(("EXFO-TEST-MIB", "uncontrolledTestOutcome"),
        ("EXFO-TEST-MIB", "uncontrolledTestProposedRepairAction"),
        ("EXFO-TEST-MIB", "uncontrolledTestProposedAdditionalText"),
        ("EXFO-TEST-MIB", "uncontrolledTestMortsReference"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformIdentifier"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformSignificance"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueType"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueInteger"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueString"))
)
if mibBuilder.loadTexts:
    uncontrolledTestResultGroup.setStatus("current")


# Notification objects

uncontrolledTestResult = NotificationType(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 3, 1)
)
uncontrolledTestResult.setObjects(
      *(("EXFO-EVENT-MIB", "eventManagedObjectInstance"),
        ("EXFO-EVENT-MIB", "eventTime"),
        ("EXFO-TEST-MIB", "uncontrolledTestSessionIdlocal"),
        ("EXFO-TEST-MIB", "uncontrolledTestCategoryInformation"),
        ("EXFO-TEST-MIB", "uncontrolledTestTimeoutPeriodType"),
        ("EXFO-TEST-MIB", "uncontrolledTestTimeoutPeriodValue"),
        ("EXFO-TEST-MIB", "uncontrolledTestOutcome"),
        ("EXFO-TEST-MIB", "uncontrolledTestProposedRepairAction"),
        ("EXFO-TEST-MIB", "uncontrolledTestProposedAdditionalText"),
        ("EXFO-TEST-MIB", "uncontrolledTestMortsReference"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformIdentifier"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformSignificance"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueType"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueInteger"),
        ("EXFO-TEST-MIB", "uncontrolledTestAddInformValueString"))
)
if mibBuilder.loadTexts:
    uncontrolledTestResult.setStatus(
        "current"
    )


# Notifications groups

uncontrolledTestNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 1, 3)
)
uncontrolledTestNotificationGroup.setObjects(
    ("EXFO-TEST-MIB", "uncontrolledTestResult")
)
if mibBuilder.loadTexts:
    uncontrolledTestNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

testAdvancedCompls = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6718, 2, 4, 1, 2, 1)
)
testAdvancedCompls.setObjects(
      *(("EXFO-TEST-MIB", "uncontrolledTestRequestGroup"),
        ("EXFO-TEST-MIB", "uncontrolledTestResultGroup"),
        ("EXFO-TEST-MIB", "uncontrolledTestNotificationGroup"))
)
if mibBuilder.loadTexts:
    testAdvancedCompls.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXFO-TEST-MIB",
    **{"TestOutcome": TestOutcome,
       "exfoTestMib": exfoTestMib,
       "test": test,
       "testConf": testConf,
       "testGroups": testGroups,
       "uncontrolledTestRequestGroup": uncontrolledTestRequestGroup,
       "uncontrolledTestResultGroup": uncontrolledTestResultGroup,
       "uncontrolledTestNotificationGroup": uncontrolledTestNotificationGroup,
       "testCompls": testCompls,
       "testAdvancedCompls": testAdvancedCompls,
       "testObjs": testObjs,
       "uncontrolledTestObjs": uncontrolledTestObjs,
       "uncontrolledTestNextIndex": uncontrolledTestNextIndex,
       "uncontrolledTestTable": uncontrolledTestTable,
       "uncontrolledTestEntry": uncontrolledTestEntry,
       "uncontrolledTestIndex": uncontrolledTestIndex,
       "uncontrolledTestRowStatus": uncontrolledTestRowStatus,
       "uncontrolledTestSessionIdlocal": uncontrolledTestSessionIdlocal,
       "uncontrolledTestCategoryInformation": uncontrolledTestCategoryInformation,
       "uncontrolledTestTimeoutPeriodType": uncontrolledTestTimeoutPeriodType,
       "uncontrolledTestTimeoutPeriodValue": uncontrolledTestTimeoutPeriodValue,
       "uncontrolledTestOutcome": uncontrolledTestOutcome,
       "uncontrolledTestProposedRepairAction": uncontrolledTestProposedRepairAction,
       "uncontrolledTestProposedAdditionalText": uncontrolledTestProposedAdditionalText,
       "uncontrolledTestMortsTable": uncontrolledTestMortsTable,
       "uncontrolledTestMortsEntry": uncontrolledTestMortsEntry,
       "uncontrolledTestMortsIndex": uncontrolledTestMortsIndex,
       "uncontrolledTestMortsReference": uncontrolledTestMortsReference,
       "uncontrolledTestAddInformTable": uncontrolledTestAddInformTable,
       "uncontrolledTestAddInformEntry": uncontrolledTestAddInformEntry,
       "uncontrolledTestAddInformIndex": uncontrolledTestAddInformIndex,
       "uncontrolledTestAddInformIdentifier": uncontrolledTestAddInformIdentifier,
       "uncontrolledTestAddInformSignificance": uncontrolledTestAddInformSignificance,
       "uncontrolledTestAddInformValueType": uncontrolledTestAddInformValueType,
       "uncontrolledTestAddInformValueInteger": uncontrolledTestAddInformValueInteger,
       "uncontrolledTestAddInformValueString": uncontrolledTestAddInformValueString,
       "testEvents": testEvents,
       "uncontrolledTestResult": uncontrolledTestResult}
)
