# SNMP MIB module (OTA-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/idemia_39999/OTA-PLATFORM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:47:54 2025
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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")


# MODULE-IDENTITY

ota_oberthur = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39999)
)
if mibBuilder.loadTexts:
    ota_oberthur.setRevisions(
        ("2016-03-08 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Jboss_ObjectIdentity = ObjectIdentity
jboss = _Jboss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 1)
)
_ActiveThreadCount_Type = Integer32
_ActiveThreadCount_Object = MibScalar
activeThreadCount = _ActiveThreadCount_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 10),
    _ActiveThreadCount_Type()
)
activeThreadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreadCount.setStatus("current")
_FreeMemory_Type = Gauge32
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 12),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("current")
_MaxMemory_Type = Gauge32
_MaxMemory_Object = MibScalar
maxMemory = _MaxMemory_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 13),
    _MaxMemory_Type()
)
maxMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxMemory.setStatus("current")
_ThreadPoolQueueSize_Type = Integer32
_ThreadPoolQueueSize_Object = MibScalar
threadPoolQueueSize = _ThreadPoolQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 14),
    _ThreadPoolQueueSize_Type()
)
threadPoolQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadPoolQueueSize.setStatus("current")
_RequestCount8080_Type = Gauge32
_RequestCount8080_Object = MibScalar
requestCount8080 = _RequestCount8080_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 15),
    _RequestCount8080_Type()
)
requestCount8080.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requestCount8080.setStatus("current")
_TxCommitCount_Type = Gauge32
_TxCommitCount_Object = MibScalar
txCommitCount = _TxCommitCount_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 16),
    _TxCommitCount_Type()
)
txCommitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCommitCount.setStatus("current")
_TxRollbackCount_Type = Gauge32
_TxRollbackCount_Object = MibScalar
txRollbackCount = _TxRollbackCount_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 17),
    _TxRollbackCount_Type()
)
txRollbackCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txRollbackCount.setStatus("current")
_TxActiveCount_Type = Gauge32
_TxActiveCount_Object = MibScalar
txActiveCount = _TxActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 18),
    _TxActiveCount_Type()
)
txActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txActiveCount.setStatus("current")
_DbInUseConnection_Type = Gauge32
_DbInUseConnection_Object = MibScalar
dbInUseConnection = _DbInUseConnection_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 19),
    _DbInUseConnection_Type()
)
dbInUseConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbInUseConnection.setStatus("current")
_DbMaxConnectionsInUse_Type = Gauge32
_DbMaxConnectionsInUse_Object = MibScalar
dbMaxConnectionsInUse = _DbMaxConnectionsInUse_Object(
    (1, 3, 6, 1, 4, 1, 39999, 1, 20),
    _DbMaxConnectionsInUse_Type()
)
dbMaxConnectionsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dbMaxConnectionsInUse.setStatus("current")
_Urls_ObjectIdentity = ObjectIdentity
urls = _Urls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 2)
)
_Webapps_Object = MibTable
webapps = _Webapps_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1)
)
if mibBuilder.loadTexts:
    webapps.setStatus("current")
_Contentroot_Object = MibTableRow
contentroot = _Contentroot_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1, 1)
)
contentroot.setIndexNames(
    (0, "OTA-PLATFORM-MIB", "webObjectName"),
)
if mibBuilder.loadTexts:
    contentroot.setStatus("current")
_WebObjectName_Type = DisplayString
_WebObjectName_Object = MibTableColumn
webObjectName = _WebObjectName_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1, 1, 2),
    _WebObjectName_Type()
)
webObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webObjectName.setStatus("current")
_WebDistributable_Type = Integer32
_WebDistributable_Object = MibTableColumn
webDistributable = _WebDistributable_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1, 1, 3),
    _WebDistributable_Type()
)
webDistributable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webDistributable.setStatus("current")
_WebSessionCounter_Type = Integer32
_WebSessionCounter_Object = MibTableColumn
webSessionCounter = _WebSessionCounter_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1, 1, 4),
    _WebSessionCounter_Type()
)
webSessionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webSessionCounter.setStatus("current")
_WebActiveSessions_Type = Integer32
_WebActiveSessions_Object = MibTableColumn
webActiveSessions = _WebActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 39999, 2, 1, 1, 5),
    _WebActiveSessions_Type()
)
webActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webActiveSessions.setStatus("current")
_Otaplatform_ObjectIdentity = ObjectIdentity
otaplatform = _Otaplatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 3)
)
_Smsc_ObjectIdentity = ObjectIdentity
smsc = _Smsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2)
)
_SmscTable_Object = MibTable
smscTable = _SmscTable_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1)
)
if mibBuilder.loadTexts:
    smscTable.setStatus("current")
_SmscEntry_Object = MibTableRow
smscEntry = _SmscEntry_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1)
)
smscEntry.setIndexNames(
    (0, "OTA-PLATFORM-MIB", "smscName"),
)
if mibBuilder.loadTexts:
    smscEntry.setStatus("current")
_SmscSeqNumber_Type = DisplayString
_SmscSeqNumber_Object = MibTableColumn
smscSeqNumber = _SmscSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 2),
    _SmscSeqNumber_Type()
)
smscSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscSeqNumber.setStatus("current")
_SmscSeverity_Type = DisplayString
_SmscSeverity_Object = MibTableColumn
smscSeverity = _SmscSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 3),
    _SmscSeverity_Type()
)
smscSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscSeverity.setStatus("current")
_SmscName_Type = DisplayString
_SmscName_Object = MibTableColumn
smscName = _SmscName_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 4),
    _SmscName_Type()
)
smscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscName.setStatus("current")
_SmscMsg_Type = DisplayString
_SmscMsg_Object = MibTableColumn
smscMsg = _SmscMsg_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 5),
    _SmscMsg_Type()
)
smscMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscMsg.setStatus("current")
_SmscIp_Type = DisplayString
_SmscIp_Object = MibTableColumn
smscIp = _SmscIp_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 6),
    _SmscIp_Type()
)
smscIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscIp.setStatus("current")
_SmscTimeStamp_Type = DisplayString
_SmscTimeStamp_Object = MibTableColumn
smscTimeStamp = _SmscTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 1, 1, 7),
    _SmscTimeStamp_Type()
)
smscTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscTimeStamp.setStatus("current")
_Smscgroup_ObjectIdentity = ObjectIdentity
smscgroup = _Smscgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3)
)
_SmscGroupTable_Object = MibTable
smscGroupTable = _SmscGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1)
)
if mibBuilder.loadTexts:
    smscGroupTable.setStatus("current")
_SmscGroupEntry_Object = MibTableRow
smscGroupEntry = _SmscGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1)
)
smscGroupEntry.setIndexNames(
    (0, "OTA-PLATFORM-MIB", "smscGroupName"),
)
if mibBuilder.loadTexts:
    smscGroupEntry.setStatus("current")
_SmscGroupSeqNumber_Type = DisplayString
_SmscGroupSeqNumber_Object = MibTableColumn
smscGroupSeqNumber = _SmscGroupSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1, 2),
    _SmscGroupSeqNumber_Type()
)
smscGroupSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscGroupSeqNumber.setStatus("current")
_SmscGroupSeverity_Type = DisplayString
_SmscGroupSeverity_Object = MibTableColumn
smscGroupSeverity = _SmscGroupSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1, 3),
    _SmscGroupSeverity_Type()
)
smscGroupSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscGroupSeverity.setStatus("current")
_SmscGroupName_Type = DisplayString
_SmscGroupName_Object = MibTableColumn
smscGroupName = _SmscGroupName_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1, 4),
    _SmscGroupName_Type()
)
smscGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscGroupName.setStatus("current")
_SmscGroupMsg_Type = DisplayString
_SmscGroupMsg_Object = MibTableColumn
smscGroupMsg = _SmscGroupMsg_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1, 5),
    _SmscGroupMsg_Type()
)
smscGroupMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscGroupMsg.setStatus("current")
_SmscGroupTimeStamp_Type = DisplayString
_SmscGroupTimeStamp_Object = MibTableColumn
smscGroupTimeStamp = _SmscGroupTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 1, 1, 6),
    _SmscGroupTimeStamp_Type()
)
smscGroupTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smscGroupTimeStamp.setStatus("current")
_Msgdiscriminator_ObjectIdentity = ObjectIdentity
msgdiscriminator = _Msgdiscriminator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4)
)
_MsgDiscriminatorTable_Object = MibTable
msgDiscriminatorTable = _MsgDiscriminatorTable_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1)
)
if mibBuilder.loadTexts:
    msgDiscriminatorTable.setStatus("current")
_MsgDiscriminatorEntry_Object = MibTableRow
msgDiscriminatorEntry = _MsgDiscriminatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1)
)
msgDiscriminatorEntry.setIndexNames(
    (0, "OTA-PLATFORM-MIB", "msgSeqNumber"),
)
if mibBuilder.loadTexts:
    msgDiscriminatorEntry.setStatus("current")
_MsgSeqNumber_Type = DisplayString
_MsgSeqNumber_Object = MibTableColumn
msgSeqNumber = _MsgSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1, 2),
    _MsgSeqNumber_Type()
)
msgSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgSeqNumber.setStatus("current")
_MsgSeverity_Type = DisplayString
_MsgSeverity_Object = MibTableColumn
msgSeverity = _MsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1, 3),
    _MsgSeverity_Type()
)
msgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgSeverity.setStatus("current")
_MsgName_Type = DisplayString
_MsgName_Object = MibTableColumn
msgName = _MsgName_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1, 4),
    _MsgName_Type()
)
msgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgName.setStatus("current")
_Msg_Type = DisplayString
_Msg_Object = MibTableColumn
msg = _Msg_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1, 5),
    _Msg_Type()
)
msg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msg.setStatus("current")
_MsgTimeStamp_Type = DisplayString
_MsgTimeStamp_Object = MibTableColumn
msgTimeStamp = _MsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 1, 1, 6),
    _MsgTimeStamp_Type()
)
msgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msgTimeStamp.setStatus("current")

# Managed Objects groups

jbossObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39999, 1, 1)
)
jbossObjectGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "activeThreadCount"),
        ("OTA-PLATFORM-MIB", "freeMemory"),
        ("OTA-PLATFORM-MIB", "maxMemory"),
        ("OTA-PLATFORM-MIB", "requestCount8080"),
        ("OTA-PLATFORM-MIB", "txCommitCount"),
        ("OTA-PLATFORM-MIB", "txRollbackCount"),
        ("OTA-PLATFORM-MIB", "txActiveCount"),
        ("OTA-PLATFORM-MIB", "dbInUseConnection"),
        ("OTA-PLATFORM-MIB", "dbMaxConnectionsInUse"))
)
if mibBuilder.loadTexts:
    jbossObjectGroup.setStatus("current")

smscObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 20)
)
smscObjGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "smscSeqNumber"),
        ("OTA-PLATFORM-MIB", "smscSeverity"),
        ("OTA-PLATFORM-MIB", "smscName"),
        ("OTA-PLATFORM-MIB", "smscMsg"),
        ("OTA-PLATFORM-MIB", "smscIp"),
        ("OTA-PLATFORM-MIB", "smscTimeStamp"))
)
if mibBuilder.loadTexts:
    smscObjGroup.setStatus("current")

smscGroupobjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 20)
)
smscGroupobjGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "smscGroupSeqNumber"),
        ("OTA-PLATFORM-MIB", "smscGroupSeverity"),
        ("OTA-PLATFORM-MIB", "smscGroupName"),
        ("OTA-PLATFORM-MIB", "smscGroupMsg"),
        ("OTA-PLATFORM-MIB", "smscGroupTimeStamp"))
)
if mibBuilder.loadTexts:
    smscGroupobjGroup.setStatus("current")

msgDiscriminatorObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 10)
)
msgDiscriminatorObjGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "msgSeqNumber"),
        ("OTA-PLATFORM-MIB", "msgSeverity"),
        ("OTA-PLATFORM-MIB", "msgName"),
        ("OTA-PLATFORM-MIB", "msg"),
        ("OTA-PLATFORM-MIB", "msgTimeStamp"))
)
if mibBuilder.loadTexts:
    msgDiscriminatorObjGroup.setStatus("current")


# Notification objects

smscConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 1)
)
smscConnected.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscConnected.setStatus(
        "current"
    )

smscDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 2)
)
smscDisconnected.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscDisconnected.setStatus(
        "current"
    )

smscDuplicatedMessageId = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 3)
)
smscDuplicatedMessageId.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscDuplicatedMessageId.setStatus(
        "current"
    )

smscDuplicatedMessageIdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 4)
)
smscDuplicatedMessageIdClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscDuplicatedMessageIdClear.setStatus(
        "current"
    )

smscMessagesQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 5)
)
smscMessagesQueueFull.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscMessagesQueueFull.setStatus(
        "current"
    )

smscMessagesQueueFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 6)
)
smscMessagesQueueFullClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscMessagesQueueFullClear.setStatus(
        "current"
    )

smscCommandsQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 7)
)
smscCommandsQueueFull.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscCommandsQueueFull.setStatus(
        "current"
    )

smscCommandsQueueFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 8)
)
smscCommandsQueueFullClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscCommandsQueueFullClear.setStatus(
        "current"
    )

smscReceivedUnsupportedMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 9)
)
smscReceivedUnsupportedMsg.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscReceivedUnsupportedMsg.setStatus(
        "current"
    )

smscReceivedUnsupportedMsgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 10)
)
smscReceivedUnsupportedMsgClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscReceivedUnsupportedMsgClear.setStatus(
        "current"
    )

smscInvalidConfirmation = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 11)
)
smscInvalidConfirmation.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscInvalidConfirmation.setStatus(
        "current"
    )

smscInvalidConfirmationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 12)
)
smscInvalidConfirmationClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscInvalidConfirmationClear.setStatus(
        "current"
    )

smscUnknownPdu = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 13)
)
smscUnknownPdu.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscUnknownPdu.setStatus(
        "current"
    )

smscUnknownPduClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 14)
)
smscUnknownPduClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscUnknownPduClear.setStatus(
        "current"
    )

smscUnexpectedPdu = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 15)
)
smscUnexpectedPdu.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscUnexpectedPdu.setStatus(
        "current"
    )

smscUnexpectedPduClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 16)
)
smscUnexpectedPduClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscUnexpectedPduClear.setStatus(
        "current"
    )

smscErrorProcessingPdu = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 17)
)
smscErrorProcessingPdu.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscErrorProcessingPdu.setStatus(
        "current"
    )

smscErrorProcessingPduClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 18)
)
smscErrorProcessingPduClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscErrorProcessingPduClear.setStatus(
        "current"
    )

smscSendingUnsupportedMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 19)
)
smscSendingUnsupportedMsg.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscSendingUnsupportedMsg.setStatus(
        "current"
    )

smscSendingUnsupportedMsgClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 20)
)
smscSendingUnsupportedMsgClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscSendingUnsupportedMsgClear.setStatus(
        "current"
    )

smscReceivedMsgDiscarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 21)
)
smscReceivedMsgDiscarded.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscReceivedMsgDiscarded.setStatus(
        "current"
    )

smscReceivedMsgDiscardedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 22)
)
smscReceivedMsgDiscardedClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscReceivedMsgDiscardedClear.setStatus(
        "current"
    )

smscPduNotAnswered = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 23)
)
smscPduNotAnswered.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscPduNotAnswered.setStatus(
        "current"
    )

smscPduNotAnsweredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 24)
)
smscPduNotAnsweredClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscPduNotAnsweredClear.setStatus(
        "current"
    )

smscNotAssociateDiscriminator = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 25)
)
smscNotAssociateDiscriminator.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscNotAssociateDiscriminator.setStatus(
        "current"
    )

smscNotAssociateDiscriminatorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2, 26)
)
smscNotAssociateDiscriminatorClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscTable")
)
if mibBuilder.loadTexts:
    smscNotAssociateDiscriminatorClear.setStatus(
        "current"
    )

smscGroupNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 1)
)
smscGroupNotAvailable.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupNotAvailable.setStatus(
        "current"
    )

smscGroupNotAvailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 2)
)
smscGroupNotAvailableClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupNotAvailableClear.setStatus(
        "current"
    )

smscGroupInvalidDestination = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 3)
)
smscGroupInvalidDestination.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupInvalidDestination.setStatus(
        "current"
    )

smscGroupInvalidDestinationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 4)
)
smscGroupInvalidDestinationClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupInvalidDestinationClear.setStatus(
        "current"
    )

smscGroupFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 5)
)
smscGroupFull.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupFull.setStatus(
        "current"
    )

smscGroupFullClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 6)
)
smscGroupFullClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupFullClear.setStatus(
        "current"
    )

smscGroupMessageExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 7)
)
smscGroupMessageExpired.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupMessageExpired.setStatus(
        "current"
    )

smscGroupMessageExpiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 8)
)
smscGroupMessageExpiredClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupMessageExpiredClear.setStatus(
        "current"
    )

smscGroupUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 9)
)
smscGroupUnknown.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupUnknown.setStatus(
        "current"
    )

smscGroupUnknownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2, 10)
)
smscGroupUnknownClear.setObjects(
    ("OTA-PLATFORM-MIB", "smscGroupTable")
)
if mibBuilder.loadTexts:
    smscGroupUnknownClear.setStatus(
        "current"
    )

messageNotDelivered = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 3, 1)
)
messageNotDelivered.setObjects(
    ("OTA-PLATFORM-MIB", "msgDiscriminatorTable")
)
if mibBuilder.loadTexts:
    messageNotDelivered.setStatus(
        "current"
    )

messageNotDeliveredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 3, 2)
)
messageNotDeliveredClear.setObjects(
    ("OTA-PLATFORM-MIB", "msgDiscriminatorTable")
)
if mibBuilder.loadTexts:
    messageNotDeliveredClear.setStatus(
        "current"
    )


# Notifications groups

notifySMSC = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 2, 2)
)
notifySMSC.setObjects(
      *(("OTA-PLATFORM-MIB", "messageNotDelivered"),
        ("OTA-PLATFORM-MIB", "messageNotDeliveredClear"))
)
if mibBuilder.loadTexts:
    notifySMSC.setStatus(
        "current"
    )

notifySMSCGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 3, 2)
)
notifySMSCGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "smscGroupNotAvailable"),
        ("OTA-PLATFORM-MIB", "smscGroupInvalidDestination"),
        ("OTA-PLATFORM-MIB", "smscGroupFull"),
        ("OTA-PLATFORM-MIB", "smscGroupMessageExpired"),
        ("OTA-PLATFORM-MIB", "smscGroupUnknown"),
        ("OTA-PLATFORM-MIB", "smscGroupCleaner"))
)
if mibBuilder.loadTexts:
    notifySMSCGroup.setStatus(
        "current"
    )

notifyMSGDiscriminatorGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39999, 3, 4, 3)
)
notifyMSGDiscriminatorGroup.setObjects(
      *(("OTA-PLATFORM-MIB", "messageNotDelivered"),
        ("OTA-PLATFORM-MIB", "messageNotDeliveredClear"))
)
if mibBuilder.loadTexts:
    notifyMSGDiscriminatorGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OTA-PLATFORM-MIB",
    **{"ota-oberthur": ota_oberthur,
       "jboss": jboss,
       "jbossObjectGroup": jbossObjectGroup,
       "activeThreadCount": activeThreadCount,
       "freeMemory": freeMemory,
       "maxMemory": maxMemory,
       "threadPoolQueueSize": threadPoolQueueSize,
       "requestCount8080": requestCount8080,
       "txCommitCount": txCommitCount,
       "txRollbackCount": txRollbackCount,
       "txActiveCount": txActiveCount,
       "dbInUseConnection": dbInUseConnection,
       "dbMaxConnectionsInUse": dbMaxConnectionsInUse,
       "urls": urls,
       "webapps": webapps,
       "contentroot": contentroot,
       "webObjectName": webObjectName,
       "webDistributable": webDistributable,
       "webSessionCounter": webSessionCounter,
       "webActiveSessions": webActiveSessions,
       "otaplatform": otaplatform,
       "smsc": smsc,
       "smscTable": smscTable,
       "smscEntry": smscEntry,
       "smscSeqNumber": smscSeqNumber,
       "smscSeverity": smscSeverity,
       "smscName": smscName,
       "smscMsg": smscMsg,
       "smscIp": smscIp,
       "smscTimeStamp": smscTimeStamp,
       "notifySMSC": notifySMSC,
       "smscConnected": smscConnected,
       "smscDisconnected": smscDisconnected,
       "smscDuplicatedMessageId": smscDuplicatedMessageId,
       "smscDuplicatedMessageIdClear": smscDuplicatedMessageIdClear,
       "smscMessagesQueueFull": smscMessagesQueueFull,
       "smscMessagesQueueFullClear": smscMessagesQueueFullClear,
       "smscCommandsQueueFull": smscCommandsQueueFull,
       "smscCommandsQueueFullClear": smscCommandsQueueFullClear,
       "smscReceivedUnsupportedMsg": smscReceivedUnsupportedMsg,
       "smscReceivedUnsupportedMsgClear": smscReceivedUnsupportedMsgClear,
       "smscInvalidConfirmation": smscInvalidConfirmation,
       "smscInvalidConfirmationClear": smscInvalidConfirmationClear,
       "smscUnknownPdu": smscUnknownPdu,
       "smscUnknownPduClear": smscUnknownPduClear,
       "smscUnexpectedPdu": smscUnexpectedPdu,
       "smscUnexpectedPduClear": smscUnexpectedPduClear,
       "smscErrorProcessingPdu": smscErrorProcessingPdu,
       "smscErrorProcessingPduClear": smscErrorProcessingPduClear,
       "smscSendingUnsupportedMsg": smscSendingUnsupportedMsg,
       "smscSendingUnsupportedMsgClear": smscSendingUnsupportedMsgClear,
       "smscReceivedMsgDiscarded": smscReceivedMsgDiscarded,
       "smscReceivedMsgDiscardedClear": smscReceivedMsgDiscardedClear,
       "smscPduNotAnswered": smscPduNotAnswered,
       "smscPduNotAnsweredClear": smscPduNotAnsweredClear,
       "smscNotAssociateDiscriminator": smscNotAssociateDiscriminator,
       "smscNotAssociateDiscriminatorClear": smscNotAssociateDiscriminatorClear,
       "smscObjGroup": smscObjGroup,
       "smscgroup": smscgroup,
       "smscGroupTable": smscGroupTable,
       "smscGroupEntry": smscGroupEntry,
       "smscGroupSeqNumber": smscGroupSeqNumber,
       "smscGroupSeverity": smscGroupSeverity,
       "smscGroupName": smscGroupName,
       "smscGroupMsg": smscGroupMsg,
       "smscGroupTimeStamp": smscGroupTimeStamp,
       "notifySMSCGroup": notifySMSCGroup,
       "smscGroupNotAvailable": smscGroupNotAvailable,
       "smscGroupNotAvailableClear": smscGroupNotAvailableClear,
       "smscGroupInvalidDestination": smscGroupInvalidDestination,
       "smscGroupInvalidDestinationClear": smscGroupInvalidDestinationClear,
       "smscGroupFull": smscGroupFull,
       "smscGroupFullClear": smscGroupFullClear,
       "smscGroupMessageExpired": smscGroupMessageExpired,
       "smscGroupMessageExpiredClear": smscGroupMessageExpiredClear,
       "smscGroupUnknown": smscGroupUnknown,
       "smscGroupUnknownClear": smscGroupUnknownClear,
       "smscGroupobjGroup": smscGroupobjGroup,
       "msgdiscriminator": msgdiscriminator,
       "msgDiscriminatorTable": msgDiscriminatorTable,
       "msgDiscriminatorEntry": msgDiscriminatorEntry,
       "msgSeqNumber": msgSeqNumber,
       "msgSeverity": msgSeverity,
       "msgName": msgName,
       "msg": msg,
       "msgTimeStamp": msgTimeStamp,
       "notifyMSGDiscriminatorGroup": notifyMSGDiscriminatorGroup,
       "messageNotDelivered": messageNotDelivered,
       "messageNotDeliveredClear": messageNotDeliveredClear,
       "msgDiscriminatorObjGroup": msgDiscriminatorObjGroup}
)
