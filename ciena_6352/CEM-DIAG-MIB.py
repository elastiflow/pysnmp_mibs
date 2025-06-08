# SNMP MIB module (CEM-DIAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-DIAG-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(Cn1000HWInstalledCardType,) = mibBuilder.importSymbols(
    "CEM-CN1000-HARDWARE",
    "Cn1000HWInstalledCardType")

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

cemDiagTestModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 22)
)
if mibBuilder.loadTexts:
    cemDiagTestModule.setRevisions(
        ("2003-10-17 16:48",
         "2002-04-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CemDiagnosticTestResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diagnosticTestPassed", 1),
          ("diagnosticTestFailed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CemDiagTestMIB_ObjectIdentity = ObjectIdentity
cemDiagTestMIB = _CemDiagTestMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1)
)
if mibBuilder.loadTexts:
    cemDiagTestMIB.setStatus("obsolete")
_CemDiagTestStatsTable_Object = MibTable
cemDiagTestStatsTable = _CemDiagTestStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1)
)
if mibBuilder.loadTexts:
    cemDiagTestStatsTable.setStatus("obsolete")
_CemDiagTestStatsEntry_Object = MibTableRow
cemDiagTestStatsEntry = _CemDiagTestStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1)
)
cemDiagTestStatsEntry.setIndexNames(
    (0, "CEM-DIAG-MIB", "cemDiagTestIndex"),
    (0, "CEM-DIAG-MIB", "cemDiagTestCardIndex"),
)
if mibBuilder.loadTexts:
    cemDiagTestStatsEntry.setStatus("obsolete")
_CemDiagTestCardIndex_Type = PhysicalIndex
_CemDiagTestCardIndex_Object = MibTableColumn
cemDiagTestCardIndex = _CemDiagTestCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 1),
    _CemDiagTestCardIndex_Type()
)
cemDiagTestCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemDiagTestCardIndex.setStatus("obsolete")


class _CemDiagTestIndex_Type(Integer32):
    """Custom type cemDiagTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_CemDiagTestIndex_Type.__name__ = "Integer32"
_CemDiagTestIndex_Object = MibTableColumn
cemDiagTestIndex = _CemDiagTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 2),
    _CemDiagTestIndex_Type()
)
cemDiagTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemDiagTestIndex.setStatus("obsolete")
_CemDiagTestShelf_Type = Integer32
_CemDiagTestShelf_Object = MibTableColumn
cemDiagTestShelf = _CemDiagTestShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 3),
    _CemDiagTestShelf_Type()
)
cemDiagTestShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestShelf.setStatus("obsolete")
_CemDiagTestSlot_Type = Integer32
_CemDiagTestSlot_Object = MibTableColumn
cemDiagTestSlot = _CemDiagTestSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 4),
    _CemDiagTestSlot_Type()
)
cemDiagTestSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestSlot.setStatus("obsolete")
_CemDiagTestCardType_Type = Cn1000HWInstalledCardType
_CemDiagTestCardType_Object = MibTableColumn
cemDiagTestCardType = _CemDiagTestCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 5),
    _CemDiagTestCardType_Type()
)
cemDiagTestCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestCardType.setStatus("obsolete")
_CemDiagTestResult_Type = CemDiagnosticTestResult
_CemDiagTestResult_Object = MibTableColumn
cemDiagTestResult = _CemDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 1, 1, 6),
    _CemDiagTestResult_Type()
)
cemDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestResult.setStatus("obsolete")
_CemDiagTotalTestsStatsCardTable_Object = MibTable
cemDiagTotalTestsStatsCardTable = _CemDiagTotalTestsStatsCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2)
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsCardTable.setStatus("obsolete")
_CemDiagTotalTestsStatsCardEntry_Object = MibTableRow
cemDiagTotalTestsStatsCardEntry = _CemDiagTotalTestsStatsCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1)
)
cemDiagTotalTestsStatsCardEntry.setIndexNames(
    (0, "CEM-DIAG-MIB", "cemDiagTestCardIndex"),
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsCardEntry.setStatus("obsolete")
_CemDiagTotalTestsCardShelf_Type = Integer32
_CemDiagTotalTestsCardShelf_Object = MibTableColumn
cemDiagTotalTestsCardShelf = _CemDiagTotalTestsCardShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 1),
    _CemDiagTotalTestsCardShelf_Type()
)
cemDiagTotalTestsCardShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardShelf.setStatus("obsolete")
_CemDiagTotalTestsCardSlot_Type = Integer32
_CemDiagTotalTestsCardSlot_Object = MibTableColumn
cemDiagTotalTestsCardSlot = _CemDiagTotalTestsCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 2),
    _CemDiagTotalTestsCardSlot_Type()
)
cemDiagTotalTestsCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardSlot.setStatus("obsolete")
_CemDiagTotalTestsCardType_Type = Cn1000HWInstalledCardType
_CemDiagTotalTestsCardType_Object = MibTableColumn
cemDiagTotalTestsCardType = _CemDiagTotalTestsCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 3),
    _CemDiagTotalTestsCardType_Type()
)
cemDiagTotalTestsCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardType.setStatus("obsolete")
_CemDiagTotalTestsCardRan_Type = Integer32
_CemDiagTotalTestsCardRan_Object = MibTableColumn
cemDiagTotalTestsCardRan = _CemDiagTotalTestsCardRan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 4),
    _CemDiagTotalTestsCardRan_Type()
)
cemDiagTotalTestsCardRan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardRan.setStatus("obsolete")
_CemDiagTotalTestsCardPassed_Type = Integer32
_CemDiagTotalTestsCardPassed_Object = MibTableColumn
cemDiagTotalTestsCardPassed = _CemDiagTotalTestsCardPassed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 5),
    _CemDiagTotalTestsCardPassed_Type()
)
cemDiagTotalTestsCardPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardPassed.setStatus("obsolete")
_CemDiagTotalTestsCardFailed_Type = Integer32
_CemDiagTotalTestsCardFailed_Object = MibTableColumn
cemDiagTotalTestsCardFailed = _CemDiagTotalTestsCardFailed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 6),
    _CemDiagTotalTestsCardFailed_Type()
)
cemDiagTotalTestsCardFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsCardFailed.setStatus("obsolete")
_CemDiagTestStatsLastRunTime_Type = Integer32
_CemDiagTestStatsLastRunTime_Object = MibTableColumn
cemDiagTestStatsLastRunTime = _CemDiagTestStatsLastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 7),
    _CemDiagTestStatsLastRunTime_Type()
)
cemDiagTestStatsLastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestStatsLastRunTime.setStatus("obsolete")


class _CemDiagTotalTestsStatsTestType_Type(Integer32):
    """Custom type cemDiagTotalTestsStatsTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inServiceDiagnostic", 1),
          ("outOfServiceDiagnostic", 2),
          ("none", 3))
    )


_CemDiagTotalTestsStatsTestType_Type.__name__ = "Integer32"
_CemDiagTotalTestsStatsTestType_Object = MibTableColumn
cemDiagTotalTestsStatsTestType = _CemDiagTotalTestsStatsTestType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 2, 1, 8),
    _CemDiagTotalTestsStatsTestType_Type()
)
cemDiagTotalTestsStatsTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsTestType.setStatus("obsolete")
_CemDiagTotalTestsStatsSystemTable_Object = MibTable
cemDiagTotalTestsStatsSystemTable = _CemDiagTotalTestsStatsSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3)
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsSystemTable.setStatus("obsolete")
_CemDiagTotalTestsStatsSystemEntry_Object = MibTableRow
cemDiagTotalTestsStatsSystemEntry = _CemDiagTotalTestsStatsSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1)
)
cemDiagTotalTestsStatsSystemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsSystemEntry.setStatus("obsolete")
_CemDiagTotalTestsSystemShelf_Type = Integer32
_CemDiagTotalTestsSystemShelf_Object = MibTableColumn
cemDiagTotalTestsSystemShelf = _CemDiagTotalTestsSystemShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 1),
    _CemDiagTotalTestsSystemShelf_Type()
)
cemDiagTotalTestsSystemShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemShelf.setStatus("obsolete")
_CemDiagTotalTestsSystemSlot_Type = Integer32
_CemDiagTotalTestsSystemSlot_Object = MibTableColumn
cemDiagTotalTestsSystemSlot = _CemDiagTotalTestsSystemSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 2),
    _CemDiagTotalTestsSystemSlot_Type()
)
cemDiagTotalTestsSystemSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemSlot.setStatus("obsolete")
_CemDiagTotalTestsSystemCardType_Type = Cn1000HWInstalledCardType
_CemDiagTotalTestsSystemCardType_Object = MibTableColumn
cemDiagTotalTestsSystemCardType = _CemDiagTotalTestsSystemCardType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 3),
    _CemDiagTotalTestsSystemCardType_Type()
)
cemDiagTotalTestsSystemCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemCardType.setStatus("obsolete")
_CemDiagTotalTestsSystemRan_Type = Integer32
_CemDiagTotalTestsSystemRan_Object = MibTableColumn
cemDiagTotalTestsSystemRan = _CemDiagTotalTestsSystemRan_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 4),
    _CemDiagTotalTestsSystemRan_Type()
)
cemDiagTotalTestsSystemRan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemRan.setStatus("obsolete")
_CemDiagTotalTestsSystemPassed_Type = Integer32
_CemDiagTotalTestsSystemPassed_Object = MibTableColumn
cemDiagTotalTestsSystemPassed = _CemDiagTotalTestsSystemPassed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 5),
    _CemDiagTotalTestsSystemPassed_Type()
)
cemDiagTotalTestsSystemPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemPassed.setStatus("obsolete")
_CemDiagTotalTestsSystemFailed_Type = Integer32
_CemDiagTotalTestsSystemFailed_Object = MibTableColumn
cemDiagTotalTestsSystemFailed = _CemDiagTotalTestsSystemFailed_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 3, 1, 6),
    _CemDiagTotalTestsSystemFailed_Type()
)
cemDiagTotalTestsSystemFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTotalTestsSystemFailed.setStatus("obsolete")
_CemDiagTestExecutionTable_Object = MibTable
cemDiagTestExecutionTable = _CemDiagTestExecutionTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4)
)
if mibBuilder.loadTexts:
    cemDiagTestExecutionTable.setStatus("obsolete")
_CemDiagTestExecutionEntry_Object = MibTableRow
cemDiagTestExecutionEntry = _CemDiagTestExecutionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4, 1)
)
cemDiagTestExecutionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cemDiagTestExecutionEntry.setStatus("obsolete")
_CemDiagTestExecutionShelf_Type = Integer32
_CemDiagTestExecutionShelf_Object = MibTableColumn
cemDiagTestExecutionShelf = _CemDiagTestExecutionShelf_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4, 1, 1),
    _CemDiagTestExecutionShelf_Type()
)
cemDiagTestExecutionShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestExecutionShelf.setStatus("obsolete")
_CemDiagTestExecutionSlot_Type = Integer32
_CemDiagTestExecutionSlot_Object = MibTableColumn
cemDiagTestExecutionSlot = _CemDiagTestExecutionSlot_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4, 1, 2),
    _CemDiagTestExecutionSlot_Type()
)
cemDiagTestExecutionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestExecutionSlot.setStatus("obsolete")


class _CemDiagTestExecutionTrigger_Type(Integer32):
    """Custom type cemDiagTestExecutionTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inServiceDiagnostic", 1),
          ("outOfServiceDiagnostic", 2),
          ("none", 3))
    )


_CemDiagTestExecutionTrigger_Type.__name__ = "Integer32"
_CemDiagTestExecutionTrigger_Object = MibTableColumn
cemDiagTestExecutionTrigger = _CemDiagTestExecutionTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4, 1, 3),
    _CemDiagTestExecutionTrigger_Type()
)
cemDiagTestExecutionTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cemDiagTestExecutionTrigger.setStatus("obsolete")


class _CemDiagTestExecutionStatus_Type(Integer32):
    """Custom type cemDiagTestExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("idle", 2))
    )


_CemDiagTestExecutionStatus_Type.__name__ = "Integer32"
_CemDiagTestExecutionStatus_Object = MibTableColumn
cemDiagTestExecutionStatus = _CemDiagTestExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 4, 1, 4),
    _CemDiagTestExecutionStatus_Type()
)
cemDiagTestExecutionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemDiagTestExecutionStatus.setStatus("obsolete")
_CemDiagTestGroups_ObjectIdentity = ObjectIdentity
cemDiagTestGroups = _CemDiagTestGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 5)
)
if mibBuilder.loadTexts:
    cemDiagTestGroups.setStatus("current")
_CemDiagTestsConformance_ObjectIdentity = ObjectIdentity
cemDiagTestsConformance = _CemDiagTestsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 6)
)
if mibBuilder.loadTexts:
    cemDiagTestsConformance.setStatus("current")

# Managed Objects groups

cemDiagTestStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 5, 1)
)
cemDiagTestStatsGroup.setObjects(
      *(("CEM-DIAG-MIB", "cemDiagTestResult"),
        ("CEM-DIAG-MIB", "cemDiagTestCardType"),
        ("CEM-DIAG-MIB", "cemDiagTestSlot"),
        ("CEM-DIAG-MIB", "cemDiagTestShelf"))
)
if mibBuilder.loadTexts:
    cemDiagTestStatsGroup.setStatus("obsolete")

cemDiagTotalTestsStatsCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 5, 2)
)
cemDiagTotalTestsStatsCardGroup.setObjects(
      *(("CEM-DIAG-MIB", "cemDiagTotalTestsCardShelf"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsCardSlot"),
        ("CEM-DIAG-MIB", "cemDiagTestStatsLastRunTime"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsStatsTestType"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsCardRan"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsCardType"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsCardPassed"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsCardFailed"))
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsCardGroup.setStatus("obsolete")

cemDiagTotalTestsStatsSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 5, 3)
)
cemDiagTotalTestsStatsSystemGroup.setObjects(
      *(("CEM-DIAG-MIB", "cemDiagTotalTestsSystemShelf"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsSystemSlot"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsSystemCardType"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsSystemRan"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsSystemPassed"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsSystemFailed"))
)
if mibBuilder.loadTexts:
    cemDiagTotalTestsStatsSystemGroup.setStatus("obsolete")

cemDiagTestExecutionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 5, 4)
)
cemDiagTestExecutionGroup.setObjects(
      *(("CEM-DIAG-MIB", "cemDiagTestExecutionShelf"),
        ("CEM-DIAG-MIB", "cemDiagTestExecutionSlot"),
        ("CEM-DIAG-MIB", "cemDiagTestExecutionTrigger"),
        ("CEM-DIAG-MIB", "cemDiagTestExecutionStatus"))
)
if mibBuilder.loadTexts:
    cemDiagTestExecutionGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cemDiagTestsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 22, 1, 6, 1)
)
cemDiagTestsCompliance.setObjects(
      *(("CEM-DIAG-MIB", "cemDiagTestStatsGroup"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsStatsCardGroup"),
        ("CEM-DIAG-MIB", "cemDiagTotalTestsStatsSystemGroup"),
        ("CEM-DIAG-MIB", "cemDiagTestExecutionGroup"))
)
if mibBuilder.loadTexts:
    cemDiagTestsCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-DIAG-MIB",
    **{"CemDiagnosticTestResult": CemDiagnosticTestResult,
       "cemDiagTestModule": cemDiagTestModule,
       "cemDiagTestMIB": cemDiagTestMIB,
       "cemDiagTestStatsTable": cemDiagTestStatsTable,
       "cemDiagTestStatsEntry": cemDiagTestStatsEntry,
       "cemDiagTestCardIndex": cemDiagTestCardIndex,
       "cemDiagTestIndex": cemDiagTestIndex,
       "cemDiagTestShelf": cemDiagTestShelf,
       "cemDiagTestSlot": cemDiagTestSlot,
       "cemDiagTestCardType": cemDiagTestCardType,
       "cemDiagTestResult": cemDiagTestResult,
       "cemDiagTotalTestsStatsCardTable": cemDiagTotalTestsStatsCardTable,
       "cemDiagTotalTestsStatsCardEntry": cemDiagTotalTestsStatsCardEntry,
       "cemDiagTotalTestsCardShelf": cemDiagTotalTestsCardShelf,
       "cemDiagTotalTestsCardSlot": cemDiagTotalTestsCardSlot,
       "cemDiagTotalTestsCardType": cemDiagTotalTestsCardType,
       "cemDiagTotalTestsCardRan": cemDiagTotalTestsCardRan,
       "cemDiagTotalTestsCardPassed": cemDiagTotalTestsCardPassed,
       "cemDiagTotalTestsCardFailed": cemDiagTotalTestsCardFailed,
       "cemDiagTestStatsLastRunTime": cemDiagTestStatsLastRunTime,
       "cemDiagTotalTestsStatsTestType": cemDiagTotalTestsStatsTestType,
       "cemDiagTotalTestsStatsSystemTable": cemDiagTotalTestsStatsSystemTable,
       "cemDiagTotalTestsStatsSystemEntry": cemDiagTotalTestsStatsSystemEntry,
       "cemDiagTotalTestsSystemShelf": cemDiagTotalTestsSystemShelf,
       "cemDiagTotalTestsSystemSlot": cemDiagTotalTestsSystemSlot,
       "cemDiagTotalTestsSystemCardType": cemDiagTotalTestsSystemCardType,
       "cemDiagTotalTestsSystemRan": cemDiagTotalTestsSystemRan,
       "cemDiagTotalTestsSystemPassed": cemDiagTotalTestsSystemPassed,
       "cemDiagTotalTestsSystemFailed": cemDiagTotalTestsSystemFailed,
       "cemDiagTestExecutionTable": cemDiagTestExecutionTable,
       "cemDiagTestExecutionEntry": cemDiagTestExecutionEntry,
       "cemDiagTestExecutionShelf": cemDiagTestExecutionShelf,
       "cemDiagTestExecutionSlot": cemDiagTestExecutionSlot,
       "cemDiagTestExecutionTrigger": cemDiagTestExecutionTrigger,
       "cemDiagTestExecutionStatus": cemDiagTestExecutionStatus,
       "cemDiagTestGroups": cemDiagTestGroups,
       "cemDiagTestStatsGroup": cemDiagTestStatsGroup,
       "cemDiagTotalTestsStatsCardGroup": cemDiagTotalTestsStatsCardGroup,
       "cemDiagTotalTestsStatsSystemGroup": cemDiagTotalTestsStatsSystemGroup,
       "cemDiagTestExecutionGroup": cemDiagTestExecutionGroup,
       "cemDiagTestsConformance": cemDiagTestsConformance,
       "cemDiagTestsCompliance": cemDiagTestsCompliance}
)
