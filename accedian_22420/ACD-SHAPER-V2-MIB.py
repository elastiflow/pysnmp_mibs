# SNMP MIB module (ACD-SHAPER-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/accedian_22420/ACD-SHAPER-V2-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:08:00 2025
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

acdShaperV2Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21)
)
if mibBuilder.loadTexts:
    acdShaperV2Mib.setRevisions(
        ("2016-09-23 01:00",
         "2016-05-26 01:00",
         "2014-02-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdShaperV2Notifications_ObjectIdentity = ObjectIdentity
acdShaperV2Notifications = _AcdShaperV2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 0)
)
_AcdShaperV2MIBObjects_ObjectIdentity = ObjectIdentity
acdShaperV2MIBObjects = _AcdShaperV2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1)
)
_AcdShaperV2QueueStatsTable_Object = MibTable
acdShaperV2QueueStatsTable = _AcdShaperV2QueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1)
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsTable.setStatus("current")
_AcdShaperV2QueueStatsEntry_Object = MibTableRow
acdShaperV2QueueStatsEntry = _AcdShaperV2QueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1)
)
acdShaperV2QueueStatsEntry.setIndexNames(
    (0, "ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsQueueId"),
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsEntry.setStatus("current")
_AcdShaperV2QueueStatsQueueId_Type = Unsigned32
_AcdShaperV2QueueStatsQueueId_Object = MibTableColumn
acdShaperV2QueueStatsQueueId = _AcdShaperV2QueueStatsQueueId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 1),
    _AcdShaperV2QueueStatsQueueId_Type()
)
acdShaperV2QueueStatsQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsQueueId.setStatus("current")


class _AcdShaperV2QueueStatsQueueName_Type(DisplayString):
    """Custom type acdShaperV2QueueStatsQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdShaperV2QueueStatsQueueName_Type.__name__ = "DisplayString"
_AcdShaperV2QueueStatsQueueName_Object = MibTableColumn
acdShaperV2QueueStatsQueueName = _AcdShaperV2QueueStatsQueueName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 2),
    _AcdShaperV2QueueStatsQueueName_Type()
)
acdShaperV2QueueStatsQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsQueueName.setStatus("current")
_AcdShaperV2QueueStatsCntGreenForwardNoDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsCntGreenForwardNoDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenForwardNoDelayFrames = _AcdShaperV2QueueStatsCntGreenForwardNoDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 3),
    _AcdShaperV2QueueStatsCntGreenForwardNoDelayFrames_Type()
)
acdShaperV2QueueStatsCntGreenForwardNoDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenForwardNoDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsCntGreenForwardNoDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsCntGreenForwardNoDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenForwardNoDelayBytes = _AcdShaperV2QueueStatsCntGreenForwardNoDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 4),
    _AcdShaperV2QueueStatsCntGreenForwardNoDelayBytes_Type()
)
acdShaperV2QueueStatsCntGreenForwardNoDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenForwardNoDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsCntYellowForwardNoDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsCntYellowForwardNoDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowForwardNoDelayFrames = _AcdShaperV2QueueStatsCntYellowForwardNoDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 5),
    _AcdShaperV2QueueStatsCntYellowForwardNoDelayFrames_Type()
)
acdShaperV2QueueStatsCntYellowForwardNoDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowForwardNoDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsCntYellowForwardNoDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsCntYellowForwardNoDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowForwardNoDelayBytes = _AcdShaperV2QueueStatsCntYellowForwardNoDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 6),
    _AcdShaperV2QueueStatsCntYellowForwardNoDelayBytes_Type()
)
acdShaperV2QueueStatsCntYellowForwardNoDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowForwardNoDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsCntGreenForwardWithDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsCntGreenForwardWithDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenForwardWithDelayFrames = _AcdShaperV2QueueStatsCntGreenForwardWithDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 7),
    _AcdShaperV2QueueStatsCntGreenForwardWithDelayFrames_Type()
)
acdShaperV2QueueStatsCntGreenForwardWithDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenForwardWithDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsCntGreenForwardWithDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsCntGreenForwardWithDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenForwardWithDelayBytes = _AcdShaperV2QueueStatsCntGreenForwardWithDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 8),
    _AcdShaperV2QueueStatsCntGreenForwardWithDelayBytes_Type()
)
acdShaperV2QueueStatsCntGreenForwardWithDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenForwardWithDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsCntYellowForwardWithDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsCntYellowForwardWithDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowForwardWithDelayFrames = _AcdShaperV2QueueStatsCntYellowForwardWithDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 9),
    _AcdShaperV2QueueStatsCntYellowForwardWithDelayFrames_Type()
)
acdShaperV2QueueStatsCntYellowForwardWithDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowForwardWithDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsCntYellowForwardWithDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsCntYellowForwardWithDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowForwardWithDelayBytes = _AcdShaperV2QueueStatsCntYellowForwardWithDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 10),
    _AcdShaperV2QueueStatsCntYellowForwardWithDelayBytes_Type()
)
acdShaperV2QueueStatsCntYellowForwardWithDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowForwardWithDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsCntGreenDiscardFullFrames_Type = Counter64
_AcdShaperV2QueueStatsCntGreenDiscardFullFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenDiscardFullFrames = _AcdShaperV2QueueStatsCntGreenDiscardFullFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 11),
    _AcdShaperV2QueueStatsCntGreenDiscardFullFrames_Type()
)
acdShaperV2QueueStatsCntGreenDiscardFullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenDiscardFullFrames.setStatus("current")
_AcdShaperV2QueueStatsCntGreenDiscardFullBytes_Type = Counter64
_AcdShaperV2QueueStatsCntGreenDiscardFullBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenDiscardFullBytes = _AcdShaperV2QueueStatsCntGreenDiscardFullBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 12),
    _AcdShaperV2QueueStatsCntGreenDiscardFullBytes_Type()
)
acdShaperV2QueueStatsCntGreenDiscardFullBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenDiscardFullBytes.setStatus("current")
_AcdShaperV2QueueStatsCntYellowDiscardFullFrames_Type = Counter64
_AcdShaperV2QueueStatsCntYellowDiscardFullFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowDiscardFullFrames = _AcdShaperV2QueueStatsCntYellowDiscardFullFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 13),
    _AcdShaperV2QueueStatsCntYellowDiscardFullFrames_Type()
)
acdShaperV2QueueStatsCntYellowDiscardFullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowDiscardFullFrames.setStatus("current")
_AcdShaperV2QueueStatsCntYellowDiscardFullBytes_Type = Counter64
_AcdShaperV2QueueStatsCntYellowDiscardFullBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowDiscardFullBytes = _AcdShaperV2QueueStatsCntYellowDiscardFullBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 14),
    _AcdShaperV2QueueStatsCntYellowDiscardFullBytes_Type()
)
acdShaperV2QueueStatsCntYellowDiscardFullBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowDiscardFullBytes.setStatus("current")
_AcdShaperV2QueueStatsCntGreenDiscardBLUEFrames_Type = Counter64
_AcdShaperV2QueueStatsCntGreenDiscardBLUEFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenDiscardBLUEFrames = _AcdShaperV2QueueStatsCntGreenDiscardBLUEFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 15),
    _AcdShaperV2QueueStatsCntGreenDiscardBLUEFrames_Type()
)
acdShaperV2QueueStatsCntGreenDiscardBLUEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenDiscardBLUEFrames.setStatus("current")
_AcdShaperV2QueueStatsCntGreenDiscardBLUEBytes_Type = Counter64
_AcdShaperV2QueueStatsCntGreenDiscardBLUEBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntGreenDiscardBLUEBytes = _AcdShaperV2QueueStatsCntGreenDiscardBLUEBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 16),
    _AcdShaperV2QueueStatsCntGreenDiscardBLUEBytes_Type()
)
acdShaperV2QueueStatsCntGreenDiscardBLUEBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntGreenDiscardBLUEBytes.setStatus("current")
_AcdShaperV2QueueStatsCntYellowDiscardBLUEFrames_Type = Counter64
_AcdShaperV2QueueStatsCntYellowDiscardBLUEFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowDiscardBLUEFrames = _AcdShaperV2QueueStatsCntYellowDiscardBLUEFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 17),
    _AcdShaperV2QueueStatsCntYellowDiscardBLUEFrames_Type()
)
acdShaperV2QueueStatsCntYellowDiscardBLUEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowDiscardBLUEFrames.setStatus("current")
_AcdShaperV2QueueStatsCntYellowDiscardBLUEBytes_Type = Counter64
_AcdShaperV2QueueStatsCntYellowDiscardBLUEBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntYellowDiscardBLUEBytes = _AcdShaperV2QueueStatsCntYellowDiscardBLUEBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 18),
    _AcdShaperV2QueueStatsCntYellowDiscardBLUEBytes_Type()
)
acdShaperV2QueueStatsCntYellowDiscardBLUEBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntYellowDiscardBLUEBytes.setStatus("current")
_AcdShaperV2QueueStatsCntCIRCompliantFrames_Type = Counter64
_AcdShaperV2QueueStatsCntCIRCompliantFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntCIRCompliantFrames = _AcdShaperV2QueueStatsCntCIRCompliantFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 19),
    _AcdShaperV2QueueStatsCntCIRCompliantFrames_Type()
)
acdShaperV2QueueStatsCntCIRCompliantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntCIRCompliantFrames.setStatus("current")
_AcdShaperV2QueueStatsCntCIRCompliantBytes_Type = Counter64
_AcdShaperV2QueueStatsCntCIRCompliantBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntCIRCompliantBytes = _AcdShaperV2QueueStatsCntCIRCompliantBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 20),
    _AcdShaperV2QueueStatsCntCIRCompliantBytes_Type()
)
acdShaperV2QueueStatsCntCIRCompliantBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntCIRCompliantBytes.setStatus("current")
_AcdShaperV2QueueStatsCntEIRCompliantFrames_Type = Counter64
_AcdShaperV2QueueStatsCntEIRCompliantFrames_Object = MibTableColumn
acdShaperV2QueueStatsCntEIRCompliantFrames = _AcdShaperV2QueueStatsCntEIRCompliantFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 21),
    _AcdShaperV2QueueStatsCntEIRCompliantFrames_Type()
)
acdShaperV2QueueStatsCntEIRCompliantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntEIRCompliantFrames.setStatus("current")
_AcdShaperV2QueueStatsCntEIRCompliantBytes_Type = Counter64
_AcdShaperV2QueueStatsCntEIRCompliantBytes_Object = MibTableColumn
acdShaperV2QueueStatsCntEIRCompliantBytes = _AcdShaperV2QueueStatsCntEIRCompliantBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 1, 1, 22),
    _AcdShaperV2QueueStatsCntEIRCompliantBytes_Type()
)
acdShaperV2QueueStatsCntEIRCompliantBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsCntEIRCompliantBytes.setStatus("current")
_AcdShaperV2QueueStatsHistTable_Object = MibTable
acdShaperV2QueueStatsHistTable = _AcdShaperV2QueueStatsHistTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistTable.setStatus("current")
_AcdShaperV2QueueStatsHistEntry_Object = MibTableRow
acdShaperV2QueueStatsHistEntry = _AcdShaperV2QueueStatsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1)
)
acdShaperV2QueueStatsHistEntry.setIndexNames(
    (0, "ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistQueueId"),
    (0, "ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistIndex"),
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistEntry.setStatus("current")
_AcdShaperV2QueueStatsHistIndex_Type = Unsigned32
_AcdShaperV2QueueStatsHistIndex_Object = MibTableColumn
acdShaperV2QueueStatsHistIndex = _AcdShaperV2QueueStatsHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 1),
    _AcdShaperV2QueueStatsHistIndex_Type()
)
acdShaperV2QueueStatsHistIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistIndex.setStatus("current")
_AcdShaperV2QueueStatsHistSamplingEndTime_Type = DateAndTime
_AcdShaperV2QueueStatsHistSamplingEndTime_Object = MibTableColumn
acdShaperV2QueueStatsHistSamplingEndTime = _AcdShaperV2QueueStatsHistSamplingEndTime_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 2),
    _AcdShaperV2QueueStatsHistSamplingEndTime_Type()
)
acdShaperV2QueueStatsHistSamplingEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistSamplingEndTime.setStatus("current")
_AcdShaperV2QueueStatsHistQueueId_Type = Unsigned32
_AcdShaperV2QueueStatsHistQueueId_Object = MibTableColumn
acdShaperV2QueueStatsHistQueueId = _AcdShaperV2QueueStatsHistQueueId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 3),
    _AcdShaperV2QueueStatsHistQueueId_Type()
)
acdShaperV2QueueStatsHistQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistQueueId.setStatus("current")


class _AcdShaperV2QueueStatsHistQueueName_Type(DisplayString):
    """Custom type acdShaperV2QueueStatsHistQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AcdShaperV2QueueStatsHistQueueName_Type.__name__ = "DisplayString"
_AcdShaperV2QueueStatsHistQueueName_Object = MibTableColumn
acdShaperV2QueueStatsHistQueueName = _AcdShaperV2QueueStatsHistQueueName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 4),
    _AcdShaperV2QueueStatsHistQueueName_Type()
)
acdShaperV2QueueStatsHistQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistQueueName.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames = _AcdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 5),
    _AcdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames_Type()
)
acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes = _AcdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 6),
    _AcdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes_Type()
)
acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames = _AcdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 7),
    _AcdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames_Type()
)
acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes = _AcdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 8),
    _AcdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes_Type()
)
acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames = _AcdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 9),
    _AcdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames_Type()
)
acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes = _AcdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 10),
    _AcdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes_Type()
)
acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames = _AcdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 11),
    _AcdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames_Type()
)
acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes = _AcdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 12),
    _AcdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes_Type()
)
acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenDiscardFullFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenDiscardFullFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenDiscardFullFrames = _AcdShaperV2QueueStatsHistCntGreenDiscardFullFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 13),
    _AcdShaperV2QueueStatsHistCntGreenDiscardFullFrames_Type()
)
acdShaperV2QueueStatsHistCntGreenDiscardFullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenDiscardFullFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenDiscardFullBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenDiscardFullBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenDiscardFullBytes = _AcdShaperV2QueueStatsHistCntGreenDiscardFullBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 14),
    _AcdShaperV2QueueStatsHistCntGreenDiscardFullBytes_Type()
)
acdShaperV2QueueStatsHistCntGreenDiscardFullBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenDiscardFullBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowDiscardFullFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowDiscardFullFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowDiscardFullFrames = _AcdShaperV2QueueStatsHistCntYellowDiscardFullFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 15),
    _AcdShaperV2QueueStatsHistCntYellowDiscardFullFrames_Type()
)
acdShaperV2QueueStatsHistCntYellowDiscardFullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowDiscardFullFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowDiscardFullBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowDiscardFullBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowDiscardFullBytes = _AcdShaperV2QueueStatsHistCntYellowDiscardFullBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 16),
    _AcdShaperV2QueueStatsHistCntYellowDiscardFullBytes_Type()
)
acdShaperV2QueueStatsHistCntYellowDiscardFullBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowDiscardFullBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames = _AcdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 17),
    _AcdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames_Type()
)
acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes = _AcdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 18),
    _AcdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes_Type()
)
acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames = _AcdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 19),
    _AcdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames_Type()
)
acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes = _AcdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 20),
    _AcdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes_Type()
)
acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntCIRCompliantFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntCIRCompliantFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntCIRCompliantFrames = _AcdShaperV2QueueStatsHistCntCIRCompliantFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 21),
    _AcdShaperV2QueueStatsHistCntCIRCompliantFrames_Type()
)
acdShaperV2QueueStatsHistCntCIRCompliantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntCIRCompliantFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntCIRCompliantBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntCIRCompliantBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntCIRCompliantBytes = _AcdShaperV2QueueStatsHistCntCIRCompliantBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 22),
    _AcdShaperV2QueueStatsHistCntCIRCompliantBytes_Type()
)
acdShaperV2QueueStatsHistCntCIRCompliantBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntCIRCompliantBytes.setStatus("current")
_AcdShaperV2QueueStatsHistCntEIRCompliantFrames_Type = Counter64
_AcdShaperV2QueueStatsHistCntEIRCompliantFrames_Object = MibTableColumn
acdShaperV2QueueStatsHistCntEIRCompliantFrames = _AcdShaperV2QueueStatsHistCntEIRCompliantFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 23),
    _AcdShaperV2QueueStatsHistCntEIRCompliantFrames_Type()
)
acdShaperV2QueueStatsHistCntEIRCompliantFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntEIRCompliantFrames.setStatus("current")
_AcdShaperV2QueueStatsHistCntEIRCompliantBytes_Type = Counter64
_AcdShaperV2QueueStatsHistCntEIRCompliantBytes_Object = MibTableColumn
acdShaperV2QueueStatsHistCntEIRCompliantBytes = _AcdShaperV2QueueStatsHistCntEIRCompliantBytes_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 1, 2, 1, 24),
    _AcdShaperV2QueueStatsHistCntEIRCompliantBytes_Type()
)
acdShaperV2QueueStatsHistCntEIRCompliantBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistCntEIRCompliantBytes.setStatus("current")
_AcdShaperV2Conformance_ObjectIdentity = ObjectIdentity
acdShaperV2Conformance = _AcdShaperV2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2)
)
_AcdShaperV2Compliances_ObjectIdentity = ObjectIdentity
acdShaperV2Compliances = _AcdShaperV2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2, 1)
)
_AcdShaperV2Groups_ObjectIdentity = ObjectIdentity
acdShaperV2Groups = _AcdShaperV2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2, 2)
)

# Managed Objects groups

acdShaperV2QueueStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2, 2, 1)
)
acdShaperV2QueueStatsGroup.setObjects(
      *(("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsQueueName"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenForwardNoDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenForwardNoDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowForwardNoDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowForwardNoDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenForwardWithDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenForwardWithDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowForwardWithDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowForwardWithDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenDiscardFullFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenDiscardFullBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowDiscardFullFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowDiscardFullBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenDiscardBLUEFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntGreenDiscardBLUEBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowDiscardBLUEFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntYellowDiscardBLUEBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntCIRCompliantFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntCIRCompliantBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntEIRCompliantFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsCntEIRCompliantBytes"))
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsGroup.setStatus("current")

acdShaperV2QueueStatsHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2, 2, 2)
)
acdShaperV2QueueStatsHistGroup.setObjects(
      *(("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistIndex"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistSamplingEndTime"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistQueueId"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistQueueName"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenDiscardFullFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenDiscardFullBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowDiscardFullFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowDiscardFullBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntCIRCompliantFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntCIRCompliantBytes"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntEIRCompliantFrames"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistCntEIRCompliantBytes"))
)
if mibBuilder.loadTexts:
    acdShaperV2QueueStatsHistGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdShaperV2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 21, 2, 1, 1)
)
acdShaperV2Compliance.setObjects(
      *(("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsGroup"),
        ("ACD-SHAPER-V2-MIB", "acdShaperV2QueueStatsHistGroup"))
)
if mibBuilder.loadTexts:
    acdShaperV2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SHAPER-V2-MIB",
    **{"acdShaperV2Mib": acdShaperV2Mib,
       "acdShaperV2Notifications": acdShaperV2Notifications,
       "acdShaperV2MIBObjects": acdShaperV2MIBObjects,
       "acdShaperV2QueueStatsTable": acdShaperV2QueueStatsTable,
       "acdShaperV2QueueStatsEntry": acdShaperV2QueueStatsEntry,
       "acdShaperV2QueueStatsQueueId": acdShaperV2QueueStatsQueueId,
       "acdShaperV2QueueStatsQueueName": acdShaperV2QueueStatsQueueName,
       "acdShaperV2QueueStatsCntGreenForwardNoDelayFrames": acdShaperV2QueueStatsCntGreenForwardNoDelayFrames,
       "acdShaperV2QueueStatsCntGreenForwardNoDelayBytes": acdShaperV2QueueStatsCntGreenForwardNoDelayBytes,
       "acdShaperV2QueueStatsCntYellowForwardNoDelayFrames": acdShaperV2QueueStatsCntYellowForwardNoDelayFrames,
       "acdShaperV2QueueStatsCntYellowForwardNoDelayBytes": acdShaperV2QueueStatsCntYellowForwardNoDelayBytes,
       "acdShaperV2QueueStatsCntGreenForwardWithDelayFrames": acdShaperV2QueueStatsCntGreenForwardWithDelayFrames,
       "acdShaperV2QueueStatsCntGreenForwardWithDelayBytes": acdShaperV2QueueStatsCntGreenForwardWithDelayBytes,
       "acdShaperV2QueueStatsCntYellowForwardWithDelayFrames": acdShaperV2QueueStatsCntYellowForwardWithDelayFrames,
       "acdShaperV2QueueStatsCntYellowForwardWithDelayBytes": acdShaperV2QueueStatsCntYellowForwardWithDelayBytes,
       "acdShaperV2QueueStatsCntGreenDiscardFullFrames": acdShaperV2QueueStatsCntGreenDiscardFullFrames,
       "acdShaperV2QueueStatsCntGreenDiscardFullBytes": acdShaperV2QueueStatsCntGreenDiscardFullBytes,
       "acdShaperV2QueueStatsCntYellowDiscardFullFrames": acdShaperV2QueueStatsCntYellowDiscardFullFrames,
       "acdShaperV2QueueStatsCntYellowDiscardFullBytes": acdShaperV2QueueStatsCntYellowDiscardFullBytes,
       "acdShaperV2QueueStatsCntGreenDiscardBLUEFrames": acdShaperV2QueueStatsCntGreenDiscardBLUEFrames,
       "acdShaperV2QueueStatsCntGreenDiscardBLUEBytes": acdShaperV2QueueStatsCntGreenDiscardBLUEBytes,
       "acdShaperV2QueueStatsCntYellowDiscardBLUEFrames": acdShaperV2QueueStatsCntYellowDiscardBLUEFrames,
       "acdShaperV2QueueStatsCntYellowDiscardBLUEBytes": acdShaperV2QueueStatsCntYellowDiscardBLUEBytes,
       "acdShaperV2QueueStatsCntCIRCompliantFrames": acdShaperV2QueueStatsCntCIRCompliantFrames,
       "acdShaperV2QueueStatsCntCIRCompliantBytes": acdShaperV2QueueStatsCntCIRCompliantBytes,
       "acdShaperV2QueueStatsCntEIRCompliantFrames": acdShaperV2QueueStatsCntEIRCompliantFrames,
       "acdShaperV2QueueStatsCntEIRCompliantBytes": acdShaperV2QueueStatsCntEIRCompliantBytes,
       "acdShaperV2QueueStatsHistTable": acdShaperV2QueueStatsHistTable,
       "acdShaperV2QueueStatsHistEntry": acdShaperV2QueueStatsHistEntry,
       "acdShaperV2QueueStatsHistIndex": acdShaperV2QueueStatsHistIndex,
       "acdShaperV2QueueStatsHistSamplingEndTime": acdShaperV2QueueStatsHistSamplingEndTime,
       "acdShaperV2QueueStatsHistQueueId": acdShaperV2QueueStatsHistQueueId,
       "acdShaperV2QueueStatsHistQueueName": acdShaperV2QueueStatsHistQueueName,
       "acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames": acdShaperV2QueueStatsHistCntGreenForwardNoDelayFrames,
       "acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes": acdShaperV2QueueStatsHistCntGreenForwardNoDelayBytes,
       "acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames": acdShaperV2QueueStatsHistCntYellowForwardNoDelayFrames,
       "acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes": acdShaperV2QueueStatsHistCntYellowForwardNoDelayBytes,
       "acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames": acdShaperV2QueueStatsHistCntGreenForwardWithDelayFrames,
       "acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes": acdShaperV2QueueStatsHistCntGreenForwardWithDelayBytes,
       "acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames": acdShaperV2QueueStatsHistCntYellowForwardWithDelayFrames,
       "acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes": acdShaperV2QueueStatsHistCntYellowForwardWithDelayBytes,
       "acdShaperV2QueueStatsHistCntGreenDiscardFullFrames": acdShaperV2QueueStatsHistCntGreenDiscardFullFrames,
       "acdShaperV2QueueStatsHistCntGreenDiscardFullBytes": acdShaperV2QueueStatsHistCntGreenDiscardFullBytes,
       "acdShaperV2QueueStatsHistCntYellowDiscardFullFrames": acdShaperV2QueueStatsHistCntYellowDiscardFullFrames,
       "acdShaperV2QueueStatsHistCntYellowDiscardFullBytes": acdShaperV2QueueStatsHistCntYellowDiscardFullBytes,
       "acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames": acdShaperV2QueueStatsHistCntGreenDiscardBLUEFrames,
       "acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes": acdShaperV2QueueStatsHistCntGreenDiscardBLUEBytes,
       "acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames": acdShaperV2QueueStatsHistCntYellowDiscardBLUEFrames,
       "acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes": acdShaperV2QueueStatsHistCntYellowDiscardBLUEBytes,
       "acdShaperV2QueueStatsHistCntCIRCompliantFrames": acdShaperV2QueueStatsHistCntCIRCompliantFrames,
       "acdShaperV2QueueStatsHistCntCIRCompliantBytes": acdShaperV2QueueStatsHistCntCIRCompliantBytes,
       "acdShaperV2QueueStatsHistCntEIRCompliantFrames": acdShaperV2QueueStatsHistCntEIRCompliantFrames,
       "acdShaperV2QueueStatsHistCntEIRCompliantBytes": acdShaperV2QueueStatsHistCntEIRCompliantBytes,
       "acdShaperV2Conformance": acdShaperV2Conformance,
       "acdShaperV2Compliances": acdShaperV2Compliances,
       "acdShaperV2Compliance": acdShaperV2Compliance,
       "acdShaperV2Groups": acdShaperV2Groups,
       "acdShaperV2QueueStatsGroup": acdShaperV2QueueStatsGroup,
       "acdShaperV2QueueStatsHistGroup": acdShaperV2QueueStatsHistGroup}
)
