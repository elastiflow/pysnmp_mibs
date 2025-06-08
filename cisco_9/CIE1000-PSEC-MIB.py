# SNMP MIB module (CIE1000-PSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-PSEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:42 2025
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

(CIE1000DisplayString,
 CIE1000InterfaceIndex,
 CIE1000Unsigned16) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString",
    "CIE1000InterfaceIndex",
    "CIE1000Unsigned16")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000PsecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66)
)
if mibBuilder.loadTexts:
    cie1000PsecMib.setRevisions(
        ("2016-06-02 00:00",
         "2014-12-10 00:00",
         "2014-12-08 00:00",
         "2014-10-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000PsecLimitActionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trap", 1),
          ("shutdown", 2),
          ("trapShutdown", 3))
    )



class CIE1000PsecStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 0),
          ("blocked", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000PsecMibObjects_ObjectIdentity = ObjectIdentity
cie1000PsecMibObjects = _Cie1000PsecMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1)
)
_Cie1000PsecConfig_ObjectIdentity = ObjectIdentity
cie1000PsecConfig = _Cie1000PsecConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2)
)
_Cie1000PsecConfigGlobals_ObjectIdentity = ObjectIdentity
cie1000PsecConfigGlobals = _Cie1000PsecConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 1)
)
_Cie1000PsecConfigGlobalsEnabled_Type = TruthValue
_Cie1000PsecConfigGlobalsEnabled_Object = MibScalar
cie1000PsecConfigGlobalsEnabled = _Cie1000PsecConfigGlobalsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 1, 1),
    _Cie1000PsecConfigGlobalsEnabled_Type()
)
cie1000PsecConfigGlobalsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigGlobalsEnabled.setStatus("current")
_Cie1000PsecConfigGlobalsEnableAging_Type = TruthValue
_Cie1000PsecConfigGlobalsEnableAging_Object = MibScalar
cie1000PsecConfigGlobalsEnableAging = _Cie1000PsecConfigGlobalsEnableAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 1, 2),
    _Cie1000PsecConfigGlobalsEnableAging_Type()
)
cie1000PsecConfigGlobalsEnableAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigGlobalsEnableAging.setStatus("current")
_Cie1000PsecConfigGlobalsAgingPeriodSecs_Type = Unsigned32
_Cie1000PsecConfigGlobalsAgingPeriodSecs_Object = MibScalar
cie1000PsecConfigGlobalsAgingPeriodSecs = _Cie1000PsecConfigGlobalsAgingPeriodSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 1, 3),
    _Cie1000PsecConfigGlobalsAgingPeriodSecs_Type()
)
cie1000PsecConfigGlobalsAgingPeriodSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigGlobalsAgingPeriodSecs.setStatus("current")
_Cie1000PsecConfigPortTable_Object = MibTable
cie1000PsecConfigPortTable = _Cie1000PsecConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cie1000PsecConfigPortTable.setStatus("current")
_Cie1000PsecConfigPortEntry_Object = MibTableRow
cie1000PsecConfigPortEntry = _Cie1000PsecConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2, 1)
)
cie1000PsecConfigPortEntry.setIndexNames(
    (0, "CIE1000-PSEC-MIB", "cie1000PsecConfigPortIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PsecConfigPortEntry.setStatus("current")
_Cie1000PsecConfigPortIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PsecConfigPortIfIndex_Object = MibTableColumn
cie1000PsecConfigPortIfIndex = _Cie1000PsecConfigPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2, 1, 1),
    _Cie1000PsecConfigPortIfIndex_Type()
)
cie1000PsecConfigPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PsecConfigPortIfIndex.setStatus("current")
_Cie1000PsecConfigPortEnabled_Type = TruthValue
_Cie1000PsecConfigPortEnabled_Object = MibTableColumn
cie1000PsecConfigPortEnabled = _Cie1000PsecConfigPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2, 1, 2),
    _Cie1000PsecConfigPortEnabled_Type()
)
cie1000PsecConfigPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigPortEnabled.setStatus("current")
_Cie1000PsecConfigPortLimit_Type = Unsigned32
_Cie1000PsecConfigPortLimit_Object = MibTableColumn
cie1000PsecConfigPortLimit = _Cie1000PsecConfigPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2, 1, 3),
    _Cie1000PsecConfigPortLimit_Type()
)
cie1000PsecConfigPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigPortLimit.setStatus("current")
_Cie1000PsecConfigPortAction_Type = CIE1000PsecLimitActionType
_Cie1000PsecConfigPortAction_Object = MibTableColumn
cie1000PsecConfigPortAction = _Cie1000PsecConfigPortAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 2, 2, 1, 4),
    _Cie1000PsecConfigPortAction_Type()
)
cie1000PsecConfigPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecConfigPortAction.setStatus("current")
_Cie1000PsecStatus_ObjectIdentity = ObjectIdentity
cie1000PsecStatus = _Cie1000PsecStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3)
)
_Cie1000PsecStatusPortTable_Object = MibTable
cie1000PsecStatusPortTable = _Cie1000PsecStatusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTable.setStatus("current")
_Cie1000PsecStatusPortEntry_Object = MibTableRow
cie1000PsecStatusPortEntry = _Cie1000PsecStatusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1)
)
cie1000PsecStatusPortEntry.setIndexNames(
    (0, "CIE1000-PSEC-MIB", "cie1000PsecStatusPortIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortEntry.setStatus("current")
_Cie1000PsecStatusPortIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PsecStatusPortIfIndex_Object = MibTableColumn
cie1000PsecStatusPortIfIndex = _Cie1000PsecStatusPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1, 1),
    _Cie1000PsecStatusPortIfIndex_Type()
)
cie1000PsecStatusPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortIfIndex.setStatus("current")
_Cie1000PsecStatusPortUsers_Type = Unsigned32
_Cie1000PsecStatusPortUsers_Object = MibTableColumn
cie1000PsecStatusPortUsers = _Cie1000PsecStatusPortUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1, 2),
    _Cie1000PsecStatusPortUsers_Type()
)
cie1000PsecStatusPortUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortUsers.setStatus("current")
_Cie1000PsecStatusPortLimitReached_Type = TruthValue
_Cie1000PsecStatusPortLimitReached_Object = MibTableColumn
cie1000PsecStatusPortLimitReached = _Cie1000PsecStatusPortLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1, 3),
    _Cie1000PsecStatusPortLimitReached_Type()
)
cie1000PsecStatusPortLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortLimitReached.setStatus("current")
_Cie1000PsecStatusPortShutdown_Type = TruthValue
_Cie1000PsecStatusPortShutdown_Object = MibTableColumn
cie1000PsecStatusPortShutdown = _Cie1000PsecStatusPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1, 4),
    _Cie1000PsecStatusPortShutdown_Type()
)
cie1000PsecStatusPortShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortShutdown.setStatus("current")
_Cie1000PsecStatusPortMacCount_Type = Unsigned32
_Cie1000PsecStatusPortMacCount_Object = MibTableColumn
cie1000PsecStatusPortMacCount = _Cie1000PsecStatusPortMacCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 1, 1, 5),
    _Cie1000PsecStatusPortMacCount_Type()
)
cie1000PsecStatusPortMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortMacCount.setStatus("current")
_Cie1000PsecStatusPortTrapsTable_Object = MibTable
cie1000PsecStatusPortTrapsTable = _Cie1000PsecStatusPortTrapsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsTable.setStatus("current")
_Cie1000PsecStatusPortTrapsEntry_Object = MibTableRow
cie1000PsecStatusPortTrapsEntry = _Cie1000PsecStatusPortTrapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1)
)
cie1000PsecStatusPortTrapsEntry.setIndexNames(
    (0, "CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsEntry.setStatus("current")
_Cie1000PsecStatusPortTrapsIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PsecStatusPortTrapsIfIndex_Object = MibTableColumn
cie1000PsecStatusPortTrapsIfIndex = _Cie1000PsecStatusPortTrapsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1, 1),
    _Cie1000PsecStatusPortTrapsIfIndex_Type()
)
cie1000PsecStatusPortTrapsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsIfIndex.setStatus("current")
_Cie1000PsecStatusPortTrapsUsers_Type = Unsigned32
_Cie1000PsecStatusPortTrapsUsers_Object = MibTableColumn
cie1000PsecStatusPortTrapsUsers = _Cie1000PsecStatusPortTrapsUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1, 2),
    _Cie1000PsecStatusPortTrapsUsers_Type()
)
cie1000PsecStatusPortTrapsUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsUsers.setStatus("current")
_Cie1000PsecStatusPortTrapsLimitReached_Type = TruthValue
_Cie1000PsecStatusPortTrapsLimitReached_Object = MibTableColumn
cie1000PsecStatusPortTrapsLimitReached = _Cie1000PsecStatusPortTrapsLimitReached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1, 3),
    _Cie1000PsecStatusPortTrapsLimitReached_Type()
)
cie1000PsecStatusPortTrapsLimitReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsLimitReached.setStatus("current")
_Cie1000PsecStatusPortTrapsShutdown_Type = TruthValue
_Cie1000PsecStatusPortTrapsShutdown_Object = MibTableColumn
cie1000PsecStatusPortTrapsShutdown = _Cie1000PsecStatusPortTrapsShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1, 4),
    _Cie1000PsecStatusPortTrapsShutdown_Type()
)
cie1000PsecStatusPortTrapsShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsShutdown.setStatus("current")
_Cie1000PsecStatusPortTrapsMacCount_Type = Unsigned32
_Cie1000PsecStatusPortTrapsMacCount_Object = MibTableColumn
cie1000PsecStatusPortTrapsMacCount = _Cie1000PsecStatusPortTrapsMacCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 3, 2, 1, 5),
    _Cie1000PsecStatusPortTrapsMacCount_Type()
)
cie1000PsecStatusPortTrapsMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsMacCount.setStatus("current")
_Cie1000PsecControl_ObjectIdentity = ObjectIdentity
cie1000PsecControl = _Cie1000PsecControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 4)
)
_Cie1000PsecControlPortReopenTable_Object = MibTable
cie1000PsecControlPortReopenTable = _Cie1000PsecControlPortReopenTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cie1000PsecControlPortReopenTable.setStatus("current")
_Cie1000PsecControlPortReopenEntry_Object = MibTableRow
cie1000PsecControlPortReopenEntry = _Cie1000PsecControlPortReopenEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 4, 1, 1)
)
cie1000PsecControlPortReopenEntry.setIndexNames(
    (0, "CIE1000-PSEC-MIB", "cie1000PsecControlPortReopenIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PsecControlPortReopenEntry.setStatus("current")
_Cie1000PsecControlPortReopenIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PsecControlPortReopenIfIndex_Object = MibTableColumn
cie1000PsecControlPortReopenIfIndex = _Cie1000PsecControlPortReopenIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 4, 1, 1, 1),
    _Cie1000PsecControlPortReopenIfIndex_Type()
)
cie1000PsecControlPortReopenIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PsecControlPortReopenIfIndex.setStatus("current")
_Cie1000PsecControlPortReopenPortReOpen_Type = TruthValue
_Cie1000PsecControlPortReopenPortReOpen_Object = MibTableColumn
cie1000PsecControlPortReopenPortReOpen = _Cie1000PsecControlPortReopenPortReOpen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 4, 1, 1, 2),
    _Cie1000PsecControlPortReopenPortReOpen_Type()
)
cie1000PsecControlPortReopenPortReOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000PsecControlPortReopenPortReOpen.setStatus("current")
_Cie1000PsecStatistics_ObjectIdentity = ObjectIdentity
cie1000PsecStatistics = _Cie1000PsecStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5)
)
_Cie1000PsecStatisticsPortTable_Object = MibTable
cie1000PsecStatisticsPortTable = _Cie1000PsecStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortTable.setStatus("current")
_Cie1000PsecStatisticsPortEntry_Object = MibTableRow
cie1000PsecStatisticsPortEntry = _Cie1000PsecStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1)
)
cie1000PsecStatisticsPortEntry.setIndexNames(
    (0, "CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortIfIndex"),
)
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortEntry.setStatus("current")
_Cie1000PsecStatisticsPortIfIndex_Type = CIE1000InterfaceIndex
_Cie1000PsecStatisticsPortIfIndex_Object = MibTableColumn
cie1000PsecStatisticsPortIfIndex = _Cie1000PsecStatisticsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 1),
    _Cie1000PsecStatisticsPortIfIndex_Type()
)
cie1000PsecStatisticsPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortIfIndex.setStatus("current")


class _Cie1000PsecStatisticsPortAgeOrHold_Type(CIE1000DisplayString):
    """Custom type cie1000PsecStatisticsPortAgeOrHold based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_Cie1000PsecStatisticsPortAgeOrHold_Type.__name__ = "CIE1000DisplayString"
_Cie1000PsecStatisticsPortAgeOrHold_Object = MibTableColumn
cie1000PsecStatisticsPortAgeOrHold = _Cie1000PsecStatisticsPortAgeOrHold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 5),
    _Cie1000PsecStatisticsPortAgeOrHold_Type()
)
cie1000PsecStatisticsPortAgeOrHold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortAgeOrHold.setStatus("current")


class _Cie1000PsecStatisticsPortCreationTime_Type(CIE1000DisplayString):
    """Custom type cie1000PsecStatisticsPortCreationTime based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Cie1000PsecStatisticsPortCreationTime_Type.__name__ = "CIE1000DisplayString"
_Cie1000PsecStatisticsPortCreationTime_Object = MibTableColumn
cie1000PsecStatisticsPortCreationTime = _Cie1000PsecStatisticsPortCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 6),
    _Cie1000PsecStatisticsPortCreationTime_Type()
)
cie1000PsecStatisticsPortCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortCreationTime.setStatus("current")
_Cie1000PsecStatisticsPortState_Type = CIE1000PsecStateType
_Cie1000PsecStatisticsPortState_Object = MibTableColumn
cie1000PsecStatisticsPortState = _Cie1000PsecStatisticsPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 7),
    _Cie1000PsecStatisticsPortState_Type()
)
cie1000PsecStatisticsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortState.setStatus("current")
_Cie1000PsecStatisticsPortMacId_Type = MacAddress
_Cie1000PsecStatisticsPortMacId_Object = MibTableColumn
cie1000PsecStatisticsPortMacId = _Cie1000PsecStatisticsPortMacId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 8),
    _Cie1000PsecStatisticsPortMacId_Type()
)
cie1000PsecStatisticsPortMacId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortMacId.setStatus("current")
_Cie1000PsecStatisticsPortVlanId_Type = CIE1000Unsigned16
_Cie1000PsecStatisticsPortVlanId_Object = MibTableColumn
cie1000PsecStatisticsPortVlanId = _Cie1000PsecStatisticsPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 5, 1, 1, 9),
    _Cie1000PsecStatisticsPortVlanId_Type()
)
cie1000PsecStatisticsPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortVlanId.setStatus("current")
_Cie1000PsecTrap_ObjectIdentity = ObjectIdentity
cie1000PsecTrap = _Cie1000PsecTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 6)
)
_Cie1000PsecMibConformance_ObjectIdentity = ObjectIdentity
cie1000PsecMibConformance = _Cie1000PsecMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2)
)
_Cie1000PsecMibCompliances_ObjectIdentity = ObjectIdentity
cie1000PsecMibCompliances = _Cie1000PsecMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 1)
)
_Cie1000PsecMibGroups_ObjectIdentity = ObjectIdentity
cie1000PsecMibGroups = _Cie1000PsecMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2)
)

# Managed Objects groups

cie1000PsecConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 1)
)
cie1000PsecConfigGlobalsInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecConfigGlobalsEnabled"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigGlobalsEnableAging"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigGlobalsAgingPeriodSecs"))
)
if mibBuilder.loadTexts:
    cie1000PsecConfigGlobalsInfoGroup.setStatus("current")

cie1000PsecConfigPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 2)
)
cie1000PsecConfigPortTableInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecConfigPortIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigPortEnabled"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigPortLimit"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigPortAction"))
)
if mibBuilder.loadTexts:
    cie1000PsecConfigPortTableInfoGroup.setStatus("current")

cie1000PsecStatusPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 3)
)
cie1000PsecStatusPortTableInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecStatusPortIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortUsers"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortLimitReached"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortShutdown"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortMacCount"))
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTableInfoGroup.setStatus("current")

cie1000PsecStatusPortTrapsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 4)
)
cie1000PsecStatusPortTrapsInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsUsers"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsLimitReached"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsShutdown"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsMacCount"))
)
if mibBuilder.loadTexts:
    cie1000PsecStatusPortTrapsInfoGroup.setStatus("current")

cie1000PsecControlPortReopenTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 5)
)
cie1000PsecControlPortReopenTableInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecControlPortReopenIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecControlPortReopenPortReOpen"))
)
if mibBuilder.loadTexts:
    cie1000PsecControlPortReopenTableInfoGroup.setStatus("current")

cie1000PsecStatisticsPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 6)
)
cie1000PsecStatisticsPortTableInfoGroup.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortAgeOrHold"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortCreationTime"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortState"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortMacId"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortVlanId"))
)
if mibBuilder.loadTexts:
    cie1000PsecStatisticsPortTableInfoGroup.setStatus("current")


# Notification objects

cie1000PsecTrapLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 6, 1)
)
cie1000PsecTrapLimitExceeded.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsUsers"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsLimitReached"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsShutdown"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsMacCount"))
)
if mibBuilder.loadTexts:
    cie1000PsecTrapLimitExceeded.setStatus(
        "current"
    )

cie1000PsecTrapMod = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 6, 2)
)
cie1000PsecTrapMod.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsIfIndex"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsUsers"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsLimitReached"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsShutdown"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsMacCount"))
)
if mibBuilder.loadTexts:
    cie1000PsecTrapMod.setStatus(
        "current"
    )

cie1000PsecTrapLimitRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 1, 6, 3)
)
cie1000PsecTrapLimitRecovered.setObjects(
    ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsIfIndex")
)
if mibBuilder.loadTexts:
    cie1000PsecTrapLimitRecovered.setStatus(
        "current"
    )


# Notifications groups

cie1000PsecTrapLimitExceededInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 7)
)
cie1000PsecTrapLimitExceededInfoGroup.setObjects(
    ("CIE1000-PSEC-MIB", "cie1000PsecTrapLimitExceeded")
)
if mibBuilder.loadTexts:
    cie1000PsecTrapLimitExceededInfoGroup.setStatus(
        "current"
    )

cie1000PsecTrapModInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 8)
)
cie1000PsecTrapModInfoGroup.setObjects(
    ("CIE1000-PSEC-MIB", "cie1000PsecTrapMod")
)
if mibBuilder.loadTexts:
    cie1000PsecTrapModInfoGroup.setStatus(
        "current"
    )

cie1000PsecTrapLimitRecoveredInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 2, 9)
)
cie1000PsecTrapLimitRecoveredInfoGroup.setObjects(
    ("CIE1000-PSEC-MIB", "cie1000PsecTrapLimitRecovered")
)
if mibBuilder.loadTexts:
    cie1000PsecTrapLimitRecoveredInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cie1000PsecMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 66, 2, 1, 1)
)
cie1000PsecMibCompliance.setObjects(
      *(("CIE1000-PSEC-MIB", "cie1000PsecConfigGlobalsInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecConfigPortTableInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTableInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatusPortTrapsInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecControlPortReopenTableInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecStatisticsPortTableInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecTrapLimitExceededInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecTrapModInfoGroup"),
        ("CIE1000-PSEC-MIB", "cie1000PsecTrapLimitRecoveredInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000PsecMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-PSEC-MIB",
    **{"CIE1000PsecLimitActionType": CIE1000PsecLimitActionType,
       "CIE1000PsecStateType": CIE1000PsecStateType,
       "cie1000PsecMib": cie1000PsecMib,
       "cie1000PsecMibObjects": cie1000PsecMibObjects,
       "cie1000PsecConfig": cie1000PsecConfig,
       "cie1000PsecConfigGlobals": cie1000PsecConfigGlobals,
       "cie1000PsecConfigGlobalsEnabled": cie1000PsecConfigGlobalsEnabled,
       "cie1000PsecConfigGlobalsEnableAging": cie1000PsecConfigGlobalsEnableAging,
       "cie1000PsecConfigGlobalsAgingPeriodSecs": cie1000PsecConfigGlobalsAgingPeriodSecs,
       "cie1000PsecConfigPortTable": cie1000PsecConfigPortTable,
       "cie1000PsecConfigPortEntry": cie1000PsecConfigPortEntry,
       "cie1000PsecConfigPortIfIndex": cie1000PsecConfigPortIfIndex,
       "cie1000PsecConfigPortEnabled": cie1000PsecConfigPortEnabled,
       "cie1000PsecConfigPortLimit": cie1000PsecConfigPortLimit,
       "cie1000PsecConfigPortAction": cie1000PsecConfigPortAction,
       "cie1000PsecStatus": cie1000PsecStatus,
       "cie1000PsecStatusPortTable": cie1000PsecStatusPortTable,
       "cie1000PsecStatusPortEntry": cie1000PsecStatusPortEntry,
       "cie1000PsecStatusPortIfIndex": cie1000PsecStatusPortIfIndex,
       "cie1000PsecStatusPortUsers": cie1000PsecStatusPortUsers,
       "cie1000PsecStatusPortLimitReached": cie1000PsecStatusPortLimitReached,
       "cie1000PsecStatusPortShutdown": cie1000PsecStatusPortShutdown,
       "cie1000PsecStatusPortMacCount": cie1000PsecStatusPortMacCount,
       "cie1000PsecStatusPortTrapsTable": cie1000PsecStatusPortTrapsTable,
       "cie1000PsecStatusPortTrapsEntry": cie1000PsecStatusPortTrapsEntry,
       "cie1000PsecStatusPortTrapsIfIndex": cie1000PsecStatusPortTrapsIfIndex,
       "cie1000PsecStatusPortTrapsUsers": cie1000PsecStatusPortTrapsUsers,
       "cie1000PsecStatusPortTrapsLimitReached": cie1000PsecStatusPortTrapsLimitReached,
       "cie1000PsecStatusPortTrapsShutdown": cie1000PsecStatusPortTrapsShutdown,
       "cie1000PsecStatusPortTrapsMacCount": cie1000PsecStatusPortTrapsMacCount,
       "cie1000PsecControl": cie1000PsecControl,
       "cie1000PsecControlPortReopenTable": cie1000PsecControlPortReopenTable,
       "cie1000PsecControlPortReopenEntry": cie1000PsecControlPortReopenEntry,
       "cie1000PsecControlPortReopenIfIndex": cie1000PsecControlPortReopenIfIndex,
       "cie1000PsecControlPortReopenPortReOpen": cie1000PsecControlPortReopenPortReOpen,
       "cie1000PsecStatistics": cie1000PsecStatistics,
       "cie1000PsecStatisticsPortTable": cie1000PsecStatisticsPortTable,
       "cie1000PsecStatisticsPortEntry": cie1000PsecStatisticsPortEntry,
       "cie1000PsecStatisticsPortIfIndex": cie1000PsecStatisticsPortIfIndex,
       "cie1000PsecStatisticsPortAgeOrHold": cie1000PsecStatisticsPortAgeOrHold,
       "cie1000PsecStatisticsPortCreationTime": cie1000PsecStatisticsPortCreationTime,
       "cie1000PsecStatisticsPortState": cie1000PsecStatisticsPortState,
       "cie1000PsecStatisticsPortMacId": cie1000PsecStatisticsPortMacId,
       "cie1000PsecStatisticsPortVlanId": cie1000PsecStatisticsPortVlanId,
       "cie1000PsecTrap": cie1000PsecTrap,
       "cie1000PsecTrapLimitExceeded": cie1000PsecTrapLimitExceeded,
       "cie1000PsecTrapMod": cie1000PsecTrapMod,
       "cie1000PsecTrapLimitRecovered": cie1000PsecTrapLimitRecovered,
       "cie1000PsecMibConformance": cie1000PsecMibConformance,
       "cie1000PsecMibCompliances": cie1000PsecMibCompliances,
       "cie1000PsecMibCompliance": cie1000PsecMibCompliance,
       "cie1000PsecMibGroups": cie1000PsecMibGroups,
       "cie1000PsecConfigGlobalsInfoGroup": cie1000PsecConfigGlobalsInfoGroup,
       "cie1000PsecConfigPortTableInfoGroup": cie1000PsecConfigPortTableInfoGroup,
       "cie1000PsecStatusPortTableInfoGroup": cie1000PsecStatusPortTableInfoGroup,
       "cie1000PsecStatusPortTrapsInfoGroup": cie1000PsecStatusPortTrapsInfoGroup,
       "cie1000PsecControlPortReopenTableInfoGroup": cie1000PsecControlPortReopenTableInfoGroup,
       "cie1000PsecStatisticsPortTableInfoGroup": cie1000PsecStatisticsPortTableInfoGroup,
       "cie1000PsecTrapLimitExceededInfoGroup": cie1000PsecTrapLimitExceededInfoGroup,
       "cie1000PsecTrapModInfoGroup": cie1000PsecTrapModInfoGroup,
       "cie1000PsecTrapLimitRecoveredInfoGroup": cie1000PsecTrapLimitRecoveredInfoGroup}
)
