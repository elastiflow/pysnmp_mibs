# SNMP MIB module (WA) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/f5_3375/WA.mib
# Produced by pysmi-1.5.11 at Wed May 21 21:18:56 2025
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

f5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375)
)
if mibBuilder.loadTexts:
    f5.setRevisions(
        ("2007-06-05 16:00",)
    )


# Types definitions


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
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Pvsystem_ObjectIdentity = ObjectIdentity
pvsystem = _Pvsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14)
)
_BasicInfo_ObjectIdentity = ObjectIdentity
basicInfo = _BasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1)
)
_StartTime_Type = OctetString
_StartTime_Object = MibScalar
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 1),
    _StartTime_Type()
)
startTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startTime.setStatus("current")
_BuildVer_Type = OctetString
_BuildVer_Object = MibScalar
buildVer = _BuildVer_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 2),
    _BuildVer_Type()
)
buildVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildVer.setStatus("current")
_BuildLatestLoc_Type = OctetString
_BuildLatestLoc_Object = MibScalar
buildLatestLoc = _BuildLatestLoc_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 3),
    _BuildLatestLoc_Type()
)
buildLatestLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildLatestLoc.setStatus("current")
_BuildLatestGlob_Type = OctetString
_BuildLatestGlob_Object = MibScalar
buildLatestGlob = _BuildLatestGlob_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 4),
    _BuildLatestGlob_Type()
)
buildLatestGlob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildLatestGlob.setStatus("current")
_ConfigVer_Type = OctetString
_ConfigVer_Object = MibScalar
configVer = _ConfigVer_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 5),
    _ConfigVer_Type()
)
configVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVer.setStatus("current")
_LogLevel_Type = Integer32
_LogLevel_Object = MibScalar
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 1, 6),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logLevel.setStatus("current")
_Comm_ObjectIdentity = ObjectIdentity
comm = _Comm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2)
)
_CommSysInfo_ObjectIdentity = ObjectIdentity
commSysInfo = _CommSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1)
)
_ThisNetID_Type = OctetString
_ThisNetID_Object = MibScalar
thisNetID = _ThisNetID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 1),
    _ThisNetID_Type()
)
thisNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thisNetID.setStatus("current")
_InsecurePort_Type = Unsigned32
_InsecurePort_Object = MibScalar
insecurePort = _InsecurePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 2),
    _InsecurePort_Type()
)
insecurePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    insecurePort.setStatus("current")
_SecurePort_Type = Unsigned32
_SecurePort_Object = MibScalar
securePort = _SecurePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 3),
    _SecurePort_Type()
)
securePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securePort.setStatus("current")
_PrimParentNetID_Type = OctetString
_PrimParentNetID_Object = MibScalar
primParentNetID = _PrimParentNetID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 4),
    _PrimParentNetID_Type()
)
primParentNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primParentNetID.setStatus("current")
_ActiveParentNetID_Type = OctetString
_ActiveParentNetID_Object = MibScalar
activeParentNetID = _ActiveParentNetID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 5),
    _ActiveParentNetID_Type()
)
activeParentNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeParentNetID.setStatus("current")


class _NumListenerFD_Type(Unsigned32):
    """Custom type numListenerFD based on Unsigned32"""
    defaultValue = 0


_NumListenerFD_Type.__name__ = "Unsigned32"
_NumListenerFD_Object = MibScalar
numListenerFD = _NumListenerFD_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 6),
    _NumListenerFD_Type()
)
numListenerFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numListenerFD.setStatus("current")


class _MsgQueueDepth_Type(Unsigned32):
    """Custom type msgQueueDepth based on Unsigned32"""
    defaultValue = 0


_MsgQueueDepth_Type.__name__ = "Unsigned32"
_MsgQueueDepth_Object = MibScalar
msgQueueDepth = _MsgQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 7),
    _MsgQueueDepth_Type()
)
msgQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgQueueDepth.setStatus("current")


class _PostQueueDepth_Type(Unsigned32):
    """Custom type postQueueDepth based on Unsigned32"""
    defaultValue = 0


_PostQueueDepth_Type.__name__ = "Unsigned32"
_PostQueueDepth_Object = MibScalar
postQueueDepth = _PostQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 8),
    _PostQueueDepth_Type()
)
postQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postQueueDepth.setStatus("current")
_GroupList_Type = OctetString
_GroupList_Object = MibScalar
groupList = _GroupList_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 9),
    _GroupList_Type()
)
groupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupList.setStatus("current")


class _NumHosts_Type(Unsigned32):
    """Custom type numHosts based on Unsigned32"""
    defaultValue = 0


_NumHosts_Type.__name__ = "Unsigned32"
_NumHosts_Object = MibScalar
numHosts = _NumHosts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 1, 10),
    _NumHosts_Type()
)
numHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHosts.setStatus("current")
_CommMsgCounts_ObjectIdentity = ObjectIdentity
commMsgCounts = _CommMsgCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2)
)


class _NumInfoSent_Type(Unsigned32):
    """Custom type numInfoSent based on Unsigned32"""
    defaultValue = 0


_NumInfoSent_Type.__name__ = "Unsigned32"
_NumInfoSent_Object = MibScalar
numInfoSent = _NumInfoSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 1),
    _NumInfoSent_Type()
)
numInfoSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numInfoSent.setStatus("current")


class _NumInfoRecv_Type(Unsigned32):
    """Custom type numInfoRecv based on Unsigned32"""
    defaultValue = 0


_NumInfoRecv_Type.__name__ = "Unsigned32"
_NumInfoRecv_Object = MibScalar
numInfoRecv = _NumInfoRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 2),
    _NumInfoRecv_Type()
)
numInfoRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numInfoRecv.setStatus("current")


class _NumQuerySent_Type(Unsigned32):
    """Custom type numQuerySent based on Unsigned32"""
    defaultValue = 0


_NumQuerySent_Type.__name__ = "Unsigned32"
_NumQuerySent_Object = MibScalar
numQuerySent = _NumQuerySent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 3),
    _NumQuerySent_Type()
)
numQuerySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numQuerySent.setStatus("current")


class _NumQueryRecv_Type(Unsigned32):
    """Custom type numQueryRecv based on Unsigned32"""
    defaultValue = 0


_NumQueryRecv_Type.__name__ = "Unsigned32"
_NumQueryRecv_Object = MibScalar
numQueryRecv = _NumQueryRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 4),
    _NumQueryRecv_Type()
)
numQueryRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numQueryRecv.setStatus("current")


class _NumReplySent_Type(Unsigned32):
    """Custom type numReplySent based on Unsigned32"""
    defaultValue = 0


_NumReplySent_Type.__name__ = "Unsigned32"
_NumReplySent_Object = MibScalar
numReplySent = _NumReplySent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 5),
    _NumReplySent_Type()
)
numReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numReplySent.setStatus("current")


class _NumReplyRecv_Type(Unsigned32):
    """Custom type numReplyRecv based on Unsigned32"""
    defaultValue = 0


_NumReplyRecv_Type.__name__ = "Unsigned32"
_NumReplyRecv_Object = MibScalar
numReplyRecv = _NumReplyRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 6),
    _NumReplyRecv_Type()
)
numReplyRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numReplyRecv.setStatus("current")


class _NumHealthSent_Type(Unsigned32):
    """Custom type numHealthSent based on Unsigned32"""
    defaultValue = 0


_NumHealthSent_Type.__name__ = "Unsigned32"
_NumHealthSent_Object = MibScalar
numHealthSent = _NumHealthSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 7),
    _NumHealthSent_Type()
)
numHealthSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHealthSent.setStatus("current")


class _NumHealthRecv_Type(Unsigned32):
    """Custom type numHealthRecv based on Unsigned32"""
    defaultValue = 0


_NumHealthRecv_Type.__name__ = "Unsigned32"
_NumHealthRecv_Object = MibScalar
numHealthRecv = _NumHealthRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 8),
    _NumHealthRecv_Type()
)
numHealthRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHealthRecv.setStatus("current")


class _NumAckSent_Type(Unsigned32):
    """Custom type numAckSent based on Unsigned32"""
    defaultValue = 0


_NumAckSent_Type.__name__ = "Unsigned32"
_NumAckSent_Object = MibScalar
numAckSent = _NumAckSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 9),
    _NumAckSent_Type()
)
numAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAckSent.setStatus("current")


class _NumAckRecv_Type(Unsigned32):
    """Custom type numAckRecv based on Unsigned32"""
    defaultValue = 0


_NumAckRecv_Type.__name__ = "Unsigned32"
_NumAckRecv_Object = MibScalar
numAckRecv = _NumAckRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 10),
    _NumAckRecv_Type()
)
numAckRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numAckRecv.setStatus("current")


class _NumFileSndSent_Type(Unsigned32):
    """Custom type numFileSndSent based on Unsigned32"""
    defaultValue = 0


_NumFileSndSent_Type.__name__ = "Unsigned32"
_NumFileSndSent_Object = MibScalar
numFileSndSent = _NumFileSndSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 11),
    _NumFileSndSent_Type()
)
numFileSndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFileSndSent.setStatus("current")


class _NumFileSndRecv_Type(Unsigned32):
    """Custom type numFileSndRecv based on Unsigned32"""
    defaultValue = 0


_NumFileSndRecv_Type.__name__ = "Unsigned32"
_NumFileSndRecv_Object = MibScalar
numFileSndRecv = _NumFileSndRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 12),
    _NumFileSndRecv_Type()
)
numFileSndRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFileSndRecv.setStatus("current")


class _NumFileRecSent_Type(Unsigned32):
    """Custom type numFileRecSent based on Unsigned32"""
    defaultValue = 0


_NumFileRecSent_Type.__name__ = "Unsigned32"
_NumFileRecSent_Object = MibScalar
numFileRecSent = _NumFileRecSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 13),
    _NumFileRecSent_Type()
)
numFileRecSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFileRecSent.setStatus("current")


class _NumFileRecRecv_Type(Unsigned32):
    """Custom type numFileRecRecv based on Unsigned32"""
    defaultValue = 0


_NumFileRecRecv_Type.__name__ = "Unsigned32"
_NumFileRecRecv_Object = MibScalar
numFileRecRecv = _NumFileRecRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 14),
    _NumFileRecRecv_Type()
)
numFileRecRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFileRecRecv.setStatus("current")


class _NumDupRecv_Type(Unsigned32):
    """Custom type numDupRecv based on Unsigned32"""
    defaultValue = 0


_NumDupRecv_Type.__name__ = "Unsigned32"
_NumDupRecv_Object = MibScalar
numDupRecv = _NumDupRecv_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 15),
    _NumDupRecv_Type()
)
numDupRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDupRecv.setStatus("current")


class _NumExpired_Type(Unsigned32):
    """Custom type numExpired based on Unsigned32"""
    defaultValue = 0


_NumExpired_Type.__name__ = "Unsigned32"
_NumExpired_Object = MibScalar
numExpired = _NumExpired_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 2, 16),
    _NumExpired_Type()
)
numExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numExpired.setStatus("current")
_CommConnInfoTable_Object = MibTable
commConnInfoTable = _CommConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3)
)
if mibBuilder.loadTexts:
    commConnInfoTable.setStatus("current")
_CommConnInfoEntry_Object = MibTableRow
commConnInfoEntry = _CommConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1)
)
commConnInfoEntry.setIndexNames(
    (0, "WA", "connNetID"),
    (0, "WA", "connIpAddr"),
    (0, "WA", "connPortNum"),
    (0, "WA", "connLastContactTime"),
    (0, "WA", "connGroupUpList"),
    (0, "WA", "connGroupDownList"),
    (0, "WA", "connSendFailNum"),
    (0, "WA", "connHostType"),
    (0, "WA", "connAltList"),
)
if mibBuilder.loadTexts:
    commConnInfoEntry.setStatus("current")
_ConnNetID_Type = OctetString
_ConnNetID_Object = MibTableColumn
connNetID = _ConnNetID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 1),
    _ConnNetID_Type()
)
connNetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connNetID.setStatus("current")
_ConnIpAddr_Type = OctetString
_ConnIpAddr_Object = MibTableColumn
connIpAddr = _ConnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 2),
    _ConnIpAddr_Type()
)
connIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connIpAddr.setStatus("current")
_ConnPortNum_Type = Unsigned32
_ConnPortNum_Object = MibTableColumn
connPortNum = _ConnPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 3),
    _ConnPortNum_Type()
)
connPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connPortNum.setStatus("current")
_ConnLastContactTime_Type = OctetString
_ConnLastContactTime_Object = MibTableColumn
connLastContactTime = _ConnLastContactTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 4),
    _ConnLastContactTime_Type()
)
connLastContactTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connLastContactTime.setStatus("current")
_ConnGroupUpList_Type = OctetString
_ConnGroupUpList_Object = MibTableColumn
connGroupUpList = _ConnGroupUpList_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 5),
    _ConnGroupUpList_Type()
)
connGroupUpList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connGroupUpList.setStatus("current")
_ConnGroupDownList_Type = OctetString
_ConnGroupDownList_Object = MibTableColumn
connGroupDownList = _ConnGroupDownList_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 6),
    _ConnGroupDownList_Type()
)
connGroupDownList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connGroupDownList.setStatus("current")
_ConnSendFailNum_Type = Unsigned32
_ConnSendFailNum_Object = MibTableColumn
connSendFailNum = _ConnSendFailNum_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 7),
    _ConnSendFailNum_Type()
)
connSendFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connSendFailNum.setStatus("current")
_ConnHostType_Type = OctetString
_ConnHostType_Object = MibTableColumn
connHostType = _ConnHostType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 8),
    _ConnHostType_Type()
)
connHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connHostType.setStatus("current")
_ConnAltList_Type = OctetString
_ConnAltList_Object = MibTableColumn
connAltList = _ConnAltList_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 2, 3, 1, 9),
    _ConnAltList_Type()
)
connAltList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connAltList.setStatus("current")
_Pvac_ObjectIdentity = ObjectIdentity
pvac = _Pvac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4)
)
_PvacSysInfo_ObjectIdentity = ObjectIdentity
pvacSysInfo = _PvacSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1)
)
_NumActiveThreads_Type = Unsigned32
_NumActiveThreads_Object = MibScalar
numActiveThreads = _NumActiveThreads_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 1),
    _NumActiveThreads_Type()
)
numActiveThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActiveThreads.setStatus("current")
_NumReqAccepted_Type = Counter64
_NumReqAccepted_Object = MibScalar
numReqAccepted = _NumReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 2),
    _NumReqAccepted_Type()
)
numReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numReqAccepted.setStatus("current")
_NumPendingReq_Type = Unsigned32
_NumPendingReq_Object = MibScalar
numPendingReq = _NumPendingReq_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 3),
    _NumPendingReq_Type()
)
numPendingReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPendingReq.setStatus("current")
_SharedFlags_Type = OctetString
_SharedFlags_Object = MibScalar
sharedFlags = _SharedFlags_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 4),
    _SharedFlags_Type()
)
sharedFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sharedFlags.setStatus("current")
_NumActiveConn_Type = Unsigned32
_NumActiveConn_Object = MibScalar
numActiveConn = _NumActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 5),
    _NumActiveConn_Type()
)
numActiveConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActiveConn.setStatus("current")
_NumReqRejected_Type = Counter64
_NumReqRejected_Object = MibScalar
numReqRejected = _NumReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 6),
    _NumReqRejected_Type()
)
numReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numReqRejected.setStatus("current")
_ProxyServerAvailable_Type = Unsigned32
_ProxyServerAvailable_Object = MibScalar
proxyServerAvailable = _ProxyServerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 7),
    _ProxyServerAvailable_Type()
)
proxyServerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyServerAvailable.setStatus("current")
_NumRespServed_Type = Counter64
_NumRespServed_Object = MibScalar
numRespServed = _NumRespServed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 1, 8),
    _NumRespServed_Type()
)
numRespServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numRespServed.setStatus("current")
_PvacCustomerInfoTable_Object = MibTable
pvacCustomerInfoTable = _PvacCustomerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2)
)
if mibBuilder.loadTexts:
    pvacCustomerInfoTable.setStatus("current")
_PvacCustomerInfoEntry_Object = MibTableRow
pvacCustomerInfoEntry = _PvacCustomerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1)
)
pvacCustomerInfoEntry.setIndexNames(
    (0, "WA", "cusName"),
    (0, "WA", "cusId"),
    (0, "WA", "stagVerNum"),
    (0, "WA", "stagLogCount"),
    (0, "WA", "stagLogLineCount"),
    (0, "WA", "liveVerNum"),
    (0, "WA", "liveLogCount"),
    (0, "WA", "liveLogLineCount"),
)
if mibBuilder.loadTexts:
    pvacCustomerInfoEntry.setStatus("current")
_CusName_Type = OctetString
_CusName_Object = MibTableColumn
cusName = _CusName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1, 1),
    _CusName_Type()
)
cusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cusName.setStatus("current")
_CusId_Type = Counter64
_CusId_Object = MibTableColumn
cusId = _CusId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1, 2),
    _CusId_Type()
)
cusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cusId.setStatus("current")
_VerNum_Type = Counter64
_VerNum_Object = MibScalar
verNum = _VerNum_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1, 3),
    _VerNum_Type()
)
verNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    verNum.setStatus("current")
_LogCount_Type = Counter64
_LogCount_Object = MibScalar
logCount = _LogCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1, 4),
    _LogCount_Type()
)
logCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCount.setStatus("current")
_LogLineCount_Type = Counter64
_LogLineCount_Object = MibScalar
logLineCount = _LogLineCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 2, 1, 5),
    _LogLineCount_Type()
)
logLineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logLineCount.setStatus("current")
_PvacCacheStats_ObjectIdentity = ObjectIdentity
pvacCacheStats = _PvacCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3)
)
_ProxyCount_Type = Unsigned32
_ProxyCount_Object = MibScalar
proxyCount = _ProxyCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 1),
    _ProxyCount_Type()
)
proxyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyCount.setStatus("current")
_ImcHitCount_Type = Unsigned32
_ImcHitCount_Object = MibScalar
imcHitCount = _ImcHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 2),
    _ImcHitCount_Type()
)
imcHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imcHitCount.setStatus("current")
_HdsHitCount_Type = Unsigned32
_HdsHitCount_Object = MibScalar
hdsHitCount = _HdsHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 3),
    _HdsHitCount_Type()
)
hdsHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdsHitCount.setStatus("current")
_NumActiveParses_Type = Unsigned32
_NumActiveParses_Object = MibScalar
numActiveParses = _NumActiveParses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 4),
    _NumActiveParses_Type()
)
numActiveParses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActiveParses.setStatus("current")
_NumActiveProxies_Type = Unsigned32
_NumActiveProxies_Object = MibScalar
numActiveProxies = _NumActiveProxies_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 5),
    _NumActiveProxies_Type()
)
numActiveProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActiveProxies.setStatus("current")
_SizeCompileQueue_Type = Counter64
_SizeCompileQueue_Object = MibScalar
sizeCompileQueue = _SizeCompileQueue_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 6),
    _SizeCompileQueue_Type()
)
sizeCompileQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeCompileQueue.setStatus("current")
_SizeEsiCompileQueue_Type = Counter64
_SizeEsiCompileQueue_Object = MibScalar
sizeEsiCompileQueue = _SizeEsiCompileQueue_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 7),
    _SizeEsiCompileQueue_Type()
)
sizeEsiCompileQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeEsiCompileQueue.setStatus("current")
_SizeAssembleQueue_Type = Counter64
_SizeAssembleQueue_Object = MibScalar
sizeAssembleQueue = _SizeAssembleQueue_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 8),
    _SizeAssembleQueue_Type()
)
sizeAssembleQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeAssembleQueue.setStatus("current")
_NumPendingProxies_Type = Unsigned32
_NumPendingProxies_Object = MibScalar
numPendingProxies = _NumPendingProxies_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 3, 9),
    _NumPendingProxies_Type()
)
numPendingProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPendingProxies.setStatus("current")
_PvacImc_ObjectIdentity = ObjectIdentity
pvacImc = _PvacImc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4)
)
_PvacImcBasic_ObjectIdentity = ObjectIdentity
pvacImcBasic = _PvacImcBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 1)
)
_MaxItemSize_Type = Unsigned32
_MaxItemSize_Object = MibScalar
maxItemSize = _MaxItemSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 1, 1),
    _MaxItemSize_Type()
)
maxItemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxItemSize.setStatus("current")
_NumPoolPops_Type = Unsigned32
_NumPoolPops_Object = MibScalar
numPoolPops = _NumPoolPops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 1, 2),
    _NumPoolPops_Type()
)
numPoolPops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPoolPops.setStatus("current")
_NumPoolPushes_Type = Unsigned32
_NumPoolPushes_Object = MibScalar
numPoolPushes = _NumPoolPushes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 1, 3),
    _NumPoolPushes_Type()
)
numPoolPushes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPoolPushes.setStatus("current")
_NumHitDrop_Type = Unsigned32
_NumHitDrop_Object = MibScalar
numHitDrop = _NumHitDrop_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 1, 4),
    _NumHitDrop_Type()
)
numHitDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHitDrop.setStatus("current")
_PvacImcConfig_ObjectIdentity = ObjectIdentity
pvacImcConfig = _PvacImcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2)
)
_ConfigBuckets_Type = Unsigned32
_ConfigBuckets_Object = MibScalar
configBuckets = _ConfigBuckets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2, 1),
    _ConfigBuckets_Type()
)
configBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configBuckets.setStatus("current")
_ConfigMutexes_Type = Unsigned32
_ConfigMutexes_Object = MibScalar
configMutexes = _ConfigMutexes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2, 2),
    _ConfigMutexes_Type()
)
configMutexes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMutexes.setStatus("current")
_ConfigScrubSleep_Type = Unsigned32
_ConfigScrubSleep_Object = MibScalar
configScrubSleep = _ConfigScrubSleep_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2, 3),
    _ConfigScrubSleep_Type()
)
configScrubSleep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configScrubSleep.setStatus("current")
_ConfigFootprint_Type = Unsigned32
_ConfigFootprint_Object = MibScalar
configFootprint = _ConfigFootprint_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2, 4),
    _ConfigFootprint_Type()
)
configFootprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFootprint.setStatus("current")
_ConfigMaxItem_Type = Unsigned32
_ConfigMaxItem_Object = MibScalar
configMaxItem = _ConfigMaxItem_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 2, 5),
    _ConfigMaxItem_Type()
)
configMaxItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMaxItem.setStatus("current")
_PvacImcScrub_ObjectIdentity = ObjectIdentity
pvacImcScrub = _PvacImcScrub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3)
)
_ScrubTime_Type = Counter64
_ScrubTime_Object = MibScalar
scrubTime = _ScrubTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3, 1),
    _ScrubTime_Type()
)
scrubTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrubTime.setStatus("current")
_ScrubVarianceSums_Type = OctetString
_ScrubVarianceSums_Object = MibScalar
scrubVarianceSums = _ScrubVarianceSums_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3, 2),
    _ScrubVarianceSums_Type()
)
scrubVarianceSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrubVarianceSums.setStatus("current")
_ScrubVisitCount_Type = Unsigned32
_ScrubVisitCount_Object = MibScalar
scrubVisitCount = _ScrubVisitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3, 3),
    _ScrubVisitCount_Type()
)
scrubVisitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrubVisitCount.setStatus("current")
_ScrubHitCount_Type = Unsigned32
_ScrubHitCount_Object = MibScalar
scrubHitCount = _ScrubHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3, 4),
    _ScrubHitCount_Type()
)
scrubHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrubHitCount.setStatus("current")
_ScrubMissCount_Type = Unsigned32
_ScrubMissCount_Object = MibScalar
scrubMissCount = _ScrubMissCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 3, 5),
    _ScrubMissCount_Type()
)
scrubMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrubMissCount.setStatus("current")
_PvacImcMemCache_ObjectIdentity = ObjectIdentity
pvacImcMemCache = _PvacImcMemCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4)
)
_LruLength_Type = Unsigned32
_LruLength_Object = MibScalar
lruLength = _LruLength_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 1),
    _LruLength_Type()
)
lruLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruLength.setStatus("current")
_LruItemBulk_Type = Unsigned32
_LruItemBulk_Object = MibScalar
lruItemBulk = _LruItemBulk_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 2),
    _LruItemBulk_Type()
)
lruItemBulk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruItemBulk.setStatus("current")
_LruHits_Type = Unsigned32
_LruHits_Object = MibScalar
lruHits = _LruHits_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 3),
    _LruHits_Type()
)
lruHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruHits.setStatus("current")
_LruAdds_Type = Unsigned32
_LruAdds_Object = MibScalar
lruAdds = _LruAdds_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 4),
    _LruAdds_Type()
)
lruAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruAdds.setStatus("current")
_LruCuts_Type = Unsigned32
_LruCuts_Object = MibScalar
lruCuts = _LruCuts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 5),
    _LruCuts_Type()
)
lruCuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruCuts.setStatus("current")
_LruDups_Type = Unsigned32
_LruDups_Object = MibScalar
lruDups = _LruDups_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 6),
    _LruDups_Type()
)
lruDups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruDups.setStatus("current")
_LruPops_Type = Unsigned32
_LruPops_Object = MibScalar
lruPops = _LruPops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 4, 4, 7),
    _LruPops_Type()
)
lruPops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lruPops.setStatus("current")
_PvacChangeLogStats_ObjectIdentity = ObjectIdentity
pvacChangeLogStats = _PvacChangeLogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 5)
)
_ChangeLogRecordCount_Type = Counter64
_ChangeLogRecordCount_Object = MibScalar
changeLogRecordCount = _ChangeLogRecordCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 5, 1),
    _ChangeLogRecordCount_Type()
)
changeLogRecordCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changeLogRecordCount.setStatus("current")
_SumOfCounts_Type = Counter64
_SumOfCounts_Object = MibScalar
sumOfCounts = _SumOfCounts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 5, 2),
    _SumOfCounts_Type()
)
sumOfCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sumOfCounts.setStatus("current")
_ChangeLogFileCount_Type = Counter64
_ChangeLogFileCount_Object = MibScalar
changeLogFileCount = _ChangeLogFileCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 4, 5, 3),
    _ChangeLogFileCount_Type()
)
changeLogFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    changeLogFileCount.setStatus("current")
_Errors_ObjectIdentity = ObjectIdentity
errors = _Errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6)
)
_ErrorStatsInfoTable_Object = MibTable
errorStatsInfoTable = _ErrorStatsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6, 1)
)
if mibBuilder.loadTexts:
    errorStatsInfoTable.setStatus("current")
_ErrorStatsInfoEntry_Object = MibTableRow
errorStatsInfoEntry = _ErrorStatsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6, 1, 1)
)
errorStatsInfoEntry.setIndexNames(
    (0, "WA", "errorCode"),
    (0, "WA", "errorCount"),
    (0, "WA", "errorDesc"),
)
if mibBuilder.loadTexts:
    errorStatsInfoEntry.setStatus("current")
_ErrorCode_Type = Counter64
_ErrorCode_Object = MibTableColumn
errorCode = _ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6, 1, 1, 1),
    _ErrorCode_Type()
)
errorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCode.setStatus("current")
_ErrorCount_Type = Counter64
_ErrorCount_Object = MibTableColumn
errorCount = _ErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6, 1, 1, 2),
    _ErrorCount_Type()
)
errorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCount.setStatus("current")
_ErrorDesc_Type = OctetString
_ErrorDesc_Object = MibTableColumn
errorDesc = _ErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 6, 1, 1, 3),
    _ErrorDesc_Type()
)
errorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDesc.setStatus("current")
_JavaInfo_ObjectIdentity = ObjectIdentity
javaInfo = _JavaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 7)
)
_JavaII_ObjectIdentity = ObjectIdentity
javaII = _JavaII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 14, 7, 1)
)
_InvHashCount_Type = Unsigned32
_InvHashCount_Object = MibScalar
invHashCount = _InvHashCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 14, 7, 1, 1),
    _InvHashCount_Type()
)
invHashCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHashCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WA",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "f5": f5,
       "pvsystem": pvsystem,
       "basicInfo": basicInfo,
       "startTime": startTime,
       "buildVer": buildVer,
       "buildLatestLoc": buildLatestLoc,
       "buildLatestGlob": buildLatestGlob,
       "configVer": configVer,
       "logLevel": logLevel,
       "comm": comm,
       "commSysInfo": commSysInfo,
       "thisNetID": thisNetID,
       "insecurePort": insecurePort,
       "securePort": securePort,
       "primParentNetID": primParentNetID,
       "activeParentNetID": activeParentNetID,
       "numListenerFD": numListenerFD,
       "msgQueueDepth": msgQueueDepth,
       "postQueueDepth": postQueueDepth,
       "groupList": groupList,
       "numHosts": numHosts,
       "commMsgCounts": commMsgCounts,
       "numInfoSent": numInfoSent,
       "numInfoRecv": numInfoRecv,
       "numQuerySent": numQuerySent,
       "numQueryRecv": numQueryRecv,
       "numReplySent": numReplySent,
       "numReplyRecv": numReplyRecv,
       "numHealthSent": numHealthSent,
       "numHealthRecv": numHealthRecv,
       "numAckSent": numAckSent,
       "numAckRecv": numAckRecv,
       "numFileSndSent": numFileSndSent,
       "numFileSndRecv": numFileSndRecv,
       "numFileRecSent": numFileRecSent,
       "numFileRecRecv": numFileRecRecv,
       "numDupRecv": numDupRecv,
       "numExpired": numExpired,
       "commConnInfoTable": commConnInfoTable,
       "commConnInfoEntry": commConnInfoEntry,
       "connNetID": connNetID,
       "connIpAddr": connIpAddr,
       "connPortNum": connPortNum,
       "connLastContactTime": connLastContactTime,
       "connGroupUpList": connGroupUpList,
       "connGroupDownList": connGroupDownList,
       "connSendFailNum": connSendFailNum,
       "connHostType": connHostType,
       "connAltList": connAltList,
       "pvac": pvac,
       "pvacSysInfo": pvacSysInfo,
       "numActiveThreads": numActiveThreads,
       "numReqAccepted": numReqAccepted,
       "numPendingReq": numPendingReq,
       "sharedFlags": sharedFlags,
       "numActiveConn": numActiveConn,
       "numReqRejected": numReqRejected,
       "proxyServerAvailable": proxyServerAvailable,
       "numRespServed": numRespServed,
       "pvacCustomerInfoTable": pvacCustomerInfoTable,
       "pvacCustomerInfoEntry": pvacCustomerInfoEntry,
       "cusName": cusName,
       "cusId": cusId,
       "verNum": verNum,
       "logCount": logCount,
       "logLineCount": logLineCount,
       "pvacCacheStats": pvacCacheStats,
       "proxyCount": proxyCount,
       "imcHitCount": imcHitCount,
       "hdsHitCount": hdsHitCount,
       "numActiveParses": numActiveParses,
       "numActiveProxies": numActiveProxies,
       "sizeCompileQueue": sizeCompileQueue,
       "sizeEsiCompileQueue": sizeEsiCompileQueue,
       "sizeAssembleQueue": sizeAssembleQueue,
       "numPendingProxies": numPendingProxies,
       "pvacImc": pvacImc,
       "pvacImcBasic": pvacImcBasic,
       "maxItemSize": maxItemSize,
       "numPoolPops": numPoolPops,
       "numPoolPushes": numPoolPushes,
       "numHitDrop": numHitDrop,
       "pvacImcConfig": pvacImcConfig,
       "configBuckets": configBuckets,
       "configMutexes": configMutexes,
       "configScrubSleep": configScrubSleep,
       "configFootprint": configFootprint,
       "configMaxItem": configMaxItem,
       "pvacImcScrub": pvacImcScrub,
       "scrubTime": scrubTime,
       "scrubVarianceSums": scrubVarianceSums,
       "scrubVisitCount": scrubVisitCount,
       "scrubHitCount": scrubHitCount,
       "scrubMissCount": scrubMissCount,
       "pvacImcMemCache": pvacImcMemCache,
       "lruLength": lruLength,
       "lruItemBulk": lruItemBulk,
       "lruHits": lruHits,
       "lruAdds": lruAdds,
       "lruCuts": lruCuts,
       "lruDups": lruDups,
       "lruPops": lruPops,
       "pvacChangeLogStats": pvacChangeLogStats,
       "changeLogRecordCount": changeLogRecordCount,
       "sumOfCounts": sumOfCounts,
       "changeLogFileCount": changeLogFileCount,
       "errors": errors,
       "errorStatsInfoTable": errorStatsInfoTable,
       "errorStatsInfoEntry": errorStatsInfoEntry,
       "errorCode": errorCode,
       "errorCount": errorCount,
       "errorDesc": errorDesc,
       "javaInfo": javaInfo,
       "javaII": javaII,
       "invHashCount": invHashCount}
)
