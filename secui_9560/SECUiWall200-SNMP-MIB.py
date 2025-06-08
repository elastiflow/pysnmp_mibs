# SNMP MIB module (SECUiWall200-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/secui_9560/SECUiWall200-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:59:21 2025
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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

secuidotcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9560)
)
if mibBuilder.loadTexts:
    secuidotcom.setRevisions(
        ("2001-05-08 00:00",
         "2001-10-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1)
)
_Firewall_ObjectIdentity = ObjectIdentity
firewall = _Firewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1)
)
_Secuiwall200_ObjectIdentity = ObjectIdentity
secuiwall200 = _Secuiwall200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2)
)
_CounterVars_ObjectIdentity = ObjectIdentity
counterVars = _CounterVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1)
)
_NicTable_Object = MibTable
nicTable = _NicTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nicTable.setStatus("current")
_NicEntry_Object = MibTableRow
nicEntry = _NicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1)
)
nicEntry.setIndexNames(
    (0, "SECUiWall200-SNMP-MIB", "nicIndex"),
)
if mibBuilder.loadTexts:
    nicEntry.setStatus("current")


class _NicIndex_Type(Integer32):
    """Custom type nicIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NicIndex_Type.__name__ = "Integer32"
_NicIndex_Object = MibTableColumn
nicIndex = _NicIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 1),
    _NicIndex_Type()
)
nicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicIndex.setStatus("current")
_NicNames_Type = DisplayString
_NicNames_Object = MibTableColumn
nicNames = _NicNames_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 2),
    _NicNames_Type()
)
nicNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicNames.setStatus("current")
_NicPacketIn_Type = Counter32
_NicPacketIn_Object = MibTableColumn
nicPacketIn = _NicPacketIn_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 3),
    _NicPacketIn_Type()
)
nicPacketIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicPacketIn.setStatus("current")
_NicPacketOut_Type = Counter32
_NicPacketOut_Object = MibTableColumn
nicPacketOut = _NicPacketOut_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 4),
    _NicPacketOut_Type()
)
nicPacketOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicPacketOut.setStatus("current")
_NicByteIn_Type = Counter32
_NicByteIn_Object = MibTableColumn
nicByteIn = _NicByteIn_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 5),
    _NicByteIn_Type()
)
nicByteIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicByteIn.setStatus("current")
_NicByteOut_Type = Counter32
_NicByteOut_Object = MibTableColumn
nicByteOut = _NicByteOut_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 1, 1, 6),
    _NicByteOut_Type()
)
nicByteOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nicByteOut.setStatus("current")
_AdmitRuleTable_Object = MibTable
admitRuleTable = _AdmitRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    admitRuleTable.setStatus("current")
_AdmitRuleEntry_Object = MibTableRow
admitRuleEntry = _AdmitRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1)
)
admitRuleEntry.setIndexNames(
    (0, "SECUiWall200-SNMP-MIB", "admitRuleIndex"),
)
if mibBuilder.loadTexts:
    admitRuleEntry.setStatus("current")


class _AdmitRuleIndex_Type(Integer32):
    """Custom type admitRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdmitRuleIndex_Type.__name__ = "Integer32"
_AdmitRuleIndex_Object = MibTableColumn
admitRuleIndex = _AdmitRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 1),
    _AdmitRuleIndex_Type()
)
admitRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleIndex.setStatus("current")
_AdmitRuleId_Type = Integer32
_AdmitRuleId_Object = MibTableColumn
admitRuleId = _AdmitRuleId_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 2),
    _AdmitRuleId_Type()
)
admitRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleId.setStatus("current")
_AdmitRuleFWNumber_Type = Integer32
_AdmitRuleFWNumber_Object = MibTableColumn
admitRuleFWNumber = _AdmitRuleFWNumber_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 3),
    _AdmitRuleFWNumber_Type()
)
admitRuleFWNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleFWNumber.setStatus("current")
_AdmitRuleFlag_Type = Integer32
_AdmitRuleFlag_Object = MibTableColumn
admitRuleFlag = _AdmitRuleFlag_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 4),
    _AdmitRuleFlag_Type()
)
admitRuleFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleFlag.setStatus("current")
_AdmitRuleUSRNumber_Type = Integer32
_AdmitRuleUSRNumber_Object = MibTableColumn
admitRuleUSRNumber = _AdmitRuleUSRNumber_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 5),
    _AdmitRuleUSRNumber_Type()
)
admitRuleUSRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleUSRNumber.setStatus("current")
_AdmitRuleFlowNumber_Type = Gauge32
_AdmitRuleFlowNumber_Object = MibTableColumn
admitRuleFlowNumber = _AdmitRuleFlowNumber_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 6),
    _AdmitRuleFlowNumber_Type()
)
admitRuleFlowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleFlowNumber.setStatus("current")
_AdmitRulePackets_Type = Counter32
_AdmitRulePackets_Object = MibTableColumn
admitRulePackets = _AdmitRulePackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 7),
    _AdmitRulePackets_Type()
)
admitRulePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRulePackets.setStatus("current")
_AdmitRuleBytes_Type = Counter32
_AdmitRuleBytes_Object = MibTableColumn
admitRuleBytes = _AdmitRuleBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 2, 1, 8),
    _AdmitRuleBytes_Type()
)
admitRuleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    admitRuleBytes.setStatus("current")
_DenyRuleTable_Object = MibTable
denyRuleTable = _DenyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    denyRuleTable.setStatus("current")
_DenyRuleEntry_Object = MibTableRow
denyRuleEntry = _DenyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1)
)
denyRuleEntry.setIndexNames(
    (0, "SECUiWall200-SNMP-MIB", "denyRuleIndex"),
)
if mibBuilder.loadTexts:
    denyRuleEntry.setStatus("current")


class _DenyRuleIndex_Type(Integer32):
    """Custom type denyRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DenyRuleIndex_Type.__name__ = "Integer32"
_DenyRuleIndex_Object = MibTableColumn
denyRuleIndex = _DenyRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 1),
    _DenyRuleIndex_Type()
)
denyRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleIndex.setStatus("current")
_DenyRuleId_Type = Integer32
_DenyRuleId_Object = MibTableColumn
denyRuleId = _DenyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 2),
    _DenyRuleId_Type()
)
denyRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleId.setStatus("current")
_DenyRuleFWNumber_Type = Integer32
_DenyRuleFWNumber_Object = MibTableColumn
denyRuleFWNumber = _DenyRuleFWNumber_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 3),
    _DenyRuleFWNumber_Type()
)
denyRuleFWNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleFWNumber.setStatus("current")
_DenyRuleFlag_Type = Integer32
_DenyRuleFlag_Object = MibTableColumn
denyRuleFlag = _DenyRuleFlag_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 4),
    _DenyRuleFlag_Type()
)
denyRuleFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleFlag.setStatus("current")
_DenyRuleUSRNumber_Type = Integer32
_DenyRuleUSRNumber_Object = MibTableColumn
denyRuleUSRNumber = _DenyRuleUSRNumber_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 5),
    _DenyRuleUSRNumber_Type()
)
denyRuleUSRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleUSRNumber.setStatus("current")
_DenyRulePackets_Type = Counter32
_DenyRulePackets_Object = MibTableColumn
denyRulePackets = _DenyRulePackets_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 6),
    _DenyRulePackets_Type()
)
denyRulePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRulePackets.setStatus("current")
_DenyRuleBytes_Type = Counter32
_DenyRuleBytes_Object = MibTableColumn
denyRuleBytes = _DenyRuleBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 3, 1, 7),
    _DenyRuleBytes_Type()
)
denyRuleBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    denyRuleBytes.setStatus("current")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4)
)
_PacketsHTTP_Type = Counter32
_PacketsHTTP_Object = MibScalar
packetsHTTP = _PacketsHTTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4, 1),
    _PacketsHTTP_Type()
)
packetsHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsHTTP.setStatus("current")
_BytesHTTP_Type = Counter32
_BytesHTTP_Object = MibScalar
bytesHTTP = _BytesHTTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4, 2),
    _BytesHTTP_Type()
)
bytesHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesHTTP.setStatus("current")
_PacketsRHTTP_Type = Counter32
_PacketsRHTTP_Object = MibScalar
packetsRHTTP = _PacketsRHTTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4, 3),
    _PacketsRHTTP_Type()
)
packetsRHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsRHTTP.setStatus("current")
_BytesRHTTP_Type = Counter32
_BytesRHTTP_Object = MibScalar
bytesRHTTP = _BytesRHTTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4, 4),
    _BytesRHTTP_Type()
)
bytesRHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesRHTTP.setStatus("current")
_JavaActiveX_Type = Counter32
_JavaActiveX_Object = MibScalar
javaActiveX = _JavaActiveX_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 4, 5),
    _JavaActiveX_Type()
)
javaActiveX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    javaActiveX.setStatus("current")
_Mail_ObjectIdentity = ObjectIdentity
mail = _Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 5)
)
_SendSMTP_Type = Counter32
_SendSMTP_Object = MibScalar
sendSMTP = _SendSMTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 5, 1),
    _SendSMTP_Type()
)
sendSMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sendSMTP.setStatus("current")
_RecvSMTP_Type = Counter32
_RecvSMTP_Object = MibScalar
recvSMTP = _RecvSMTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 5, 2),
    _RecvSMTP_Type()
)
recvSMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recvSMTP.setStatus("current")
_DropSMTP_Type = Counter32
_DropSMTP_Object = MibScalar
dropSMTP = _DropSMTP_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 5, 3),
    _DropSMTP_Type()
)
dropSMTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dropSMTP.setStatus("current")
_Urlblock_ObjectIdentity = ObjectIdentity
urlblock = _Urlblock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 6)
)
_BlockURL_Type = Counter32
_BlockURL_Object = MibScalar
blockURL = _BlockURL_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 6, 1),
    _BlockURL_Type()
)
blockURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockURL.setStatus("current")
_Resources_ObjectIdentity = ObjectIdentity
resources = _Resources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 7)
)
_CpuUsage_Type = DisplayString
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 7, 1),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_MemUsage_Type = DisplayString
_MemUsage_Object = MibScalar
memUsage = _MemUsage_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 7, 2),
    _MemUsage_Type()
)
memUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsage.setStatus("current")
_TShaperTable_Object = MibTable
tShaperTable = _TShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 8)
)
if mibBuilder.loadTexts:
    tShaperTable.setStatus("current")
_TShaperEntry_Object = MibTableRow
tShaperEntry = _TShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 8, 1)
)
tShaperEntry.setIndexNames(
    (0, "SECUiWall200-SNMP-MIB", "queueIndex"),
)
if mibBuilder.loadTexts:
    tShaperEntry.setStatus("current")


class _TShapeIndex_Type(Integer32):
    """Custom type tShapeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TShapeIndex_Type.__name__ = "Integer32"
_TShapeIndex_Object = MibTableColumn
tShapeIndex = _TShapeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 8, 1, 1),
    _TShapeIndex_Type()
)
tShapeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tShapeIndex.setStatus("current")


class _QueueIndex_Type(Integer32):
    """Custom type queueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QueueIndex_Type.__name__ = "Integer32"
_QueueIndex_Object = MibTableColumn
queueIndex = _QueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 8, 1, 2),
    _QueueIndex_Type()
)
queueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueIndex.setStatus("current")
_QueueBytes_Type = Counter32
_QueueBytes_Object = MibTableColumn
queueBytes = _QueueBytes_Object(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 1, 8, 1, 3),
    _QueueBytes_Type()
)
queueBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueBytes.setStatus("current")
_SecuiwallTraps_ObjectIdentity = ObjectIdentity
secuiwallTraps = _SecuiwallTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 128)
)

# Managed Objects groups


# Notification objects

secuiwallStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 128, 1)
)
if mibBuilder.loadTexts:
    secuiwallStart.setStatus(
        "current"
    )

secuiwallShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 128, 2)
)
if mibBuilder.loadTexts:
    secuiwallShutdown.setStatus(
        "current"
    )

secuiwallAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 128, 3)
)
if mibBuilder.loadTexts:
    secuiwallAlert.setStatus(
        "current"
    )

secuiwallHacking = NotificationType(
    (1, 3, 6, 1, 4, 1, 9560, 1, 1, 2, 128, 4)
)
if mibBuilder.loadTexts:
    secuiwallHacking.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SECUiWall200-SNMP-MIB",
    **{"secuidotcom": secuidotcom,
       "products": products,
       "firewall": firewall,
       "secuiwall200": secuiwall200,
       "counterVars": counterVars,
       "nicTable": nicTable,
       "nicEntry": nicEntry,
       "nicIndex": nicIndex,
       "nicNames": nicNames,
       "nicPacketIn": nicPacketIn,
       "nicPacketOut": nicPacketOut,
       "nicByteIn": nicByteIn,
       "nicByteOut": nicByteOut,
       "admitRuleTable": admitRuleTable,
       "admitRuleEntry": admitRuleEntry,
       "admitRuleIndex": admitRuleIndex,
       "admitRuleId": admitRuleId,
       "admitRuleFWNumber": admitRuleFWNumber,
       "admitRuleFlag": admitRuleFlag,
       "admitRuleUSRNumber": admitRuleUSRNumber,
       "admitRuleFlowNumber": admitRuleFlowNumber,
       "admitRulePackets": admitRulePackets,
       "admitRuleBytes": admitRuleBytes,
       "denyRuleTable": denyRuleTable,
       "denyRuleEntry": denyRuleEntry,
       "denyRuleIndex": denyRuleIndex,
       "denyRuleId": denyRuleId,
       "denyRuleFWNumber": denyRuleFWNumber,
       "denyRuleFlag": denyRuleFlag,
       "denyRuleUSRNumber": denyRuleUSRNumber,
       "denyRulePackets": denyRulePackets,
       "denyRuleBytes": denyRuleBytes,
       "web": web,
       "packetsHTTP": packetsHTTP,
       "bytesHTTP": bytesHTTP,
       "packetsRHTTP": packetsRHTTP,
       "bytesRHTTP": bytesRHTTP,
       "javaActiveX": javaActiveX,
       "mail": mail,
       "sendSMTP": sendSMTP,
       "recvSMTP": recvSMTP,
       "dropSMTP": dropSMTP,
       "urlblock": urlblock,
       "blockURL": blockURL,
       "resources": resources,
       "cpuUsage": cpuUsage,
       "memUsage": memUsage,
       "tShaperTable": tShaperTable,
       "tShaperEntry": tShaperEntry,
       "tShapeIndex": tShapeIndex,
       "queueIndex": queueIndex,
       "queueBytes": queueBytes,
       "secuiwallTraps": secuiwallTraps,
       "secuiwallStart": secuiwallStart,
       "secuiwallShutdown": secuiwallShutdown,
       "secuiwallAlert": secuiwallAlert,
       "secuiwallHacking": secuiwallHacking}
)
