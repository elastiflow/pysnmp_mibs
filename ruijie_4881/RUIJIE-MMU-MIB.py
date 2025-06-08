# SNMP MIB module (RUIJIE-MMU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-MMU-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:12 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieMMUMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141)
)
if mibBuilder.loadTexts:
    ruijieMMUMIB.setRevisions(
        ("2015-06-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieMmuIfVoqInTable_Object = MibTable
ruijieMmuIfVoqInTable = _RuijieMmuIfVoqInTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1)
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqInTable.setStatus("current")
_RuijieMmuIfVoqInEntry_Object = MibTableRow
ruijieMmuIfVoqInEntry = _RuijieMmuIfVoqInEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1)
)
ruijieMmuIfVoqInEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieInIfxId"),
    (0, "RUIJIE-MMU-MIB", "ruijieInQueueId"),
    (0, "RUIJIE-MMU-MIB", "ruijieInDevId"),
    (0, "RUIJIE-MMU-MIB", "ruijieInSlotId"),
    (0, "RUIJIE-MMU-MIB", "ruijieInPgId"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqInEntry.setStatus("current")
_RuijieInIfxId_Type = IfIndex
_RuijieInIfxId_Object = MibTableColumn
ruijieInIfxId = _RuijieInIfxId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 1),
    _RuijieInIfxId_Type()
)
ruijieInIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInIfxId.setStatus("current")
_RuijieInQueueId_Type = Integer32
_RuijieInQueueId_Object = MibTableColumn
ruijieInQueueId = _RuijieInQueueId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 2),
    _RuijieInQueueId_Type()
)
ruijieInQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInQueueId.setStatus("current")
_RuijieInDevId_Type = Integer32
_RuijieInDevId_Object = MibTableColumn
ruijieInDevId = _RuijieInDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 3),
    _RuijieInDevId_Type()
)
ruijieInDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInDevId.setStatus("current")
_RuijieInSlotId_Type = Integer32
_RuijieInSlotId_Object = MibTableColumn
ruijieInSlotId = _RuijieInSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 4),
    _RuijieInSlotId_Type()
)
ruijieInSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInSlotId.setStatus("current")
_RuijieInPgId_Type = Integer32
_RuijieInPgId_Object = MibTableColumn
ruijieInPgId = _RuijieInPgId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 5),
    _RuijieInPgId_Type()
)
ruijieInPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInPgId.setStatus("current")
_RuijieInTransmitPackets_Type = Counter64
_RuijieInTransmitPackets_Object = MibTableColumn
ruijieInTransmitPackets = _RuijieInTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 6),
    _RuijieInTransmitPackets_Type()
)
ruijieInTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInTransmitPackets.setStatus("current")
_RuijieInTransmitBytes_Type = Counter64
_RuijieInTransmitBytes_Object = MibTableColumn
ruijieInTransmitBytes = _RuijieInTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 7),
    _RuijieInTransmitBytes_Type()
)
ruijieInTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInTransmitBytes.setStatus("current")
_RuijieInDropPackets_Type = Counter64
_RuijieInDropPackets_Object = MibTableColumn
ruijieInDropPackets = _RuijieInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 8),
    _RuijieInDropPackets_Type()
)
ruijieInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInDropPackets.setStatus("current")
_RuijieInDropBytes_Type = Counter64
_RuijieInDropBytes_Object = MibTableColumn
ruijieInDropBytes = _RuijieInDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 1, 1, 9),
    _RuijieInDropBytes_Type()
)
ruijieInDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieInDropBytes.setStatus("current")
_RuijieMmuIfVoqOutTable_Object = MibTable
ruijieMmuIfVoqOutTable = _RuijieMmuIfVoqOutTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2)
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqOutTable.setStatus("current")
_RuijieMmuIfVoqOutEntry_Object = MibTableRow
ruijieMmuIfVoqOutEntry = _RuijieMmuIfVoqOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1)
)
ruijieMmuIfVoqOutEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieOutIfxId"),
    (0, "RUIJIE-MMU-MIB", "ruijieOutQueueId"),
    (0, "RUIJIE-MMU-MIB", "ruijieOutDevId"),
    (0, "RUIJIE-MMU-MIB", "ruijieOutSlotId"),
    (0, "RUIJIE-MMU-MIB", "ruijieOutPgId"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqOutEntry.setStatus("current")
_RuijieOutIfxId_Type = IfIndex
_RuijieOutIfxId_Object = MibTableColumn
ruijieOutIfxId = _RuijieOutIfxId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 1),
    _RuijieOutIfxId_Type()
)
ruijieOutIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutIfxId.setStatus("current")
_RuijieOutQueueId_Type = Integer32
_RuijieOutQueueId_Object = MibTableColumn
ruijieOutQueueId = _RuijieOutQueueId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 2),
    _RuijieOutQueueId_Type()
)
ruijieOutQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutQueueId.setStatus("current")
_RuijieOutDevId_Type = Integer32
_RuijieOutDevId_Object = MibTableColumn
ruijieOutDevId = _RuijieOutDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 3),
    _RuijieOutDevId_Type()
)
ruijieOutDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutDevId.setStatus("current")
_RuijieOutSlotId_Type = Integer32
_RuijieOutSlotId_Object = MibTableColumn
ruijieOutSlotId = _RuijieOutSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 4),
    _RuijieOutSlotId_Type()
)
ruijieOutSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutSlotId.setStatus("current")
_RuijieOutPgId_Type = Integer32
_RuijieOutPgId_Object = MibTableColumn
ruijieOutPgId = _RuijieOutPgId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 5),
    _RuijieOutPgId_Type()
)
ruijieOutPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutPgId.setStatus("current")
_RuijieOutTransmitPackets_Type = Counter64
_RuijieOutTransmitPackets_Object = MibTableColumn
ruijieOutTransmitPackets = _RuijieOutTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 6),
    _RuijieOutTransmitPackets_Type()
)
ruijieOutTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutTransmitPackets.setStatus("current")
_RuijieOutTransmitBytes_Type = Counter64
_RuijieOutTransmitBytes_Object = MibTableColumn
ruijieOutTransmitBytes = _RuijieOutTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 7),
    _RuijieOutTransmitBytes_Type()
)
ruijieOutTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutTransmitBytes.setStatus("current")
_RuijieOutDropPackets_Type = Counter64
_RuijieOutDropPackets_Object = MibTableColumn
ruijieOutDropPackets = _RuijieOutDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 8),
    _RuijieOutDropPackets_Type()
)
ruijieOutDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutDropPackets.setStatus("current")
_RuijieOutDropBytes_Type = Counter64
_RuijieOutDropBytes_Object = MibTableColumn
ruijieOutDropBytes = _RuijieOutDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 2, 1, 9),
    _RuijieOutDropBytes_Type()
)
ruijieOutDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieOutDropBytes.setStatus("current")
_RuijieMmuIfWarnTable_Object = MibTable
ruijieMmuIfWarnTable = _RuijieMmuIfWarnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3)
)
if mibBuilder.loadTexts:
    ruijieMmuIfWarnTable.setStatus("current")
_RuijieMmuIfWarnEntry_Object = MibTableRow
ruijieMmuIfWarnEntry = _RuijieMmuIfWarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1)
)
ruijieMmuIfWarnEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieWarnIfxId"),
    (0, "RUIJIE-MMU-MIB", "ruijieWarnDevId"),
    (0, "RUIJIE-MMU-MIB", "ruijieWarnSlotId"),
    (0, "RUIJIE-MMU-MIB", "ruijieWarnPgId"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfWarnEntry.setStatus("current")
_RuijieWarnIfxId_Type = IfIndex
_RuijieWarnIfxId_Object = MibTableColumn
ruijieWarnIfxId = _RuijieWarnIfxId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 1),
    _RuijieWarnIfxId_Type()
)
ruijieWarnIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnIfxId.setStatus("current")
_RuijieWarnDevId_Type = Integer32
_RuijieWarnDevId_Object = MibTableColumn
ruijieWarnDevId = _RuijieWarnDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 2),
    _RuijieWarnDevId_Type()
)
ruijieWarnDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnDevId.setStatus("current")
_RuijieWarnSlotId_Type = Integer32
_RuijieWarnSlotId_Object = MibTableColumn
ruijieWarnSlotId = _RuijieWarnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 3),
    _RuijieWarnSlotId_Type()
)
ruijieWarnSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnSlotId.setStatus("current")
_RuijieWarnPgId_Type = Integer32
_RuijieWarnPgId_Object = MibTableColumn
ruijieWarnPgId = _RuijieWarnPgId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 4),
    _RuijieWarnPgId_Type()
)
ruijieWarnPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnPgId.setStatus("current")
_RuijieWarnUsedCell_Type = Integer32
_RuijieWarnUsedCell_Object = MibTableColumn
ruijieWarnUsedCell = _RuijieWarnUsedCell_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 5),
    _RuijieWarnUsedCell_Type()
)
ruijieWarnUsedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnUsedCell.setStatus("current")
_RuijieWarnTotalCell_Type = Integer32
_RuijieWarnTotalCell_Object = MibTableColumn
ruijieWarnTotalCell = _RuijieWarnTotalCell_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 6),
    _RuijieWarnTotalCell_Type()
)
ruijieWarnTotalCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnTotalCell.setStatus("current")
_RuijieWarnLimit_Type = Integer32
_RuijieWarnLimit_Object = MibTableColumn
ruijieWarnLimit = _RuijieWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 7),
    _RuijieWarnLimit_Type()
)
ruijieWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnLimit.setStatus("current")
_RuijieWarnCount_Type = Integer32
_RuijieWarnCount_Object = MibTableColumn
ruijieWarnCount = _RuijieWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 3, 1, 8),
    _RuijieWarnCount_Type()
)
ruijieWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWarnCount.setStatus("current")
_RuijieMmuIfVoqWarnTable_Object = MibTable
ruijieMmuIfVoqWarnTable = _RuijieMmuIfVoqWarnTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4)
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqWarnTable.setStatus("current")
_RuijieMmuIfVoqWarnEntry_Object = MibTableRow
ruijieMmuIfVoqWarnEntry = _RuijieMmuIfVoqWarnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1)
)
ruijieMmuIfVoqWarnEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieVoqWarnIfxId"),
    (0, "RUIJIE-MMU-MIB", "ruijieVoqWarnQueueId"),
    (0, "RUIJIE-MMU-MIB", "ruijieVoqWarnDevId"),
    (0, "RUIJIE-MMU-MIB", "ruijieVoqWarnSlotId"),
    (0, "RUIJIE-MMU-MIB", "ruijieVoqWarnPgId"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfVoqWarnEntry.setStatus("current")
_RuijieVoqWarnIfxId_Type = IfIndex
_RuijieVoqWarnIfxId_Object = MibTableColumn
ruijieVoqWarnIfxId = _RuijieVoqWarnIfxId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 1),
    _RuijieVoqWarnIfxId_Type()
)
ruijieVoqWarnIfxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnIfxId.setStatus("current")
_RuijieVoqWarnQueueId_Type = Integer32
_RuijieVoqWarnQueueId_Object = MibTableColumn
ruijieVoqWarnQueueId = _RuijieVoqWarnQueueId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 2),
    _RuijieVoqWarnQueueId_Type()
)
ruijieVoqWarnQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnQueueId.setStatus("current")
_RuijieVoqWarnDevId_Type = Integer32
_RuijieVoqWarnDevId_Object = MibTableColumn
ruijieVoqWarnDevId = _RuijieVoqWarnDevId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 3),
    _RuijieVoqWarnDevId_Type()
)
ruijieVoqWarnDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnDevId.setStatus("current")
_RuijieVoqWarnSlotId_Type = Integer32
_RuijieVoqWarnSlotId_Object = MibTableColumn
ruijieVoqWarnSlotId = _RuijieVoqWarnSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 4),
    _RuijieVoqWarnSlotId_Type()
)
ruijieVoqWarnSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnSlotId.setStatus("current")
_RuijieVoqWarnPgId_Type = Integer32
_RuijieVoqWarnPgId_Object = MibTableColumn
ruijieVoqWarnPgId = _RuijieVoqWarnPgId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 5),
    _RuijieVoqWarnPgId_Type()
)
ruijieVoqWarnPgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnPgId.setStatus("current")
_RuijieVoqWarnUsedcells_Type = Counter64
_RuijieVoqWarnUsedcells_Object = MibTableColumn
ruijieVoqWarnUsedcells = _RuijieVoqWarnUsedcells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 6),
    _RuijieVoqWarnUsedcells_Type()
)
ruijieVoqWarnUsedcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnUsedcells.setStatus("current")
_RuijieVoqWarnAvailablecells_Type = Counter64
_RuijieVoqWarnAvailablecells_Object = MibTableColumn
ruijieVoqWarnAvailablecells = _RuijieVoqWarnAvailablecells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 7),
    _RuijieVoqWarnAvailablecells_Type()
)
ruijieVoqWarnAvailablecells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnAvailablecells.setStatus("current")
_RuijieVoqWarnTotalcells_Type = Counter64
_RuijieVoqWarnTotalcells_Object = MibTableColumn
ruijieVoqWarnTotalcells = _RuijieVoqWarnTotalcells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 8),
    _RuijieVoqWarnTotalcells_Type()
)
ruijieVoqWarnTotalcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnTotalcells.setStatus("current")
_RuijieVoqWarnUsage_Type = Counter64
_RuijieVoqWarnUsage_Object = MibTableColumn
ruijieVoqWarnUsage = _RuijieVoqWarnUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 9),
    _RuijieVoqWarnUsage_Type()
)
ruijieVoqWarnUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnUsage.setStatus("current")
_RuijieVoqWarnUsagewarnlimit_Type = Counter64
_RuijieVoqWarnUsagewarnlimit_Object = MibTableColumn
ruijieVoqWarnUsagewarnlimit = _RuijieVoqWarnUsagewarnlimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 10),
    _RuijieVoqWarnUsagewarnlimit_Type()
)
ruijieVoqWarnUsagewarnlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnUsagewarnlimit.setStatus("current")
_RuijieVoqWarnUsagewarncount_Type = Counter64
_RuijieVoqWarnUsagewarncount_Object = MibTableColumn
ruijieVoqWarnUsagewarncount = _RuijieVoqWarnUsagewarncount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 11),
    _RuijieVoqWarnUsagewarncount_Type()
)
ruijieVoqWarnUsagewarncount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnUsagewarncount.setStatus("current")
_RuijieVoqWarnPeakedcells_Type = Counter64
_RuijieVoqWarnPeakedcells_Object = MibTableColumn
ruijieVoqWarnPeakedcells = _RuijieVoqWarnPeakedcells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 4, 1, 12),
    _RuijieVoqWarnPeakedcells_Type()
)
ruijieVoqWarnPeakedcells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieVoqWarnPeakedcells.setStatus("current")
_RuijieMmuIfQueueSupportTable_Object = MibTable
ruijieMmuIfQueueSupportTable = _RuijieMmuIfQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5)
)
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportTable.setStatus("current")
_RuijieMmuIfQueueSupportEntry_Object = MibTableRow
ruijieMmuIfQueueSupportEntry = _RuijieMmuIfQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1)
)
ruijieMmuIfQueueSupportEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfIndex"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfQueueIndex"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfSliceIndex"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportEntry.setStatus("current")
_RuijieMmuIfIndex_Type = IfIndex
_RuijieMmuIfIndex_Object = MibTableColumn
ruijieMmuIfIndex = _RuijieMmuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 1),
    _RuijieMmuIfIndex_Type()
)
ruijieMmuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfIndex.setStatus("current")
_RuijieMmuIfQueueIndex_Type = Integer32
_RuijieMmuIfQueueIndex_Object = MibTableColumn
ruijieMmuIfQueueIndex = _RuijieMmuIfQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 2),
    _RuijieMmuIfQueueIndex_Type()
)
ruijieMmuIfQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueIndex.setStatus("current")
_RuijieMmuIfSliceIndex_Type = Integer32
_RuijieMmuIfSliceIndex_Object = MibTableColumn
ruijieMmuIfSliceIndex = _RuijieMmuIfSliceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 3),
    _RuijieMmuIfSliceIndex_Type()
)
ruijieMmuIfSliceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfSliceIndex.setStatus("current")
_RuijieMmuIfQueueSupportUsedCells_Type = Counter64
_RuijieMmuIfQueueSupportUsedCells_Object = MibTableColumn
ruijieMmuIfQueueSupportUsedCells = _RuijieMmuIfQueueSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 4),
    _RuijieMmuIfQueueSupportUsedCells_Type()
)
ruijieMmuIfQueueSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportUsedCells.setStatus("current")
_RuijieMmuIfQueueSupportAvailableCells_Type = Counter64
_RuijieMmuIfQueueSupportAvailableCells_Object = MibTableColumn
ruijieMmuIfQueueSupportAvailableCells = _RuijieMmuIfQueueSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 5),
    _RuijieMmuIfQueueSupportAvailableCells_Type()
)
ruijieMmuIfQueueSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportAvailableCells.setStatus("current")
_RuijieMmuIfQueueSupportTotalCells_Type = Counter64
_RuijieMmuIfQueueSupportTotalCells_Object = MibTableColumn
ruijieMmuIfQueueSupportTotalCells = _RuijieMmuIfQueueSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 6),
    _RuijieMmuIfQueueSupportTotalCells_Type()
)
ruijieMmuIfQueueSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportTotalCells.setStatus("current")
_RuijieMmuIfQueueSupportUsage_Type = Counter64
_RuijieMmuIfQueueSupportUsage_Object = MibTableColumn
ruijieMmuIfQueueSupportUsage = _RuijieMmuIfQueueSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 7),
    _RuijieMmuIfQueueSupportUsage_Type()
)
ruijieMmuIfQueueSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportUsage.setStatus("current")
_RuijieMmuIfQueueSupportUsageWarnLimit_Type = Counter64
_RuijieMmuIfQueueSupportUsageWarnLimit_Object = MibTableColumn
ruijieMmuIfQueueSupportUsageWarnLimit = _RuijieMmuIfQueueSupportUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 8),
    _RuijieMmuIfQueueSupportUsageWarnLimit_Type()
)
ruijieMmuIfQueueSupportUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportUsageWarnLimit.setStatus("current")
_RuijieMmuIfQueueSupportUsageWarnCount_Type = Counter64
_RuijieMmuIfQueueSupportUsageWarnCount_Object = MibTableColumn
ruijieMmuIfQueueSupportUsageWarnCount = _RuijieMmuIfQueueSupportUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 9),
    _RuijieMmuIfQueueSupportUsageWarnCount_Type()
)
ruijieMmuIfQueueSupportUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportUsageWarnCount.setStatus("current")
_RuijieMmuIfQueueSupportPeakedCells_Type = Counter64
_RuijieMmuIfQueueSupportPeakedCells_Object = MibTableColumn
ruijieMmuIfQueueSupportPeakedCells = _RuijieMmuIfQueueSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 10),
    _RuijieMmuIfQueueSupportPeakedCells_Type()
)
ruijieMmuIfQueueSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportPeakedCells.setStatus("current")
_RuijieMmuIfQueueSupportServicePoolID_Type = Counter64
_RuijieMmuIfQueueSupportServicePoolID_Object = MibTableColumn
ruijieMmuIfQueueSupportServicePoolID = _RuijieMmuIfQueueSupportServicePoolID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 5, 1, 11),
    _RuijieMmuIfQueueSupportServicePoolID_Type()
)
ruijieMmuIfQueueSupportServicePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfQueueSupportServicePoolID.setStatus("current")
_RuijieMmuIfMulticastQueueSupportTable_Object = MibTable
ruijieMmuIfMulticastQueueSupportTable = _RuijieMmuIfMulticastQueueSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6)
)
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportTable.setStatus("current")
_RuijieMmuIfMulticastQueueSupportEntry_Object = MibTableRow
ruijieMmuIfMulticastQueueSupportEntry = _RuijieMmuIfMulticastQueueSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1)
)
ruijieMmuIfMulticastQueueSupportEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfIndexMulticast"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfMulticastQueueIndex"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfSliceIndexMulticast"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportEntry.setStatus("current")
_RuijieMmuIfIndexMulticast_Type = IfIndex
_RuijieMmuIfIndexMulticast_Object = MibTableColumn
ruijieMmuIfIndexMulticast = _RuijieMmuIfIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 1),
    _RuijieMmuIfIndexMulticast_Type()
)
ruijieMmuIfIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfIndexMulticast.setStatus("current")
_RuijieMmuIfMulticastQueueIndex_Type = Integer32
_RuijieMmuIfMulticastQueueIndex_Object = MibTableColumn
ruijieMmuIfMulticastQueueIndex = _RuijieMmuIfMulticastQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 2),
    _RuijieMmuIfMulticastQueueIndex_Type()
)
ruijieMmuIfMulticastQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueIndex.setStatus("current")
_RuijieMmuIfSliceIndexMulticast_Type = Integer32
_RuijieMmuIfSliceIndexMulticast_Object = MibTableColumn
ruijieMmuIfSliceIndexMulticast = _RuijieMmuIfSliceIndexMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 3),
    _RuijieMmuIfSliceIndexMulticast_Type()
)
ruijieMmuIfSliceIndexMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfSliceIndexMulticast.setStatus("current")
_RuijieMmuIfMulticastQueueSupportUsedCells_Type = Counter64
_RuijieMmuIfMulticastQueueSupportUsedCells_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportUsedCells = _RuijieMmuIfMulticastQueueSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 4),
    _RuijieMmuIfMulticastQueueSupportUsedCells_Type()
)
ruijieMmuIfMulticastQueueSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportUsedCells.setStatus("current")
_RuijieMmuIfMulticastQueueSupportAvailableCells_Type = Counter64
_RuijieMmuIfMulticastQueueSupportAvailableCells_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportAvailableCells = _RuijieMmuIfMulticastQueueSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 5),
    _RuijieMmuIfMulticastQueueSupportAvailableCells_Type()
)
ruijieMmuIfMulticastQueueSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportAvailableCells.setStatus("current")
_RuijieMmuIfMulticastQueueSupportTotalCells_Type = Counter64
_RuijieMmuIfMulticastQueueSupportTotalCells_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportTotalCells = _RuijieMmuIfMulticastQueueSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 6),
    _RuijieMmuIfMulticastQueueSupportTotalCells_Type()
)
ruijieMmuIfMulticastQueueSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportTotalCells.setStatus("current")
_RuijieMmuIfMulticastQueueSupportUsage_Type = Counter64
_RuijieMmuIfMulticastQueueSupportUsage_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportUsage = _RuijieMmuIfMulticastQueueSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 7),
    _RuijieMmuIfMulticastQueueSupportUsage_Type()
)
ruijieMmuIfMulticastQueueSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportUsage.setStatus("current")
_RuijieMmuIfMulticastQueueSupportUsageWarnLimit_Type = Counter64
_RuijieMmuIfMulticastQueueSupportUsageWarnLimit_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportUsageWarnLimit = _RuijieMmuIfMulticastQueueSupportUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 8),
    _RuijieMmuIfMulticastQueueSupportUsageWarnLimit_Type()
)
ruijieMmuIfMulticastQueueSupportUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportUsageWarnLimit.setStatus("current")
_RuijieMmuIfMulticastQueueSupportUsageWarnCount_Type = Counter64
_RuijieMmuIfMulticastQueueSupportUsageWarnCount_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportUsageWarnCount = _RuijieMmuIfMulticastQueueSupportUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 9),
    _RuijieMmuIfMulticastQueueSupportUsageWarnCount_Type()
)
ruijieMmuIfMulticastQueueSupportUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportUsageWarnCount.setStatus("current")
_RuijieMmuIfMulticastQueueSupportPeakedCells_Type = Counter64
_RuijieMmuIfMulticastQueueSupportPeakedCells_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportPeakedCells = _RuijieMmuIfMulticastQueueSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 10),
    _RuijieMmuIfMulticastQueueSupportPeakedCells_Type()
)
ruijieMmuIfMulticastQueueSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportPeakedCells.setStatus("current")
_RuijieMmuIfMulticastQueueSupportServicePoolID_Type = Counter64
_RuijieMmuIfMulticastQueueSupportServicePoolID_Object = MibTableColumn
ruijieMmuIfMulticastQueueSupportServicePoolID = _RuijieMmuIfMulticastQueueSupportServicePoolID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 6, 1, 11),
    _RuijieMmuIfMulticastQueueSupportServicePoolID_Type()
)
ruijieMmuIfMulticastQueueSupportServicePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfMulticastQueueSupportServicePoolID.setStatus("current")
_RuijieMmuIfPriorityGroupSupportTable_Object = MibTable
ruijieMmuIfPriorityGroupSupportTable = _RuijieMmuIfPriorityGroupSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7)
)
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportTable.setStatus("current")
_RuijieMmuIfPriorityGroupSupportEntry_Object = MibTableRow
ruijieMmuIfPriorityGroupSupportEntry = _RuijieMmuIfPriorityGroupSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1)
)
ruijieMmuIfPriorityGroupSupportEntry.setIndexNames(
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfIndexPriorityGroup"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfPriorityGroupIdIndex"),
    (0, "RUIJIE-MMU-MIB", "ruijieMmuIfSliceIndexPriorityGroup"),
)
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportEntry.setStatus("current")
_RuijieMmuIfIndexPriorityGroup_Type = IfIndex
_RuijieMmuIfIndexPriorityGroup_Object = MibTableColumn
ruijieMmuIfIndexPriorityGroup = _RuijieMmuIfIndexPriorityGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 1),
    _RuijieMmuIfIndexPriorityGroup_Type()
)
ruijieMmuIfIndexPriorityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfIndexPriorityGroup.setStatus("current")
_RuijieMmuIfPriorityGroupIdIndex_Type = Integer32
_RuijieMmuIfPriorityGroupIdIndex_Object = MibTableColumn
ruijieMmuIfPriorityGroupIdIndex = _RuijieMmuIfPriorityGroupIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 2),
    _RuijieMmuIfPriorityGroupIdIndex_Type()
)
ruijieMmuIfPriorityGroupIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupIdIndex.setStatus("current")
_RuijieMmuIfSliceIndexPriorityGroup_Type = Integer32
_RuijieMmuIfSliceIndexPriorityGroup_Object = MibTableColumn
ruijieMmuIfSliceIndexPriorityGroup = _RuijieMmuIfSliceIndexPriorityGroup_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 3),
    _RuijieMmuIfSliceIndexPriorityGroup_Type()
)
ruijieMmuIfSliceIndexPriorityGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfSliceIndexPriorityGroup.setStatus("current")
_RuijieMmuIfPriorityGroupSupportUsedCells_Type = Counter64
_RuijieMmuIfPriorityGroupSupportUsedCells_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportUsedCells = _RuijieMmuIfPriorityGroupSupportUsedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 4),
    _RuijieMmuIfPriorityGroupSupportUsedCells_Type()
)
ruijieMmuIfPriorityGroupSupportUsedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportUsedCells.setStatus("current")
_RuijieMmuIfPriorityGroupSupportAvailableCells_Type = Counter64
_RuijieMmuIfPriorityGroupSupportAvailableCells_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportAvailableCells = _RuijieMmuIfPriorityGroupSupportAvailableCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 5),
    _RuijieMmuIfPriorityGroupSupportAvailableCells_Type()
)
ruijieMmuIfPriorityGroupSupportAvailableCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportAvailableCells.setStatus("current")
_RuijieMmuIfPriorityGroupSupportTotalCells_Type = Counter64
_RuijieMmuIfPriorityGroupSupportTotalCells_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportTotalCells = _RuijieMmuIfPriorityGroupSupportTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 6),
    _RuijieMmuIfPriorityGroupSupportTotalCells_Type()
)
ruijieMmuIfPriorityGroupSupportTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportTotalCells.setStatus("current")
_RuijieMmuIfPriorityGroupSupportUsage_Type = Counter64
_RuijieMmuIfPriorityGroupSupportUsage_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportUsage = _RuijieMmuIfPriorityGroupSupportUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 7),
    _RuijieMmuIfPriorityGroupSupportUsage_Type()
)
ruijieMmuIfPriorityGroupSupportUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportUsage.setStatus("current")
_RuijieMmuIfPriorityGroupSupportPeakedCells_Type = Counter64
_RuijieMmuIfPriorityGroupSupportPeakedCells_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportPeakedCells = _RuijieMmuIfPriorityGroupSupportPeakedCells_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 8),
    _RuijieMmuIfPriorityGroupSupportPeakedCells_Type()
)
ruijieMmuIfPriorityGroupSupportPeakedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportPeakedCells.setStatus("current")
_RuijieMmuIfPriorityGroupSupportUsedHeadroom_Type = Counter64
_RuijieMmuIfPriorityGroupSupportUsedHeadroom_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportUsedHeadroom = _RuijieMmuIfPriorityGroupSupportUsedHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 9),
    _RuijieMmuIfPriorityGroupSupportUsedHeadroom_Type()
)
ruijieMmuIfPriorityGroupSupportUsedHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportUsedHeadroom.setStatus("current")
_RuijieMmuIfPriorityGroupSupportAvailableHeadroom_Type = Counter64
_RuijieMmuIfPriorityGroupSupportAvailableHeadroom_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportAvailableHeadroom = _RuijieMmuIfPriorityGroupSupportAvailableHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 10),
    _RuijieMmuIfPriorityGroupSupportAvailableHeadroom_Type()
)
ruijieMmuIfPriorityGroupSupportAvailableHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportAvailableHeadroom.setStatus("current")
_RuijieMmuIfPriorityGroupSupportPeakedHeadroom_Type = Counter64
_RuijieMmuIfPriorityGroupSupportPeakedHeadroom_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportPeakedHeadroom = _RuijieMmuIfPriorityGroupSupportPeakedHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 11),
    _RuijieMmuIfPriorityGroupSupportPeakedHeadroom_Type()
)
ruijieMmuIfPriorityGroupSupportPeakedHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportPeakedHeadroom.setStatus("current")
_RuijieMmuIfPriorityGroupSupportUsageWarnLimit_Type = Counter64
_RuijieMmuIfPriorityGroupSupportUsageWarnLimit_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportUsageWarnLimit = _RuijieMmuIfPriorityGroupSupportUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 12),
    _RuijieMmuIfPriorityGroupSupportUsageWarnLimit_Type()
)
ruijieMmuIfPriorityGroupSupportUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportUsageWarnLimit.setStatus("current")
_RuijieMmuIfPriorityGroupSupportUsageWarnCount_Type = Counter64
_RuijieMmuIfPriorityGroupSupportUsageWarnCount_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportUsageWarnCount = _RuijieMmuIfPriorityGroupSupportUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 13),
    _RuijieMmuIfPriorityGroupSupportUsageWarnCount_Type()
)
ruijieMmuIfPriorityGroupSupportUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportUsageWarnCount.setStatus("current")
_RuijieMmuIfPriorityGroupSupportServicePoolID_Type = Counter64
_RuijieMmuIfPriorityGroupSupportServicePoolID_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportServicePoolID = _RuijieMmuIfPriorityGroupSupportServicePoolID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 14),
    _RuijieMmuIfPriorityGroupSupportServicePoolID_Type()
)
ruijieMmuIfPriorityGroupSupportServicePoolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportServicePoolID.setStatus("current")
_RuijieMmuIfPriorityGroupSupportTotalHeadroom_Type = Counter64
_RuijieMmuIfPriorityGroupSupportTotalHeadroom_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportTotalHeadroom = _RuijieMmuIfPriorityGroupSupportTotalHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 15),
    _RuijieMmuIfPriorityGroupSupportTotalHeadroom_Type()
)
ruijieMmuIfPriorityGroupSupportTotalHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportTotalHeadroom.setStatus("current")
_RuijieMmuIfPriorityGroupSupportHeadroomUsage_Type = Counter64
_RuijieMmuIfPriorityGroupSupportHeadroomUsage_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportHeadroomUsage = _RuijieMmuIfPriorityGroupSupportHeadroomUsage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 16),
    _RuijieMmuIfPriorityGroupSupportHeadroomUsage_Type()
)
ruijieMmuIfPriorityGroupSupportHeadroomUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportHeadroomUsage.setStatus("current")
_RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit_Type = Counter64
_RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit = _RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 17),
    _RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit_Type()
)
ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit.setStatus("current")
_RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount_Type = Counter64
_RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount_Object = MibTableColumn
ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount = _RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 141, 7, 1, 18),
    _RuijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount_Type()
)
ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-MMU-MIB",
    **{"ruijieMMUMIB": ruijieMMUMIB,
       "ruijieMmuIfVoqInTable": ruijieMmuIfVoqInTable,
       "ruijieMmuIfVoqInEntry": ruijieMmuIfVoqInEntry,
       "ruijieInIfxId": ruijieInIfxId,
       "ruijieInQueueId": ruijieInQueueId,
       "ruijieInDevId": ruijieInDevId,
       "ruijieInSlotId": ruijieInSlotId,
       "ruijieInPgId": ruijieInPgId,
       "ruijieInTransmitPackets": ruijieInTransmitPackets,
       "ruijieInTransmitBytes": ruijieInTransmitBytes,
       "ruijieInDropPackets": ruijieInDropPackets,
       "ruijieInDropBytes": ruijieInDropBytes,
       "ruijieMmuIfVoqOutTable": ruijieMmuIfVoqOutTable,
       "ruijieMmuIfVoqOutEntry": ruijieMmuIfVoqOutEntry,
       "ruijieOutIfxId": ruijieOutIfxId,
       "ruijieOutQueueId": ruijieOutQueueId,
       "ruijieOutDevId": ruijieOutDevId,
       "ruijieOutSlotId": ruijieOutSlotId,
       "ruijieOutPgId": ruijieOutPgId,
       "ruijieOutTransmitPackets": ruijieOutTransmitPackets,
       "ruijieOutTransmitBytes": ruijieOutTransmitBytes,
       "ruijieOutDropPackets": ruijieOutDropPackets,
       "ruijieOutDropBytes": ruijieOutDropBytes,
       "ruijieMmuIfWarnTable": ruijieMmuIfWarnTable,
       "ruijieMmuIfWarnEntry": ruijieMmuIfWarnEntry,
       "ruijieWarnIfxId": ruijieWarnIfxId,
       "ruijieWarnDevId": ruijieWarnDevId,
       "ruijieWarnSlotId": ruijieWarnSlotId,
       "ruijieWarnPgId": ruijieWarnPgId,
       "ruijieWarnUsedCell": ruijieWarnUsedCell,
       "ruijieWarnTotalCell": ruijieWarnTotalCell,
       "ruijieWarnLimit": ruijieWarnLimit,
       "ruijieWarnCount": ruijieWarnCount,
       "ruijieMmuIfVoqWarnTable": ruijieMmuIfVoqWarnTable,
       "ruijieMmuIfVoqWarnEntry": ruijieMmuIfVoqWarnEntry,
       "ruijieVoqWarnIfxId": ruijieVoqWarnIfxId,
       "ruijieVoqWarnQueueId": ruijieVoqWarnQueueId,
       "ruijieVoqWarnDevId": ruijieVoqWarnDevId,
       "ruijieVoqWarnSlotId": ruijieVoqWarnSlotId,
       "ruijieVoqWarnPgId": ruijieVoqWarnPgId,
       "ruijieVoqWarnUsedcells": ruijieVoqWarnUsedcells,
       "ruijieVoqWarnAvailablecells": ruijieVoqWarnAvailablecells,
       "ruijieVoqWarnTotalcells": ruijieVoqWarnTotalcells,
       "ruijieVoqWarnUsage": ruijieVoqWarnUsage,
       "ruijieVoqWarnUsagewarnlimit": ruijieVoqWarnUsagewarnlimit,
       "ruijieVoqWarnUsagewarncount": ruijieVoqWarnUsagewarncount,
       "ruijieVoqWarnPeakedcells": ruijieVoqWarnPeakedcells,
       "ruijieMmuIfQueueSupportTable": ruijieMmuIfQueueSupportTable,
       "ruijieMmuIfQueueSupportEntry": ruijieMmuIfQueueSupportEntry,
       "ruijieMmuIfIndex": ruijieMmuIfIndex,
       "ruijieMmuIfQueueIndex": ruijieMmuIfQueueIndex,
       "ruijieMmuIfSliceIndex": ruijieMmuIfSliceIndex,
       "ruijieMmuIfQueueSupportUsedCells": ruijieMmuIfQueueSupportUsedCells,
       "ruijieMmuIfQueueSupportAvailableCells": ruijieMmuIfQueueSupportAvailableCells,
       "ruijieMmuIfQueueSupportTotalCells": ruijieMmuIfQueueSupportTotalCells,
       "ruijieMmuIfQueueSupportUsage": ruijieMmuIfQueueSupportUsage,
       "ruijieMmuIfQueueSupportUsageWarnLimit": ruijieMmuIfQueueSupportUsageWarnLimit,
       "ruijieMmuIfQueueSupportUsageWarnCount": ruijieMmuIfQueueSupportUsageWarnCount,
       "ruijieMmuIfQueueSupportPeakedCells": ruijieMmuIfQueueSupportPeakedCells,
       "ruijieMmuIfQueueSupportServicePoolID": ruijieMmuIfQueueSupportServicePoolID,
       "ruijieMmuIfMulticastQueueSupportTable": ruijieMmuIfMulticastQueueSupportTable,
       "ruijieMmuIfMulticastQueueSupportEntry": ruijieMmuIfMulticastQueueSupportEntry,
       "ruijieMmuIfIndexMulticast": ruijieMmuIfIndexMulticast,
       "ruijieMmuIfMulticastQueueIndex": ruijieMmuIfMulticastQueueIndex,
       "ruijieMmuIfSliceIndexMulticast": ruijieMmuIfSliceIndexMulticast,
       "ruijieMmuIfMulticastQueueSupportUsedCells": ruijieMmuIfMulticastQueueSupportUsedCells,
       "ruijieMmuIfMulticastQueueSupportAvailableCells": ruijieMmuIfMulticastQueueSupportAvailableCells,
       "ruijieMmuIfMulticastQueueSupportTotalCells": ruijieMmuIfMulticastQueueSupportTotalCells,
       "ruijieMmuIfMulticastQueueSupportUsage": ruijieMmuIfMulticastQueueSupportUsage,
       "ruijieMmuIfMulticastQueueSupportUsageWarnLimit": ruijieMmuIfMulticastQueueSupportUsageWarnLimit,
       "ruijieMmuIfMulticastQueueSupportUsageWarnCount": ruijieMmuIfMulticastQueueSupportUsageWarnCount,
       "ruijieMmuIfMulticastQueueSupportPeakedCells": ruijieMmuIfMulticastQueueSupportPeakedCells,
       "ruijieMmuIfMulticastQueueSupportServicePoolID": ruijieMmuIfMulticastQueueSupportServicePoolID,
       "ruijieMmuIfPriorityGroupSupportTable": ruijieMmuIfPriorityGroupSupportTable,
       "ruijieMmuIfPriorityGroupSupportEntry": ruijieMmuIfPriorityGroupSupportEntry,
       "ruijieMmuIfIndexPriorityGroup": ruijieMmuIfIndexPriorityGroup,
       "ruijieMmuIfPriorityGroupIdIndex": ruijieMmuIfPriorityGroupIdIndex,
       "ruijieMmuIfSliceIndexPriorityGroup": ruijieMmuIfSliceIndexPriorityGroup,
       "ruijieMmuIfPriorityGroupSupportUsedCells": ruijieMmuIfPriorityGroupSupportUsedCells,
       "ruijieMmuIfPriorityGroupSupportAvailableCells": ruijieMmuIfPriorityGroupSupportAvailableCells,
       "ruijieMmuIfPriorityGroupSupportTotalCells": ruijieMmuIfPriorityGroupSupportTotalCells,
       "ruijieMmuIfPriorityGroupSupportUsage": ruijieMmuIfPriorityGroupSupportUsage,
       "ruijieMmuIfPriorityGroupSupportPeakedCells": ruijieMmuIfPriorityGroupSupportPeakedCells,
       "ruijieMmuIfPriorityGroupSupportUsedHeadroom": ruijieMmuIfPriorityGroupSupportUsedHeadroom,
       "ruijieMmuIfPriorityGroupSupportAvailableHeadroom": ruijieMmuIfPriorityGroupSupportAvailableHeadroom,
       "ruijieMmuIfPriorityGroupSupportPeakedHeadroom": ruijieMmuIfPriorityGroupSupportPeakedHeadroom,
       "ruijieMmuIfPriorityGroupSupportUsageWarnLimit": ruijieMmuIfPriorityGroupSupportUsageWarnLimit,
       "ruijieMmuIfPriorityGroupSupportUsageWarnCount": ruijieMmuIfPriorityGroupSupportUsageWarnCount,
       "ruijieMmuIfPriorityGroupSupportServicePoolID": ruijieMmuIfPriorityGroupSupportServicePoolID,
       "ruijieMmuIfPriorityGroupSupportTotalHeadroom": ruijieMmuIfPriorityGroupSupportTotalHeadroom,
       "ruijieMmuIfPriorityGroupSupportHeadroomUsage": ruijieMmuIfPriorityGroupSupportHeadroomUsage,
       "ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit": ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnLimit,
       "ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount": ruijieMmuIfPriorityGroupSupportHeadroomUsageWarnCount}
)
