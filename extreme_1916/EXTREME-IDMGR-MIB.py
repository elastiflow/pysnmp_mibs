# SNMP MIB module (EXTREME-IDMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-IDMGR-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

extremeIdMgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ExtremeIdMgrInetAddrDetectMethod(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ipArp", 1),
          ("dhcpSnooping", 2))
    )


class ExtremeIdMgrInetAddrSecViolation(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("arp", 1),
          ("dos", 2),
          ("garp", 3),
          ("srcIpLockdown", 4),
          ("dhcpSnooping", 5))
    )


# MIB Managed Objects in the order of their OIDs

_ExtremeIdMgrTraps_ObjectIdentity = ObjectIdentity
extremeIdMgrTraps = _ExtremeIdMgrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1)
)
_ExtremeIdMgrTrapPrefix_ObjectIdentity = ObjectIdentity
extremeIdMgrTrapPrefix = _ExtremeIdMgrTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 0)
)


class _ExtremeIdMgrTrapSeverity_Type(Integer32):
    """Custom type extremeIdMgrTrapSeverity based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("notice", 4),
          ("info", 5),
          ("debug-summary", 6),
          ("debug-verbose", 7),
          ("debug-data", 8))
    )


_ExtremeIdMgrTrapSeverity_Type.__name__ = "Integer32"
_ExtremeIdMgrTrapSeverity_Object = MibScalar
extremeIdMgrTrapSeverity = _ExtremeIdMgrTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 1),
    _ExtremeIdMgrTrapSeverity_Type()
)
extremeIdMgrTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrTrapSeverity.setStatus("current")


class _ExtremeIdMgrMemUsageLevel_Type(Integer32):
    """Custom type extremeIdMgrMemUsageLevel based on Integer32"""
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
        *(("normal", 1),
          ("high", 2),
          ("critical", 3),
          ("maximum", 4))
    )


_ExtremeIdMgrMemUsageLevel_Type.__name__ = "Integer32"
_ExtremeIdMgrMemUsageLevel_Object = MibScalar
extremeIdMgrMemUsageLevel = _ExtremeIdMgrMemUsageLevel_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 2),
    _ExtremeIdMgrMemUsageLevel_Type()
)
extremeIdMgrMemUsageLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemUsageLevel.setStatus("current")
_ExtremeIdMgrMemUsage_Type = Integer32
_ExtremeIdMgrMemUsage_Object = MibScalar
extremeIdMgrMemUsage = _ExtremeIdMgrMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 3),
    _ExtremeIdMgrMemUsage_Type()
)
extremeIdMgrMemUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemUsage.setStatus("current")
_ExtremeIdMgrMemMaxSize_Type = Integer32
_ExtremeIdMgrMemMaxSize_Object = MibScalar
extremeIdMgrMemMaxSize = _ExtremeIdMgrMemMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 4),
    _ExtremeIdMgrMemMaxSize_Type()
)
extremeIdMgrMemMaxSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrMemMaxSize.setStatus("current")
_ExtremeIdMgrEffectiveStaleAgingTime_Type = Integer32
_ExtremeIdMgrEffectiveStaleAgingTime_Object = MibScalar
extremeIdMgrEffectiveStaleAgingTime = _ExtremeIdMgrEffectiveStaleAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 5),
    _ExtremeIdMgrEffectiveStaleAgingTime_Type()
)
extremeIdMgrEffectiveStaleAgingTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeIdMgrEffectiveStaleAgingTime.setStatus("current")
_ExtremeIdMgrObjects_ObjectIdentity = ObjectIdentity
extremeIdMgrObjects = _ExtremeIdMgrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2)
)
_ExtremeLocationTable_Object = MibTable
extremeLocationTable = _ExtremeLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1)
)
if mibBuilder.loadTexts:
    extremeLocationTable.setStatus("current")
_ExtremeLocationEntry_Object = MibTableRow
extremeLocationEntry = _ExtremeLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1, 1)
)
extremeLocationEntry.setIndexNames(
    (0, "EXTREME-IDMGR-MIB", "extremeLocationMacAddress"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInterface"),
)
if mibBuilder.loadTexts:
    extremeLocationEntry.setStatus("current")
_ExtremeLocationMacAddress_Type = MacAddress
_ExtremeLocationMacAddress_Object = MibTableColumn
extremeLocationMacAddress = _ExtremeLocationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1, 1, 1),
    _ExtremeLocationMacAddress_Type()
)
extremeLocationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeLocationMacAddress.setStatus("current")
_ExtremeLocationInterface_Type = InterfaceIndex
_ExtremeLocationInterface_Object = MibTableColumn
extremeLocationInterface = _ExtremeLocationInterface_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1, 1, 2),
    _ExtremeLocationInterface_Type()
)
extremeLocationInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeLocationInterface.setStatus("current")


class _ExtremeLocationDetectMethods_Type(Bits):
    """Custom type extremeLocationDetectMethods based on Bits"""
    namedValues = NamedValues(
        *(("fdbLearn", 1),
          ("ipArp", 2),
          ("dhcpSnooping", 3),
          ("lldp", 4),
          ("kerberos", 5),
          ("netloginMac", 6),
          ("netloginWeb", 7),
          ("netloginDot1x", 8))
    )

_ExtremeLocationDetectMethods_Type.__name__ = "Bits"
_ExtremeLocationDetectMethods_Object = MibTableColumn
extremeLocationDetectMethods = _ExtremeLocationDetectMethods_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1, 1, 3),
    _ExtremeLocationDetectMethods_Type()
)
extremeLocationDetectMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationDetectMethods.setStatus("current")
_ExtremeLocationDetectTime_Type = DateAndTime
_ExtremeLocationDetectTime_Object = MibTableColumn
extremeLocationDetectTime = _ExtremeLocationDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 1, 1, 4),
    _ExtremeLocationDetectTime_Type()
)
extremeLocationDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationDetectTime.setStatus("current")
_ExtremeLocationDetectMethodTable_Object = MibTable
extremeLocationDetectMethodTable = _ExtremeLocationDetectMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 2)
)
if mibBuilder.loadTexts:
    extremeLocationDetectMethodTable.setStatus("current")
_ExtremeLocationDetectMethodEntry_Object = MibTableRow
extremeLocationDetectMethodEntry = _ExtremeLocationDetectMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 2, 1)
)
extremeLocationDetectMethodEntry.setIndexNames(
    (0, "EXTREME-IDMGR-MIB", "extremeLocationDetectMethod"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationMacAddress"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInterface"),
)
if mibBuilder.loadTexts:
    extremeLocationDetectMethodEntry.setStatus("current")


class _ExtremeLocationDetectMethod_Type(Integer32):
    """Custom type extremeLocationDetectMethod based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("fdbLearn", 1),
          ("ipArp", 2),
          ("dhcpSnooping", 3),
          ("lldp", 4),
          ("kerberos", 5),
          ("netloginMac", 6),
          ("netloginWeb", 7),
          ("netloginDot1x", 8))
    )


_ExtremeLocationDetectMethod_Type.__name__ = "Integer32"
_ExtremeLocationDetectMethod_Object = MibTableColumn
extremeLocationDetectMethod = _ExtremeLocationDetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 2, 1, 1),
    _ExtremeLocationDetectMethod_Type()
)
extremeLocationDetectMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeLocationDetectMethod.setStatus("current")
_ExtremeLocationDetectMethodData_Type = AutonomousType
_ExtremeLocationDetectMethodData_Object = MibTableColumn
extremeLocationDetectMethodData = _ExtremeLocationDetectMethodData_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 2, 1, 2),
    _ExtremeLocationDetectMethodData_Type()
)
extremeLocationDetectMethodData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationDetectMethodData.setStatus("current")
_ExtremeLocationVlanTable_Object = MibTable
extremeLocationVlanTable = _ExtremeLocationVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 3)
)
if mibBuilder.loadTexts:
    extremeLocationVlanTable.setStatus("current")
_ExtremeLocationVlanEntry_Object = MibTableRow
extremeLocationVlanEntry = _ExtremeLocationVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 3, 1)
)
extremeLocationVlanEntry.setIndexNames(
    (0, "EXTREME-IDMGR-MIB", "extremeLocationMacAddress"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInterface"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeLocationVlanEntry.setStatus("current")
_ExtremeLocationVlanIfIndex_Type = InterfaceIndex
_ExtremeLocationVlanIfIndex_Object = MibTableColumn
extremeLocationVlanIfIndex = _ExtremeLocationVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 3, 1, 1),
    _ExtremeLocationVlanIfIndex_Type()
)
extremeLocationVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationVlanIfIndex.setStatus("current")
_ExtremeLocationInetAddrTable_Object = MibTable
extremeLocationInetAddrTable = _ExtremeLocationInetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4)
)
if mibBuilder.loadTexts:
    extremeLocationInetAddrTable.setStatus("current")
_ExtremeLocationInetAddrEntry_Object = MibTableRow
extremeLocationInetAddrEntry = _ExtremeLocationInetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4, 1)
)
extremeLocationInetAddrEntry.setIndexNames(
    (0, "EXTREME-IDMGR-MIB", "extremeLocationMacAddress"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInterface"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationVlanIfIndex"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInetAddrType"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInetAddr"),
)
if mibBuilder.loadTexts:
    extremeLocationInetAddrEntry.setStatus("current")
_ExtremeLocationInetAddrType_Type = InetAddressType
_ExtremeLocationInetAddrType_Object = MibTableColumn
extremeLocationInetAddrType = _ExtremeLocationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4, 1, 1),
    _ExtremeLocationInetAddrType_Type()
)
extremeLocationInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeLocationInetAddrType.setStatus("current")
_ExtremeLocationInetAddr_Type = InetAddress
_ExtremeLocationInetAddr_Object = MibTableColumn
extremeLocationInetAddr = _ExtremeLocationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4, 1, 2),
    _ExtremeLocationInetAddr_Type()
)
extremeLocationInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeLocationInetAddr.setStatus("current")
_ExtremeLocationInetAddrDetectMethod_Type = ExtremeIdMgrInetAddrDetectMethod
_ExtremeLocationInetAddrDetectMethod_Object = MibTableColumn
extremeLocationInetAddrDetectMethod = _ExtremeLocationInetAddrDetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4, 1, 3),
    _ExtremeLocationInetAddrDetectMethod_Type()
)
extremeLocationInetAddrDetectMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationInetAddrDetectMethod.setStatus("current")
_ExtremeLocationInetAddrSecViolations_Type = ExtremeIdMgrInetAddrSecViolation
_ExtremeLocationInetAddrSecViolations_Object = MibTableColumn
extremeLocationInetAddrSecViolations = _ExtremeLocationInetAddrSecViolations_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 4, 1, 4),
    _ExtremeLocationInetAddrSecViolations_Type()
)
extremeLocationInetAddrSecViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationInetAddrSecViolations.setStatus("current")
_ExtremeLocationInetAddrInvTable_Object = MibTable
extremeLocationInetAddrInvTable = _ExtremeLocationInetAddrInvTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 5)
)
if mibBuilder.loadTexts:
    extremeLocationInetAddrInvTable.setStatus("current")
_ExtremeLocationInetAddrInvEntry_Object = MibTableRow
extremeLocationInetAddrInvEntry = _ExtremeLocationInetAddrInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 5, 1)
)
extremeLocationInetAddrInvEntry.setIndexNames(
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInetAddrType"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInetAddr"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationVlanIfIndex"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationInterface"),
    (0, "EXTREME-IDMGR-MIB", "extremeLocationMacAddress"),
)
if mibBuilder.loadTexts:
    extremeLocationInetAddrInvEntry.setStatus("current")
_ExtremeLocationInetAddrInvDetectMethod_Type = ExtremeIdMgrInetAddrDetectMethod
_ExtremeLocationInetAddrInvDetectMethod_Object = MibTableColumn
extremeLocationInetAddrInvDetectMethod = _ExtremeLocationInetAddrInvDetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 5, 1, 1),
    _ExtremeLocationInetAddrInvDetectMethod_Type()
)
extremeLocationInetAddrInvDetectMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationInetAddrInvDetectMethod.setStatus("current")
_ExtremeLocationInetAddrInvSecViolations_Type = ExtremeIdMgrInetAddrSecViolation
_ExtremeLocationInetAddrInvSecViolations_Object = MibTableColumn
extremeLocationInetAddrInvSecViolations = _ExtremeLocationInetAddrInvSecViolations_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 2, 5, 1, 2),
    _ExtremeLocationInetAddrInvSecViolations_Type()
)
extremeLocationInetAddrInvSecViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeLocationInetAddrInvSecViolations.setStatus("current")
_ExtremeIdMgrConformance_ObjectIdentity = ObjectIdentity
extremeIdMgrConformance = _ExtremeIdMgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 3)
)

# Managed Objects groups


# Notification objects

extremeIdMgrMemLevelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 36, 1, 0, 1)
)
extremeIdMgrMemLevelChange.setObjects(
      *(("EXTREME-IDMGR-MIB", "extremeIdMgrTrapSeverity"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemUsageLevel"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemUsage"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrMemMaxSize"),
        ("EXTREME-IDMGR-MIB", "extremeIdMgrEffectiveStaleAgingTime"))
)
if mibBuilder.loadTexts:
    extremeIdMgrMemLevelChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-IDMGR-MIB",
    **{"ExtremeIdMgrInetAddrDetectMethod": ExtremeIdMgrInetAddrDetectMethod,
       "ExtremeIdMgrInetAddrSecViolation": ExtremeIdMgrInetAddrSecViolation,
       "extremeIdMgr": extremeIdMgr,
       "extremeIdMgrTraps": extremeIdMgrTraps,
       "extremeIdMgrTrapPrefix": extremeIdMgrTrapPrefix,
       "extremeIdMgrMemLevelChange": extremeIdMgrMemLevelChange,
       "extremeIdMgrTrapSeverity": extremeIdMgrTrapSeverity,
       "extremeIdMgrMemUsageLevel": extremeIdMgrMemUsageLevel,
       "extremeIdMgrMemUsage": extremeIdMgrMemUsage,
       "extremeIdMgrMemMaxSize": extremeIdMgrMemMaxSize,
       "extremeIdMgrEffectiveStaleAgingTime": extremeIdMgrEffectiveStaleAgingTime,
       "extremeIdMgrObjects": extremeIdMgrObjects,
       "extremeLocationTable": extremeLocationTable,
       "extremeLocationEntry": extremeLocationEntry,
       "extremeLocationMacAddress": extremeLocationMacAddress,
       "extremeLocationInterface": extremeLocationInterface,
       "extremeLocationDetectMethods": extremeLocationDetectMethods,
       "extremeLocationDetectTime": extremeLocationDetectTime,
       "extremeLocationDetectMethodTable": extremeLocationDetectMethodTable,
       "extremeLocationDetectMethodEntry": extremeLocationDetectMethodEntry,
       "extremeLocationDetectMethod": extremeLocationDetectMethod,
       "extremeLocationDetectMethodData": extremeLocationDetectMethodData,
       "extremeLocationVlanTable": extremeLocationVlanTable,
       "extremeLocationVlanEntry": extremeLocationVlanEntry,
       "extremeLocationVlanIfIndex": extremeLocationVlanIfIndex,
       "extremeLocationInetAddrTable": extremeLocationInetAddrTable,
       "extremeLocationInetAddrEntry": extremeLocationInetAddrEntry,
       "extremeLocationInetAddrType": extremeLocationInetAddrType,
       "extremeLocationInetAddr": extremeLocationInetAddr,
       "extremeLocationInetAddrDetectMethod": extremeLocationInetAddrDetectMethod,
       "extremeLocationInetAddrSecViolations": extremeLocationInetAddrSecViolations,
       "extremeLocationInetAddrInvTable": extremeLocationInetAddrInvTable,
       "extremeLocationInetAddrInvEntry": extremeLocationInetAddrInvEntry,
       "extremeLocationInetAddrInvDetectMethod": extremeLocationInetAddrInvDetectMethod,
       "extremeLocationInetAddrInvSecViolations": extremeLocationInetAddrInvSecViolations,
       "extremeIdMgrConformance": extremeIdMgrConformance}
)
