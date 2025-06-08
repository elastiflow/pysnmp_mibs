# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DUPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-UNIFIED-COMPUTING-DUPE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 08:58:45 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsDupeOperation,
 CucsDupeStatus,
 CucsMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsDupeOperation",
    "CucsDupeStatus",
    "CucsMoMoClassId")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsDupeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDupeScopeTable_Object = MibTable
cucsDupeScopeTable = _CucsDupeScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1)
)
if mibBuilder.loadTexts:
    cucsDupeScopeTable.setStatus("current")
_CucsDupeScopeEntry_Object = MibTableRow
cucsDupeScopeEntry = _CucsDupeScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1)
)
cucsDupeScopeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DUPE-MIB", "cucsDupeScopeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDupeScopeEntry.setStatus("current")
_CucsDupeScopeInstanceId_Type = CucsManagedObjectId
_CucsDupeScopeInstanceId_Object = MibTableColumn
cucsDupeScopeInstanceId = _CucsDupeScopeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 1),
    _CucsDupeScopeInstanceId_Type()
)
cucsDupeScopeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDupeScopeInstanceId.setStatus("current")
_CucsDupeScopeDn_Type = CucsManagedObjectDn
_CucsDupeScopeDn_Object = MibTableColumn
cucsDupeScopeDn = _CucsDupeScopeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 2),
    _CucsDupeScopeDn_Type()
)
cucsDupeScopeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeDn.setStatus("current")
_CucsDupeScopeRn_Type = SnmpAdminString
_CucsDupeScopeRn_Object = MibTableColumn
cucsDupeScopeRn = _CucsDupeScopeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 3),
    _CucsDupeScopeRn_Type()
)
cucsDupeScopeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeRn.setStatus("current")
_CucsDupeScopeClientMoDn_Type = SnmpAdminString
_CucsDupeScopeClientMoDn_Object = MibTableColumn
cucsDupeScopeClientMoDn = _CucsDupeScopeClientMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 4),
    _CucsDupeScopeClientMoDn_Type()
)
cucsDupeScopeClientMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeClientMoDn.setStatus("current")
_CucsDupeScopeId_Type = Gauge32
_CucsDupeScopeId_Object = MibTableColumn
cucsDupeScopeId = _CucsDupeScopeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 5),
    _CucsDupeScopeId_Type()
)
cucsDupeScopeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeId.setStatus("current")
_CucsDupeScopeIsSystem_Type = TruthValue
_CucsDupeScopeIsSystem_Object = MibTableColumn
cucsDupeScopeIsSystem = _CucsDupeScopeIsSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 6),
    _CucsDupeScopeIsSystem_Type()
)
cucsDupeScopeIsSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeIsSystem.setStatus("current")
_CucsDupeScopeMoClassId_Type = CucsMoMoClassId
_CucsDupeScopeMoClassId_Object = MibTableColumn
cucsDupeScopeMoClassId = _CucsDupeScopeMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 7),
    _CucsDupeScopeMoClassId_Type()
)
cucsDupeScopeMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeMoClassId.setStatus("current")
_CucsDupeScopeOperCode_Type = CucsDupeOperation
_CucsDupeScopeOperCode_Object = MibTableColumn
cucsDupeScopeOperCode = _CucsDupeScopeOperCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 8),
    _CucsDupeScopeOperCode_Type()
)
cucsDupeScopeOperCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeOperCode.setStatus("current")
_CucsDupeScopeSecondaryKey_Type = SnmpAdminString
_CucsDupeScopeSecondaryKey_Object = MibTableColumn
cucsDupeScopeSecondaryKey = _CucsDupeScopeSecondaryKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 9),
    _CucsDupeScopeSecondaryKey_Type()
)
cucsDupeScopeSecondaryKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeSecondaryKey.setStatus("current")
_CucsDupeScopeSourceMoDn_Type = SnmpAdminString
_CucsDupeScopeSourceMoDn_Object = MibTableColumn
cucsDupeScopeSourceMoDn = _CucsDupeScopeSourceMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 1, 1, 10),
    _CucsDupeScopeSourceMoDn_Type()
)
cucsDupeScopeSourceMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeSourceMoDn.setStatus("current")
_CucsDupeScopeResultTable_Object = MibTable
cucsDupeScopeResultTable = _CucsDupeScopeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2)
)
if mibBuilder.loadTexts:
    cucsDupeScopeResultTable.setStatus("current")
_CucsDupeScopeResultEntry_Object = MibTableRow
cucsDupeScopeResultEntry = _CucsDupeScopeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1)
)
cucsDupeScopeResultEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DUPE-MIB", "cucsDupeScopeResultInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDupeScopeResultEntry.setStatus("current")
_CucsDupeScopeResultInstanceId_Type = CucsManagedObjectId
_CucsDupeScopeResultInstanceId_Object = MibTableColumn
cucsDupeScopeResultInstanceId = _CucsDupeScopeResultInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 1),
    _CucsDupeScopeResultInstanceId_Type()
)
cucsDupeScopeResultInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDupeScopeResultInstanceId.setStatus("current")
_CucsDupeScopeResultDn_Type = CucsManagedObjectDn
_CucsDupeScopeResultDn_Object = MibTableColumn
cucsDupeScopeResultDn = _CucsDupeScopeResultDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 2),
    _CucsDupeScopeResultDn_Type()
)
cucsDupeScopeResultDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeResultDn.setStatus("current")
_CucsDupeScopeResultRn_Type = SnmpAdminString
_CucsDupeScopeResultRn_Object = MibTableColumn
cucsDupeScopeResultRn = _CucsDupeScopeResultRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 3),
    _CucsDupeScopeResultRn_Type()
)
cucsDupeScopeResultRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeResultRn.setStatus("current")
_CucsDupeScopeResultMessage_Type = SnmpAdminString
_CucsDupeScopeResultMessage_Object = MibTableColumn
cucsDupeScopeResultMessage = _CucsDupeScopeResultMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 4),
    _CucsDupeScopeResultMessage_Type()
)
cucsDupeScopeResultMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeResultMessage.setStatus("current")
_CucsDupeScopeResultScopeStatus_Type = CucsDupeStatus
_CucsDupeScopeResultScopeStatus_Object = MibTableColumn
cucsDupeScopeResultScopeStatus = _CucsDupeScopeResultScopeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 5),
    _CucsDupeScopeResultScopeStatus_Type()
)
cucsDupeScopeResultScopeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeResultScopeStatus.setStatus("current")
_CucsDupeScopeResultUpdateTime_Type = DateAndTime
_CucsDupeScopeResultUpdateTime_Object = MibTableColumn
cucsDupeScopeResultUpdateTime = _CucsDupeScopeResultUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 78, 2, 1, 6),
    _CucsDupeScopeResultUpdateTime_Type()
)
cucsDupeScopeResultUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDupeScopeResultUpdateTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DUPE-MIB",
    **{"cucsDupeObjects": cucsDupeObjects,
       "cucsDupeScopeTable": cucsDupeScopeTable,
       "cucsDupeScopeEntry": cucsDupeScopeEntry,
       "cucsDupeScopeInstanceId": cucsDupeScopeInstanceId,
       "cucsDupeScopeDn": cucsDupeScopeDn,
       "cucsDupeScopeRn": cucsDupeScopeRn,
       "cucsDupeScopeClientMoDn": cucsDupeScopeClientMoDn,
       "cucsDupeScopeId": cucsDupeScopeId,
       "cucsDupeScopeIsSystem": cucsDupeScopeIsSystem,
       "cucsDupeScopeMoClassId": cucsDupeScopeMoClassId,
       "cucsDupeScopeOperCode": cucsDupeScopeOperCode,
       "cucsDupeScopeSecondaryKey": cucsDupeScopeSecondaryKey,
       "cucsDupeScopeSourceMoDn": cucsDupeScopeSourceMoDn,
       "cucsDupeScopeResultTable": cucsDupeScopeResultTable,
       "cucsDupeScopeResultEntry": cucsDupeScopeResultEntry,
       "cucsDupeScopeResultInstanceId": cucsDupeScopeResultInstanceId,
       "cucsDupeScopeResultDn": cucsDupeScopeResultDn,
       "cucsDupeScopeResultRn": cucsDupeScopeResultRn,
       "cucsDupeScopeResultMessage": cucsDupeScopeResultMessage,
       "cucsDupeScopeResultScopeStatus": cucsDupeScopeResultScopeStatus,
       "cucsDupeScopeResultUpdateTime": cucsDupeScopeResultUpdateTime}
)
