# SNMP MIB module (ZYXEL-SESCOMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/zyxel_890/ZYXEL-SESCOMMON-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 08:35:51 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(sesSeriesCommon,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "sesSeriesCommon")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SesLineStatusTable_Object = MibTable
sesLineStatusTable = _SesLineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sesLineStatusTable.setStatus("mandatory")
_SesLineStatusEntry_Object = MibTableRow
sesLineStatusEntry = _SesLineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1)
)
sesLineStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sesLineStatusEntry.setStatus("mandatory")
_SesLineUptime_Type = TimeTicks
_SesLineUptime_Object = MibTableColumn
sesLineUptime = _SesLineUptime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 1),
    _SesLineUptime_Type()
)
sesLineUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineUptime.setStatus("mandatory")
_SesLineLinkDown_Type = Counter32
_SesLineLinkDown_Object = MibTableColumn
sesLineLinkDown = _SesLineLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 2),
    _SesLineLinkDown_Type()
)
sesLineLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineLinkDown.setStatus("mandatory")
_SesLineNMdefect_Type = Counter32
_SesLineNMdefect_Object = MibTableColumn
sesLineNMdefect = _SesLineNMdefect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 3),
    _SesLineNMdefect_Type()
)
sesLineNMdefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineNMdefect.setStatus("mandatory")
_SesLineHECdefect_Type = Counter32
_SesLineHECdefect_Object = MibTableColumn
sesLineHECdefect = _SesLineHECdefect_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 4),
    _SesLineHECdefect_Type()
)
sesLineHECdefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineHECdefect.setStatus("mandatory")
_SesLineTxPackets_Type = Counter32
_SesLineTxPackets_Object = MibTableColumn
sesLineTxPackets = _SesLineTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 5),
    _SesLineTxPackets_Type()
)
sesLineTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineTxPackets.setStatus("mandatory")
_SesLineRxPackets_Type = Counter32
_SesLineRxPackets_Object = MibTableColumn
sesLineRxPackets = _SesLineRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 6),
    _SesLineRxPackets_Type()
)
sesLineRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineRxPackets.setStatus("mandatory")
_SesLineTxFrames_Type = Counter32
_SesLineTxFrames_Object = MibTableColumn
sesLineTxFrames = _SesLineTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 7),
    _SesLineTxFrames_Type()
)
sesLineTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineTxFrames.setStatus("mandatory")
_SesLineRxFrames_Type = Counter32
_SesLineRxFrames_Object = MibTableColumn
sesLineRxFrames = _SesLineRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 8),
    _SesLineRxFrames_Type()
)
sesLineRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineRxFrames.setStatus("mandatory")
_SesLineTxCells_Type = Counter32
_SesLineTxCells_Object = MibTableColumn
sesLineTxCells = _SesLineTxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 9),
    _SesLineTxCells_Type()
)
sesLineTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineTxCells.setStatus("mandatory")
_SesLineRxCells_Type = Counter32
_SesLineRxCells_Object = MibTableColumn
sesLineRxCells = _SesLineRxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 1, 1, 10),
    _SesLineRxCells_Type()
)
sesLineRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesLineRxCells.setStatus("mandatory")
_SesMaxNumOfProfiles_Type = Integer32
_SesMaxNumOfProfiles_Object = MibScalar
sesMaxNumOfProfiles = _SesMaxNumOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 2),
    _SesMaxNumOfProfiles_Type()
)
sesMaxNumOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesMaxNumOfProfiles.setStatus("mandatory")
_SesLineConfTable_Object = MibTable
sesLineConfTable = _SesLineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sesLineConfTable.setStatus("mandatory")
_SesLineConfEntry_Object = MibTableRow
sesLineConfEntry = _SesLineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 3, 1)
)
sesLineConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sesLineConfEntry.setStatus("mandatory")


class _SesLineConfEncap_Type(Integer32):
    """Custom type sesLineConfEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_SesLineConfEncap_Type.__name__ = "Integer32"
_SesLineConfEncap_Object = MibTableColumn
sesLineConfEncap = _SesLineConfEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 3, 1, 1),
    _SesLineConfEncap_Type()
)
sesLineConfEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesLineConfEncap.setStatus("mandatory")
_SesLineConfVpi_Type = Integer32
_SesLineConfVpi_Object = MibTableColumn
sesLineConfVpi = _SesLineConfVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 3, 1, 2),
    _SesLineConfVpi_Type()
)
sesLineConfVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesLineConfVpi.setStatus("mandatory")
_SesLineConfVci_Type = Integer32
_SesLineConfVci_Object = MibTableColumn
sesLineConfVci = _SesLineConfVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 3, 1, 3),
    _SesLineConfVci_Type()
)
sesLineConfVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesLineConfVci.setStatus("mandatory")
_SesMaxNumOfPortBondings_Type = Integer32
_SesMaxNumOfPortBondings_Object = MibScalar
sesMaxNumOfPortBondings = _SesMaxNumOfPortBondings_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 4),
    _SesMaxNumOfPortBondings_Type()
)
sesMaxNumOfPortBondings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sesMaxNumOfPortBondings.setStatus("mandatory")
_SesPortBondingTable_Object = MibTable
sesPortBondingTable = _SesPortBondingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5)
)
if mibBuilder.loadTexts:
    sesPortBondingTable.setStatus("mandatory")
_SesPortBondingEntry_Object = MibTableRow
sesPortBondingEntry = _SesPortBondingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1)
)
sesPortBondingEntry.setIndexNames(
    (1, "ZYXEL-SESCOMMON-MIB", "sesPortBondingName"),
)
if mibBuilder.loadTexts:
    sesPortBondingEntry.setStatus("mandatory")


class _SesPortBondingName_Type(DisplayString):
    """Custom type sesPortBondingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SesPortBondingName_Type.__name__ = "DisplayString"
_SesPortBondingName_Object = MibTableColumn
sesPortBondingName = _SesPortBondingName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1, 1),
    _SesPortBondingName_Type()
)
sesPortBondingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sesPortBondingName.setStatus("mandatory")
_SesPortBondingNumOfMembers_Type = Integer32
_SesPortBondingNumOfMembers_Object = MibTableColumn
sesPortBondingNumOfMembers = _SesPortBondingNumOfMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1, 2),
    _SesPortBondingNumOfMembers_Type()
)
sesPortBondingNumOfMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesPortBondingNumOfMembers.setStatus("mandatory")
_SesPortBondingMemberList_Type = OctetString
_SesPortBondingMemberList_Object = MibTableColumn
sesPortBondingMemberList = _SesPortBondingMemberList_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1, 3),
    _SesPortBondingMemberList_Type()
)
sesPortBondingMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesPortBondingMemberList.setStatus("mandatory")


class _SesPortBondingMode_Type(Integer32):
    """Custom type sesPortBondingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("twoWireC", 1),
          ("twoWireR", 2),
          ("fourWireC", 3),
          ("fourWireR", 4),
          ("eightWireC", 5),
          ("eightWireR", 6))
    )


_SesPortBondingMode_Type.__name__ = "Integer32"
_SesPortBondingMode_Object = MibTableColumn
sesPortBondingMode = _SesPortBondingMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1, 4),
    _SesPortBondingMode_Type()
)
sesPortBondingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesPortBondingMode.setStatus("mandatory")
_SesPortBondingRowStatus_Type = RowStatus
_SesPortBondingRowStatus_Object = MibTableColumn
sesPortBondingRowStatus = _SesPortBondingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 5, 1, 5),
    _SesPortBondingRowStatus_Type()
)
sesPortBondingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesPortBondingRowStatus.setStatus("mandatory")
_SesNwireTable_Object = MibTable
sesNwireTable = _SesNwireTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6)
)
if mibBuilder.loadTexts:
    sesNwireTable.setStatus("mandatory")
_SesNwireEntry_Object = MibTableRow
sesNwireEntry = _SesNwireEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6, 1)
)
sesNwireEntry.setIndexNames(
    (1, "ZYXEL-SESCOMMON-MIB", "sesNwireGroupName"),
)
if mibBuilder.loadTexts:
    sesNwireEntry.setStatus("mandatory")


class _SesNwireGroupName_Type(DisplayString):
    """Custom type sesNwireGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SesNwireGroupName_Type.__name__ = "DisplayString"
_SesNwireGroupName_Object = MibTableColumn
sesNwireGroupName = _SesNwireGroupName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6, 1, 1),
    _SesNwireGroupName_Type()
)
sesNwireGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sesNwireGroupName.setStatus("mandatory")
_SesNwireGroupNumber_Type = OctetString
_SesNwireGroupNumber_Object = MibTableColumn
sesNwireGroupNumber = _SesNwireGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6, 1, 2),
    _SesNwireGroupNumber_Type()
)
sesNwireGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesNwireGroupNumber.setStatus("mandatory")


class _SesNwireMode_Type(Integer32):
    """Custom type sesNwireMode based on Integer32"""
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
        *(("fourWireC", 1),
          ("fourWireR", 2),
          ("eightWireC", 3),
          ("eightWireR", 4))
    )


_SesNwireMode_Type.__name__ = "Integer32"
_SesNwireMode_Object = MibTableColumn
sesNwireMode = _SesNwireMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6, 1, 3),
    _SesNwireMode_Type()
)
sesNwireMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesNwireMode.setStatus("mandatory")
_SesNwireRowStatus_Type = RowStatus
_SesNwireRowStatus_Object = MibTableColumn
sesNwireRowStatus = _SesNwireRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 5, 1, 6, 1, 4),
    _SesNwireRowStatus_Type()
)
sesNwireRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sesNwireRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SESCOMMON-MIB",
    **{"sesLineStatusTable": sesLineStatusTable,
       "sesLineStatusEntry": sesLineStatusEntry,
       "sesLineUptime": sesLineUptime,
       "sesLineLinkDown": sesLineLinkDown,
       "sesLineNMdefect": sesLineNMdefect,
       "sesLineHECdefect": sesLineHECdefect,
       "sesLineTxPackets": sesLineTxPackets,
       "sesLineRxPackets": sesLineRxPackets,
       "sesLineTxFrames": sesLineTxFrames,
       "sesLineRxFrames": sesLineRxFrames,
       "sesLineTxCells": sesLineTxCells,
       "sesLineRxCells": sesLineRxCells,
       "sesMaxNumOfProfiles": sesMaxNumOfProfiles,
       "sesLineConfTable": sesLineConfTable,
       "sesLineConfEntry": sesLineConfEntry,
       "sesLineConfEncap": sesLineConfEncap,
       "sesLineConfVpi": sesLineConfVpi,
       "sesLineConfVci": sesLineConfVci,
       "sesMaxNumOfPortBondings": sesMaxNumOfPortBondings,
       "sesPortBondingTable": sesPortBondingTable,
       "sesPortBondingEntry": sesPortBondingEntry,
       "sesPortBondingName": sesPortBondingName,
       "sesPortBondingNumOfMembers": sesPortBondingNumOfMembers,
       "sesPortBondingMemberList": sesPortBondingMemberList,
       "sesPortBondingMode": sesPortBondingMode,
       "sesPortBondingRowStatus": sesPortBondingRowStatus,
       "sesNwireTable": sesNwireTable,
       "sesNwireEntry": sesNwireEntry,
       "sesNwireGroupName": sesNwireGroupName,
       "sesNwireGroupNumber": sesNwireGroupNumber,
       "sesNwireMode": sesNwireMode,
       "sesNwireRowStatus": sesNwireRowStatus}
)
