# SNMP MIB module (RUIJIE-PFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PFC-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "ConfigStatus",
    "IfIndex")

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

ruijiePfcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157)
)
if mibBuilder.loadTexts:
    ruijiePfcMIB.setRevisions(
        ("2017-12-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePfcCounterMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePfcCounterMIBObjects = _RuijiePfcCounterMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1)
)
_RuijiePfcIfPriorityCounterTable_Object = MibTable
ruijiePfcIfPriorityCounterTable = _RuijiePfcIfPriorityCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1)
)
if mibBuilder.loadTexts:
    ruijiePfcIfPriorityCounterTable.setStatus("current")
_RuijiePfcIfPriorityCounterEntry_Object = MibTableRow
ruijiePfcIfPriorityCounterEntry = _RuijiePfcIfPriorityCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1)
)
ruijiePfcIfPriorityCounterEntry.setIndexNames(
    (0, "RUIJIE-PFC-MIB", "ruijieIfIndex"),
    (0, "RUIJIE-PFC-MIB", "ruijiePfcPriority"),
)
if mibBuilder.loadTexts:
    ruijiePfcIfPriorityCounterEntry.setStatus("current")
_RuijieIfIndex_Type = IfIndex
_RuijieIfIndex_Object = MibTableColumn
ruijieIfIndex = _RuijieIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 1),
    _RuijieIfIndex_Type()
)
ruijieIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIndex.setStatus("current")
_RuijiePfcPriority_Type = Integer32
_RuijiePfcPriority_Object = MibTableColumn
ruijiePfcPriority = _RuijiePfcPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 2),
    _RuijiePfcPriority_Type()
)
ruijiePfcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcPriority.setStatus("current")
_RuijiePfcRequests_Type = Counter64
_RuijiePfcRequests_Object = MibTableColumn
ruijiePfcRequests = _RuijiePfcRequests_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 3),
    _RuijiePfcRequests_Type()
)
ruijiePfcRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequests.setStatus("current")
_RuijiePfcRequestsRate_Type = Counter64
_RuijiePfcRequestsRate_Object = MibTableColumn
ruijiePfcRequestsRate = _RuijiePfcRequestsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 4),
    _RuijiePfcRequestsRate_Type()
)
ruijiePfcRequestsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate.setStatus("current")
_RuijiePfcRequestsRate1st_Type = Counter64
_RuijiePfcRequestsRate1st_Object = MibTableColumn
ruijiePfcRequestsRate1st = _RuijiePfcRequestsRate1st_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 5),
    _RuijiePfcRequestsRate1st_Type()
)
ruijiePfcRequestsRate1st.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate1st.setStatus("current")
_RuijiePfcRequestsRate1stTime_Type = DisplayString
_RuijiePfcRequestsRate1stTime_Object = MibTableColumn
ruijiePfcRequestsRate1stTime = _RuijiePfcRequestsRate1stTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 6),
    _RuijiePfcRequestsRate1stTime_Type()
)
ruijiePfcRequestsRate1stTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate1stTime.setStatus("current")
_RuijiePfcRequestsRate2nd_Type = Counter64
_RuijiePfcRequestsRate2nd_Object = MibTableColumn
ruijiePfcRequestsRate2nd = _RuijiePfcRequestsRate2nd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 7),
    _RuijiePfcRequestsRate2nd_Type()
)
ruijiePfcRequestsRate2nd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate2nd.setStatus("current")
_RuijiePfcRequestsRate2ndTime_Type = DisplayString
_RuijiePfcRequestsRate2ndTime_Object = MibTableColumn
ruijiePfcRequestsRate2ndTime = _RuijiePfcRequestsRate2ndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 8),
    _RuijiePfcRequestsRate2ndTime_Type()
)
ruijiePfcRequestsRate2ndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate2ndTime.setStatus("current")
_RuijiePfcRequestsRate3rd_Type = Counter64
_RuijiePfcRequestsRate3rd_Object = MibTableColumn
ruijiePfcRequestsRate3rd = _RuijiePfcRequestsRate3rd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 9),
    _RuijiePfcRequestsRate3rd_Type()
)
ruijiePfcRequestsRate3rd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate3rd.setStatus("current")
_RuijiePfcRequestsRate3rdTime_Type = DisplayString
_RuijiePfcRequestsRate3rdTime_Object = MibTableColumn
ruijiePfcRequestsRate3rdTime = _RuijiePfcRequestsRate3rdTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 10),
    _RuijiePfcRequestsRate3rdTime_Type()
)
ruijiePfcRequestsRate3rdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcRequestsRate3rdTime.setStatus("current")
_RuijiePfcIndications_Type = Counter64
_RuijiePfcIndications_Object = MibTableColumn
ruijiePfcIndications = _RuijiePfcIndications_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 11),
    _RuijiePfcIndications_Type()
)
ruijiePfcIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndications.setStatus("current")
_RuijiePfcIndicationsRate_Type = Counter64
_RuijiePfcIndicationsRate_Object = MibTableColumn
ruijiePfcIndicationsRate = _RuijiePfcIndicationsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 12),
    _RuijiePfcIndicationsRate_Type()
)
ruijiePfcIndicationsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate.setStatus("current")
_RuijiePfcIndicationsRate1st_Type = Counter64
_RuijiePfcIndicationsRate1st_Object = MibTableColumn
ruijiePfcIndicationsRate1st = _RuijiePfcIndicationsRate1st_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 13),
    _RuijiePfcIndicationsRate1st_Type()
)
ruijiePfcIndicationsRate1st.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate1st.setStatus("current")
_RuijiePfcIndicationsRate1stTime_Type = DisplayString
_RuijiePfcIndicationsRate1stTime_Object = MibTableColumn
ruijiePfcIndicationsRate1stTime = _RuijiePfcIndicationsRate1stTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 14),
    _RuijiePfcIndicationsRate1stTime_Type()
)
ruijiePfcIndicationsRate1stTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate1stTime.setStatus("current")
_RuijiePfcIndicationsRate2nd_Type = Counter64
_RuijiePfcIndicationsRate2nd_Object = MibTableColumn
ruijiePfcIndicationsRate2nd = _RuijiePfcIndicationsRate2nd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 15),
    _RuijiePfcIndicationsRate2nd_Type()
)
ruijiePfcIndicationsRate2nd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate2nd.setStatus("current")
_RuijiePfcIndicationsRate2ndTime_Type = DisplayString
_RuijiePfcIndicationsRate2ndTime_Object = MibTableColumn
ruijiePfcIndicationsRate2ndTime = _RuijiePfcIndicationsRate2ndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 16),
    _RuijiePfcIndicationsRate2ndTime_Type()
)
ruijiePfcIndicationsRate2ndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate2ndTime.setStatus("current")
_RuijiePfcIndicationsRate3rd_Type = Counter64
_RuijiePfcIndicationsRate3rd_Object = MibTableColumn
ruijiePfcIndicationsRate3rd = _RuijiePfcIndicationsRate3rd_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 17),
    _RuijiePfcIndicationsRate3rd_Type()
)
ruijiePfcIndicationsRate3rd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate3rd.setStatus("current")
_RuijiePfcIndicationsRate3rdTime_Type = DisplayString
_RuijiePfcIndicationsRate3rdTime_Object = MibTableColumn
ruijiePfcIndicationsRate3rdTime = _RuijiePfcIndicationsRate3rdTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 1, 1, 1, 18),
    _RuijiePfcIndicationsRate3rdTime_Type()
)
ruijiePfcIndicationsRate3rdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePfcIndicationsRate3rdTime.setStatus("current")
_RuijiePfcMIBConformance_ObjectIdentity = ObjectIdentity
ruijiePfcMIBConformance = _RuijiePfcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 2)
)

# Managed Objects groups

ruijiePfcIfPriorityCounterMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 157, 2, 1)
)
ruijiePfcIfPriorityCounterMIBGroup.setObjects(
      *(("RUIJIE-PFC-MIB", "ruijieIfIndex"),
        ("RUIJIE-PFC-MIB", "ruijiePfcPriority"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequests"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate1st"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate1stTime"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate2nd"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate2ndTime"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate3rd"),
        ("RUIJIE-PFC-MIB", "ruijiePfcRequestsRate3rdTime"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndications"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate1st"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate1stTime"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate2nd"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate2ndTime"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate3rd"),
        ("RUIJIE-PFC-MIB", "ruijiePfcIndicationsRate3rdTime"))
)
if mibBuilder.loadTexts:
    ruijiePfcIfPriorityCounterMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PFC-MIB",
    **{"ruijiePfcMIB": ruijiePfcMIB,
       "ruijiePfcCounterMIBObjects": ruijiePfcCounterMIBObjects,
       "ruijiePfcIfPriorityCounterTable": ruijiePfcIfPriorityCounterTable,
       "ruijiePfcIfPriorityCounterEntry": ruijiePfcIfPriorityCounterEntry,
       "ruijieIfIndex": ruijieIfIndex,
       "ruijiePfcPriority": ruijiePfcPriority,
       "ruijiePfcRequests": ruijiePfcRequests,
       "ruijiePfcRequestsRate": ruijiePfcRequestsRate,
       "ruijiePfcRequestsRate1st": ruijiePfcRequestsRate1st,
       "ruijiePfcRequestsRate1stTime": ruijiePfcRequestsRate1stTime,
       "ruijiePfcRequestsRate2nd": ruijiePfcRequestsRate2nd,
       "ruijiePfcRequestsRate2ndTime": ruijiePfcRequestsRate2ndTime,
       "ruijiePfcRequestsRate3rd": ruijiePfcRequestsRate3rd,
       "ruijiePfcRequestsRate3rdTime": ruijiePfcRequestsRate3rdTime,
       "ruijiePfcIndications": ruijiePfcIndications,
       "ruijiePfcIndicationsRate": ruijiePfcIndicationsRate,
       "ruijiePfcIndicationsRate1st": ruijiePfcIndicationsRate1st,
       "ruijiePfcIndicationsRate1stTime": ruijiePfcIndicationsRate1stTime,
       "ruijiePfcIndicationsRate2nd": ruijiePfcIndicationsRate2nd,
       "ruijiePfcIndicationsRate2ndTime": ruijiePfcIndicationsRate2ndTime,
       "ruijiePfcIndicationsRate3rd": ruijiePfcIndicationsRate3rd,
       "ruijiePfcIndicationsRate3rdTime": ruijiePfcIndicationsRate3rdTime,
       "ruijiePfcMIBConformance": ruijiePfcMIBConformance,
       "ruijiePfcIfPriorityCounterMIBGroup": ruijiePfcIfPriorityCounterMIBGroup}
)
