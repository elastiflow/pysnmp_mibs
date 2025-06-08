# SNMP MIB module (SMARTCAST-SLEDGEHAMMER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/smartcast_44502/SMARTCAST-SLEDGEHAMMER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:00:16 2025
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
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

sled = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44502)
)
if mibBuilder.loadTexts:
    sled.setRevisions(
        ("2015-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44502, 0)
)
_ProcOutput_ObjectIdentity = ObjectIdentity
procOutput = _ProcOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0)
)
_ProcOutputStatusTable_Object = MibTable
procOutputStatusTable = _ProcOutputStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1)
)
if mibBuilder.loadTexts:
    procOutputStatusTable.setStatus("current")
_ProcOutputStatusEntry_Object = MibTableRow
procOutputStatusEntry = _ProcOutputStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1)
)
procOutputStatusEntry.setIndexNames(
    (0, "SMARTCAST-SLEDGEHAMMER-MIB", "procOutputStatusIndex"),
)
if mibBuilder.loadTexts:
    procOutputStatusEntry.setStatus("current")
_ProcOutputStatusIndex_Type = Gauge32
_ProcOutputStatusIndex_Object = MibTableColumn
procOutputStatusIndex = _ProcOutputStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 1),
    _ProcOutputStatusIndex_Type()
)
procOutputStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procOutputStatusIndex.setStatus("current")
_OutputVideoStatus_Type = Integer32
_OutputVideoStatus_Object = MibTableColumn
outputVideoStatus = _OutputVideoStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 2),
    _OutputVideoStatus_Type()
)
outputVideoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputVideoStatus.setStatus("current")
_OutputAudioStatus_Type = Integer32
_OutputAudioStatus_Object = MibTableColumn
outputAudioStatus = _OutputAudioStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 3),
    _OutputAudioStatus_Type()
)
outputAudioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputAudioStatus.setStatus("current")
_Videobuffer_Type = Integer32
_Videobuffer_Object = MibTableColumn
videobuffer = _Videobuffer_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 4),
    _Videobuffer_Type()
)
videobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videobuffer.setStatus("current")
_Audiobuffer_Type = Integer32
_Audiobuffer_Object = MibTableColumn
audiobuffer = _Audiobuffer_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 5),
    _Audiobuffer_Type()
)
audiobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audiobuffer.setStatus("current")
_Playlistdrift_Type = Integer32
_Playlistdrift_Object = MibTableColumn
playlistdrift = _Playlistdrift_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 6),
    _Playlistdrift_Type()
)
playlistdrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    playlistdrift.setStatus("current")
_SyncerStatus_Type = Integer32
_SyncerStatus_Object = MibTableColumn
syncerStatus = _SyncerStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 0, 1, 1, 7),
    _SyncerStatus_Type()
)
syncerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncerStatus.setStatus("current")
_ProcIngest_ObjectIdentity = ObjectIdentity
procIngest = _ProcIngest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1)
)
_IngestStatus_Type = Integer32
_IngestStatus_Object = MibScalar
ingestStatus = _IngestStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 1),
    _IngestStatus_Type()
)
ingestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingestStatus.setStatus("current")
_ProcIngestTable_Object = MibTable
procIngestTable = _ProcIngestTable_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 2)
)
if mibBuilder.loadTexts:
    procIngestTable.setStatus("current")
_ProcIngestEntry_Object = MibTableRow
procIngestEntry = _ProcIngestEntry_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 2, 1)
)
procIngestEntry.setIndexNames(
    (0, "SMARTCAST-SLEDGEHAMMER-MIB", "procIngestIndex"),
)
if mibBuilder.loadTexts:
    procIngestEntry.setStatus("current")
_ProcIngestIndex_Type = Gauge32
_ProcIngestIndex_Object = MibTableColumn
procIngestIndex = _ProcIngestIndex_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 2, 1, 1),
    _ProcIngestIndex_Type()
)
procIngestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    procIngestIndex.setStatus("current")
_IngestsFailed_Type = Integer32
_IngestsFailed_Object = MibTableColumn
ingestsFailed = _IngestsFailed_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 2, 1, 2),
    _IngestsFailed_Type()
)
ingestsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ingestsFailed.setStatus("current")
_LastSuccesfulSequenceUpdate_Type = Integer32
_LastSuccesfulSequenceUpdate_Object = MibTableColumn
lastSuccesfulSequenceUpdate = _LastSuccesfulSequenceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 2, 1, 3),
    _LastSuccesfulSequenceUpdate_Type()
)
lastSuccesfulSequenceUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastSuccesfulSequenceUpdate.setStatus("current")
_PlsingestStatus_Type = Integer32
_PlsingestStatus_Object = MibScalar
plsingestStatus = _PlsingestStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 1, 3),
    _PlsingestStatus_Type()
)
plsingestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsingestStatus.setStatus("current")
_ProcContentdelivery_ObjectIdentity = ObjectIdentity
procContentdelivery = _ProcContentdelivery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44502, 0, 2)
)
_ContentdeliveryStatus_Type = Integer32
_ContentdeliveryStatus_Object = MibScalar
contentdeliveryStatus = _ContentdeliveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 2, 1),
    _ContentdeliveryStatus_Type()
)
contentdeliveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentdeliveryStatus.setStatus("current")
_ContentdeliveriesScheduled_Type = Integer32
_ContentdeliveriesScheduled_Object = MibScalar
contentdeliveriesScheduled = _ContentdeliveriesScheduled_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 2, 2),
    _ContentdeliveriesScheduled_Type()
)
contentdeliveriesScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contentdeliveriesScheduled.setStatus("current")
_MediapoolStatus_Type = Integer32
_MediapoolStatus_Object = MibScalar
mediapoolStatus = _MediapoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 2, 3),
    _MediapoolStatus_Type()
)
mediapoolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediapoolStatus.setStatus("current")
_PlsserviceStatus_Type = Integer32
_PlsserviceStatus_Object = MibScalar
plsserviceStatus = _PlsserviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 44502, 0, 2, 4),
    _PlsserviceStatus_Type()
)
plsserviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    plsserviceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMARTCAST-SLEDGEHAMMER-MIB",
    **{"sled": sled,
       "software": software,
       "procOutput": procOutput,
       "procOutputStatusTable": procOutputStatusTable,
       "procOutputStatusEntry": procOutputStatusEntry,
       "procOutputStatusIndex": procOutputStatusIndex,
       "outputVideoStatus": outputVideoStatus,
       "outputAudioStatus": outputAudioStatus,
       "videobuffer": videobuffer,
       "audiobuffer": audiobuffer,
       "playlistdrift": playlistdrift,
       "syncerStatus": syncerStatus,
       "procIngest": procIngest,
       "ingestStatus": ingestStatus,
       "procIngestTable": procIngestTable,
       "procIngestEntry": procIngestEntry,
       "procIngestIndex": procIngestIndex,
       "ingestsFailed": ingestsFailed,
       "lastSuccesfulSequenceUpdate": lastSuccesfulSequenceUpdate,
       "plsingestStatus": plsingestStatus,
       "procContentdelivery": procContentdelivery,
       "contentdeliveryStatus": contentdeliveryStatus,
       "contentdeliveriesScheduled": contentdeliveriesScheduled,
       "mediapoolStatus": mediapoolStatus,
       "plsserviceStatus": plsserviceStatus}
)
