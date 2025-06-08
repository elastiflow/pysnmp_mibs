# SNMP MIB module (RUIJIE-WAN-FPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-WAN-FPM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:00 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieWanFpmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153)
)
if mibBuilder.loadTexts:
    ruijieWanFpmMIB.setRevisions(
        ("2017-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWanFpmMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWanFpmMIBObjects = _RuijieWanFpmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1)
)
_RuijieWanFpmResultsTable_Object = MibTable
ruijieWanFpmResultsTable = _RuijieWanFpmResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWanFpmResultsTable.setStatus("current")
_RuijieWanFpmResultsEntry_Object = MibTableRow
ruijieWanFpmResultsEntry = _RuijieWanFpmResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1)
)
ruijieWanFpmResultsEntry.setIndexNames(
    (0, "RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsIfIndex"),
)
if mibBuilder.loadTexts:
    ruijieWanFpmResultsEntry.setStatus("current")
_RuijieWanFpmResultsIfIndex_Type = IfIndex
_RuijieWanFpmResultsIfIndex_Object = MibTableColumn
ruijieWanFpmResultsIfIndex = _RuijieWanFpmResultsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 1),
    _RuijieWanFpmResultsIfIndex_Type()
)
ruijieWanFpmResultsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsIfIndex.setStatus("current")


class _RuijieWanFpmResultsMode_Type(Integer32):
    """Custom type ruijieWanFpmResultsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_RuijieWanFpmResultsMode_Type.__name__ = "Integer32"
_RuijieWanFpmResultsMode_Object = MibTableColumn
ruijieWanFpmResultsMode = _RuijieWanFpmResultsMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 2),
    _RuijieWanFpmResultsMode_Type()
)
ruijieWanFpmResultsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsMode.setStatus("current")
_RuijieWanFpmResultsPeerIp_Type = InetAddress
_RuijieWanFpmResultsPeerIp_Object = MibTableColumn
ruijieWanFpmResultsPeerIp = _RuijieWanFpmResultsPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 3),
    _RuijieWanFpmResultsPeerIp_Type()
)
ruijieWanFpmResultsPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsPeerIp.setStatus("current")
_RuijieWanFpmResultsNetworkAF_Type = InetAddressType
_RuijieWanFpmResultsNetworkAF_Object = MibTableColumn
ruijieWanFpmResultsNetworkAF = _RuijieWanFpmResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 4),
    _RuijieWanFpmResultsNetworkAF_Type()
)
ruijieWanFpmResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsNetworkAF.setStatus("current")


class _RuijieWanFpmResultsSessStatus_Type(Integer32):
    """Custom type ruijieWanFpmResultsSessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("reserved", 3))
    )


_RuijieWanFpmResultsSessStatus_Type.__name__ = "Integer32"
_RuijieWanFpmResultsSessStatus_Object = MibTableColumn
ruijieWanFpmResultsSessStatus = _RuijieWanFpmResultsSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 5),
    _RuijieWanFpmResultsSessStatus_Type()
)
ruijieWanFpmResultsSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsSessStatus.setStatus("current")


class _RuijieWanFpmResultsLinkQuality_Type(Integer32):
    """Custom type ruijieWanFpmResultsLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("well", 1),
          ("worse", 2),
          ("reserved", 3))
    )


_RuijieWanFpmResultsLinkQuality_Type.__name__ = "Integer32"
_RuijieWanFpmResultsLinkQuality_Object = MibTableColumn
ruijieWanFpmResultsLinkQuality = _RuijieWanFpmResultsLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 6),
    _RuijieWanFpmResultsLinkQuality_Type()
)
ruijieWanFpmResultsLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsLinkQuality.setStatus("current")


class _RuijieWanFpmResultsWorseAction_Type(Integer32):
    """Custom type ruijieWanFpmResultsWorseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("unforward", 2))
    )


_RuijieWanFpmResultsWorseAction_Type.__name__ = "Integer32"
_RuijieWanFpmResultsWorseAction_Object = MibTableColumn
ruijieWanFpmResultsWorseAction = _RuijieWanFpmResultsWorseAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 7),
    _RuijieWanFpmResultsWorseAction_Type()
)
ruijieWanFpmResultsWorseAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsWorseAction.setStatus("current")
_RuijieWanFpmResultsRTT_Type = Unsigned32
_RuijieWanFpmResultsRTT_Object = MibTableColumn
ruijieWanFpmResultsRTT = _RuijieWanFpmResultsRTT_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 8),
    _RuijieWanFpmResultsRTT_Type()
)
ruijieWanFpmResultsRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsRTT.setStatus("current")
_RuijieWanFpmResultsJitter_Type = Unsigned32
_RuijieWanFpmResultsJitter_Object = MibTableColumn
ruijieWanFpmResultsJitter = _RuijieWanFpmResultsJitter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 9),
    _RuijieWanFpmResultsJitter_Type()
)
ruijieWanFpmResultsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsJitter.setStatus("current")
_RuijieWanFpmResultsUpDroprate_Type = Unsigned32
_RuijieWanFpmResultsUpDroprate_Object = MibTableColumn
ruijieWanFpmResultsUpDroprate = _RuijieWanFpmResultsUpDroprate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 10),
    _RuijieWanFpmResultsUpDroprate_Type()
)
ruijieWanFpmResultsUpDroprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsUpDroprate.setStatus("current")
_RuijieWanFpmResultsDownDroprate_Type = Unsigned32
_RuijieWanFpmResultsDownDroprate_Object = MibTableColumn
ruijieWanFpmResultsDownDroprate = _RuijieWanFpmResultsDownDroprate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 11),
    _RuijieWanFpmResultsDownDroprate_Type()
)
ruijieWanFpmResultsDownDroprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsDownDroprate.setStatus("current")
_RuijieWanFpmResultsByteTxSpeed_Type = Unsigned32
_RuijieWanFpmResultsByteTxSpeed_Object = MibTableColumn
ruijieWanFpmResultsByteTxSpeed = _RuijieWanFpmResultsByteTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 12),
    _RuijieWanFpmResultsByteTxSpeed_Type()
)
ruijieWanFpmResultsByteTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsByteTxSpeed.setStatus("current")
_RuijieWanFpmResultsByteRxSpeed_Type = Unsigned32
_RuijieWanFpmResultsByteRxSpeed_Object = MibTableColumn
ruijieWanFpmResultsByteRxSpeed = _RuijieWanFpmResultsByteRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 13),
    _RuijieWanFpmResultsByteRxSpeed_Type()
)
ruijieWanFpmResultsByteRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsByteRxSpeed.setStatus("current")
_RuijieWanFpmResultsPktsTxSpeed_Type = Unsigned32
_RuijieWanFpmResultsPktsTxSpeed_Object = MibTableColumn
ruijieWanFpmResultsPktsTxSpeed = _RuijieWanFpmResultsPktsTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 14),
    _RuijieWanFpmResultsPktsTxSpeed_Type()
)
ruijieWanFpmResultsPktsTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsPktsTxSpeed.setStatus("current")
_RuijieWanFpmResultsPktsRxSpeed_Type = Unsigned32
_RuijieWanFpmResultsPktsRxSpeed_Object = MibTableColumn
ruijieWanFpmResultsPktsRxSpeed = _RuijieWanFpmResultsPktsRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 15),
    _RuijieWanFpmResultsPktsRxSpeed_Type()
)
ruijieWanFpmResultsPktsRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsPktsRxSpeed.setStatus("current")
_RuijieWanFpmResultsCresteTime_Type = DateAndTime
_RuijieWanFpmResultsCresteTime_Object = MibTableColumn
ruijieWanFpmResultsCresteTime = _RuijieWanFpmResultsCresteTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 16),
    _RuijieWanFpmResultsCresteTime_Type()
)
ruijieWanFpmResultsCresteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsCresteTime.setStatus("current")


class _RuijieWanFpmResultsTrapType_Type(Integer32):
    """Custom type ruijieWanFpmResultsTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("getPeriodResult", 1),
          ("getTickResult", 2),
          ("reserved", 3))
    )


_RuijieWanFpmResultsTrapType_Type.__name__ = "Integer32"
_RuijieWanFpmResultsTrapType_Object = MibTableColumn
ruijieWanFpmResultsTrapType = _RuijieWanFpmResultsTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 17),
    _RuijieWanFpmResultsTrapType_Type()
)
ruijieWanFpmResultsTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsTrapType.setStatus("current")
_RuijieWanFpmResultsSessId_Type = Unsigned32
_RuijieWanFpmResultsSessId_Object = MibTableColumn
ruijieWanFpmResultsSessId = _RuijieWanFpmResultsSessId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 1, 1, 1, 18),
    _RuijieWanFpmResultsSessId_Type()
)
ruijieWanFpmResultsSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWanFpmResultsSessId.setStatus("current")
_RuijieWanFpmMonitor_ObjectIdentity = ObjectIdentity
ruijieWanFpmMonitor = _RuijieWanFpmMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 2)
)
_RuijieWanFpmMonitorTRAP_ObjectIdentity = ObjectIdentity
ruijieWanFpmMonitorTRAP = _RuijieWanFpmMonitorTRAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 2, 1)
)
_RuijieWanFpmNotifications_ObjectIdentity = ObjectIdentity
ruijieWanFpmNotifications = _RuijieWanFpmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 2, 1, 1)
)

# Managed Objects groups


# Notification objects

ruijieWanFpmLqWell = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 2, 1, 1, 1)
)
ruijieWanFpmLqWell.setObjects(
      *(("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsIfIndex"),
        ("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsSessStatus"),
        ("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsLinkQuality"))
)
if mibBuilder.loadTexts:
    ruijieWanFpmLqWell.setStatus(
        "current"
    )

ruijieWanFpmLqBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 153, 2, 1, 1, 2)
)
ruijieWanFpmLqBad.setObjects(
      *(("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsIfIndex"),
        ("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsSessStatus"),
        ("RUIJIE-WAN-FPM-MIB", "ruijieWanFpmResultsLinkQuality"))
)
if mibBuilder.loadTexts:
    ruijieWanFpmLqBad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-WAN-FPM-MIB",
    **{"ruijieWanFpmMIB": ruijieWanFpmMIB,
       "ruijieWanFpmMIBObjects": ruijieWanFpmMIBObjects,
       "ruijieWanFpmResultsTable": ruijieWanFpmResultsTable,
       "ruijieWanFpmResultsEntry": ruijieWanFpmResultsEntry,
       "ruijieWanFpmResultsIfIndex": ruijieWanFpmResultsIfIndex,
       "ruijieWanFpmResultsMode": ruijieWanFpmResultsMode,
       "ruijieWanFpmResultsPeerIp": ruijieWanFpmResultsPeerIp,
       "ruijieWanFpmResultsNetworkAF": ruijieWanFpmResultsNetworkAF,
       "ruijieWanFpmResultsSessStatus": ruijieWanFpmResultsSessStatus,
       "ruijieWanFpmResultsLinkQuality": ruijieWanFpmResultsLinkQuality,
       "ruijieWanFpmResultsWorseAction": ruijieWanFpmResultsWorseAction,
       "ruijieWanFpmResultsRTT": ruijieWanFpmResultsRTT,
       "ruijieWanFpmResultsJitter": ruijieWanFpmResultsJitter,
       "ruijieWanFpmResultsUpDroprate": ruijieWanFpmResultsUpDroprate,
       "ruijieWanFpmResultsDownDroprate": ruijieWanFpmResultsDownDroprate,
       "ruijieWanFpmResultsByteTxSpeed": ruijieWanFpmResultsByteTxSpeed,
       "ruijieWanFpmResultsByteRxSpeed": ruijieWanFpmResultsByteRxSpeed,
       "ruijieWanFpmResultsPktsTxSpeed": ruijieWanFpmResultsPktsTxSpeed,
       "ruijieWanFpmResultsPktsRxSpeed": ruijieWanFpmResultsPktsRxSpeed,
       "ruijieWanFpmResultsCresteTime": ruijieWanFpmResultsCresteTime,
       "ruijieWanFpmResultsTrapType": ruijieWanFpmResultsTrapType,
       "ruijieWanFpmResultsSessId": ruijieWanFpmResultsSessId,
       "ruijieWanFpmMonitor": ruijieWanFpmMonitor,
       "ruijieWanFpmMonitorTRAP": ruijieWanFpmMonitorTRAP,
       "ruijieWanFpmNotifications": ruijieWanFpmNotifications,
       "ruijieWanFpmLqWell": ruijieWanFpmLqWell,
       "ruijieWanFpmLqBad": ruijieWanFpmLqBad}
)
