# SNMP MIB module (WHSD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/telegra_50055/WHSD.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:46:19 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Telegra_ObjectIdentity = ObjectIdentity
telegra = _Telegra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50055)
)
_Whsd_ObjectIdentity = ObjectIdentity
whsd = _Whsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50055, 16217)
)
_WhsdRoadOutstation_ObjectIdentity = ObjectIdentity
whsdRoadOutstation = _WhsdRoadOutstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1)
)
_WhsdRoadOutstationTable_Object = MibTable
whsdRoadOutstationTable = _WhsdRoadOutstationTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1)
)
if mibBuilder.loadTexts:
    whsdRoadOutstationTable.setStatus("mandatory")
_WhsdRoadOutstationEntry_Object = MibTableRow
whsdRoadOutstationEntry = _WhsdRoadOutstationEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1)
)
whsdRoadOutstationEntry.setIndexNames(
    (0, "WHSD", "whsdRoadOutstationIndex"),
)
if mibBuilder.loadTexts:
    whsdRoadOutstationEntry.setStatus("mandatory")
_WhsdRoadOutstationIndex_Type = Integer32
_WhsdRoadOutstationIndex_Object = MibTableColumn
whsdRoadOutstationIndex = _WhsdRoadOutstationIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1, 1),
    _WhsdRoadOutstationIndex_Type()
)
whsdRoadOutstationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationIndex.setStatus("mandatory")
_WhsdRoadOutstationStatusTableIndex_Type = Integer32
_WhsdRoadOutstationStatusTableIndex_Object = MibTableColumn
whsdRoadOutstationStatusTableIndex = _WhsdRoadOutstationStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1, 2),
    _WhsdRoadOutstationStatusTableIndex_Type()
)
whsdRoadOutstationStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationStatusTableIndex.setStatus("mandatory")
_WhsdRoadOutstationName_Type = OctetString
_WhsdRoadOutstationName_Object = MibTableColumn
whsdRoadOutstationName = _WhsdRoadOutstationName_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1, 3),
    _WhsdRoadOutstationName_Type()
)
whsdRoadOutstationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationName.setStatus("mandatory")
_WhsdRoadOutstationDescription_Type = OctetString
_WhsdRoadOutstationDescription_Object = MibTableColumn
whsdRoadOutstationDescription = _WhsdRoadOutstationDescription_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1, 4),
    _WhsdRoadOutstationDescription_Type()
)
whsdRoadOutstationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationDescription.setStatus("mandatory")
_WhsdRoadOutstationPosition_Type = OctetString
_WhsdRoadOutstationPosition_Object = MibTableColumn
whsdRoadOutstationPosition = _WhsdRoadOutstationPosition_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 1, 1, 5),
    _WhsdRoadOutstationPosition_Type()
)
whsdRoadOutstationPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationPosition.setStatus("mandatory")
_WhsdRoadOutstationSignalTable_Object = MibTable
whsdRoadOutstationSignalTable = _WhsdRoadOutstationSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 2)
)
if mibBuilder.loadTexts:
    whsdRoadOutstationSignalTable.setStatus("mandatory")
_WhsdRoadOutstationSignalEntry_Object = MibTableRow
whsdRoadOutstationSignalEntry = _WhsdRoadOutstationSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 2, 1)
)
whsdRoadOutstationSignalEntry.setIndexNames(
    (0, "WHSD", "whsdRoadOutstationSignalIndex"),
)
if mibBuilder.loadTexts:
    whsdRoadOutstationSignalEntry.setStatus("mandatory")
_WhsdRoadOutstationSignalIndex_Type = Integer32
_WhsdRoadOutstationSignalIndex_Object = MibTableColumn
whsdRoadOutstationSignalIndex = _WhsdRoadOutstationSignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 2, 1, 1),
    _WhsdRoadOutstationSignalIndex_Type()
)
whsdRoadOutstationSignalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationSignalIndex.setStatus("mandatory")


class _WhsdRoadOutstationCommunicationStatusValue_Type(Integer32):
    """Custom type whsdRoadOutstationCommunicationStatusValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationOk", 0),
          ("communicationBreak", 1))
    )


_WhsdRoadOutstationCommunicationStatusValue_Type.__name__ = "Integer32"
_WhsdRoadOutstationCommunicationStatusValue_Object = MibTableColumn
whsdRoadOutstationCommunicationStatusValue = _WhsdRoadOutstationCommunicationStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 1, 2, 1, 2),
    _WhsdRoadOutstationCommunicationStatusValue_Type()
)
whsdRoadOutstationCommunicationStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdRoadOutstationCommunicationStatusValue.setStatus("mandatory")
_WhsdVms_ObjectIdentity = ObjectIdentity
whsdVms = _WhsdVms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2)
)
_WhsdVmsTable_Object = MibTable
whsdVmsTable = _WhsdVmsTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1)
)
if mibBuilder.loadTexts:
    whsdVmsTable.setStatus("mandatory")
_WhsdVmsEntry_Object = MibTableRow
whsdVmsEntry = _WhsdVmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1)
)
whsdVmsEntry.setIndexNames(
    (0, "WHSD", "whsdVmsIndex"),
)
if mibBuilder.loadTexts:
    whsdVmsEntry.setStatus("mandatory")
_WhsdVmsIndex_Type = Integer32
_WhsdVmsIndex_Object = MibTableColumn
whsdVmsIndex = _WhsdVmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1, 1),
    _WhsdVmsIndex_Type()
)
whsdVmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsIndex.setStatus("mandatory")
_WhsdVmsStatusTableIndex_Type = Integer32
_WhsdVmsStatusTableIndex_Object = MibTableColumn
whsdVmsStatusTableIndex = _WhsdVmsStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1, 2),
    _WhsdVmsStatusTableIndex_Type()
)
whsdVmsStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsStatusTableIndex.setStatus("mandatory")
_WhsdVmsName_Type = OctetString
_WhsdVmsName_Object = MibTableColumn
whsdVmsName = _WhsdVmsName_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1, 3),
    _WhsdVmsName_Type()
)
whsdVmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsName.setStatus("mandatory")
_WhsdVmsDescription_Type = OctetString
_WhsdVmsDescription_Object = MibTableColumn
whsdVmsDescription = _WhsdVmsDescription_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1, 4),
    _WhsdVmsDescription_Type()
)
whsdVmsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsDescription.setStatus("mandatory")
_WhsdVmsPosition_Type = OctetString
_WhsdVmsPosition_Object = MibTableColumn
whsdVmsPosition = _WhsdVmsPosition_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 1, 1, 5),
    _WhsdVmsPosition_Type()
)
whsdVmsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsPosition.setStatus("mandatory")
_WhsdVmsSignalTable_Object = MibTable
whsdVmsSignalTable = _WhsdVmsSignalTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 2)
)
if mibBuilder.loadTexts:
    whsdVmsSignalTable.setStatus("mandatory")
_WhsdVmsSignalEntry_Object = MibTableRow
whsdVmsSignalEntry = _WhsdVmsSignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 2, 1)
)
whsdVmsSignalEntry.setIndexNames(
    (0, "WHSD", "whsdVmsSignalIndex"),
)
if mibBuilder.loadTexts:
    whsdVmsSignalEntry.setStatus("mandatory")
_WhsdVmsSignalIndex_Type = Integer32
_WhsdVmsSignalIndex_Object = MibTableColumn
whsdVmsSignalIndex = _WhsdVmsSignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 2, 1, 1),
    _WhsdVmsSignalIndex_Type()
)
whsdVmsSignalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsSignalIndex.setStatus("mandatory")


class _WhsdVmsDetectedErrorValue_Type(Integer32):
    """Custom type whsdVmsDetectedErrorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("errorOnDevice", 1))
    )


_WhsdVmsDetectedErrorValue_Type.__name__ = "Integer32"
_WhsdVmsDetectedErrorValue_Object = MibTableColumn
whsdVmsDetectedErrorValue = _WhsdVmsDetectedErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 2, 1, 2),
    _WhsdVmsDetectedErrorValue_Type()
)
whsdVmsDetectedErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsDetectedErrorValue.setStatus("mandatory")


class _WhsdVmsCommunicationErrorValue_Type(Integer32):
    """Custom type whsdVmsCommunicationErrorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationOk", 0),
          ("communicationBreak", 1))
    )


_WhsdVmsCommunicationErrorValue_Type.__name__ = "Integer32"
_WhsdVmsCommunicationErrorValue_Object = MibTableColumn
whsdVmsCommunicationErrorValue = _WhsdVmsCommunicationErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 2, 2, 1, 2),
    _WhsdVmsCommunicationErrorValue_Type()
)
whsdVmsCommunicationErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdVmsCommunicationErrorValue.setStatus("mandatory")
_WhsdDisplay_ObjectIdentity = ObjectIdentity
whsdDisplay = _WhsdDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3)
)
_WhsdDisplayTable_Object = MibTable
whsdDisplayTable = _WhsdDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1)
)
if mibBuilder.loadTexts:
    whsdDisplayTable.setStatus("mandatory")
_WhsdDisplayEntry_Object = MibTableRow
whsdDisplayEntry = _WhsdDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1)
)
whsdDisplayEntry.setIndexNames(
    (0, "WHSD", "whsdDisplayIndex"),
)
if mibBuilder.loadTexts:
    whsdDisplayEntry.setStatus("mandatory")
_WhsdDisplayIndex_Type = Integer32
_WhsdDisplayIndex_Object = MibTableColumn
whsdDisplayIndex = _WhsdDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1, 1),
    _WhsdDisplayIndex_Type()
)
whsdDisplayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayIndex.setStatus("mandatory")
_WhsdDisplayStatusTableIndex_Type = Integer32
_WhsdDisplayStatusTableIndex_Object = MibTableColumn
whsdDisplayStatusTableIndex = _WhsdDisplayStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1, 2),
    _WhsdDisplayStatusTableIndex_Type()
)
whsdDisplayStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayStatusTableIndex.setStatus("mandatory")
_WhsdDisplayName_Type = OctetString
_WhsdDisplayName_Object = MibTableColumn
whsdDisplayName = _WhsdDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1, 3),
    _WhsdDisplayName_Type()
)
whsdDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayName.setStatus("mandatory")
_WhsdDisplayDescription_Type = OctetString
_WhsdDisplayDescription_Object = MibTableColumn
whsdDisplayDescription = _WhsdDisplayDescription_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1, 4),
    _WhsdDisplayDescription_Type()
)
whsdDisplayDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayDescription.setStatus("mandatory")
_WhsdDisplayPosition_Type = OctetString
_WhsdDisplayPosition_Object = MibTableColumn
whsdDisplayPosition = _WhsdDisplayPosition_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 1, 1, 5),
    _WhsdDisplayPosition_Type()
)
whsdDisplayPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayPosition.setStatus("mandatory")
_WhsdDisplaySignalTable_Object = MibTable
whsdDisplaySignalTable = _WhsdDisplaySignalTable_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 2)
)
if mibBuilder.loadTexts:
    whsdDisplaySignalTable.setStatus("mandatory")
_WhsdDisplaySignalEntry_Object = MibTableRow
whsdDisplaySignalEntry = _WhsdDisplaySignalEntry_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 2, 1)
)
whsdDisplaySignalEntry.setIndexNames(
    (0, "WHSD", "whsdDisplaySignalIndex"),
)
if mibBuilder.loadTexts:
    whsdDisplaySignalEntry.setStatus("mandatory")
_WhsdDisplaySignalIndex_Type = Integer32
_WhsdDisplaySignalIndex_Object = MibTableColumn
whsdDisplaySignalIndex = _WhsdDisplaySignalIndex_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 2, 1, 1),
    _WhsdDisplaySignalIndex_Type()
)
whsdDisplaySignalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplaySignalIndex.setStatus("mandatory")


class _WhsdDisplayDetectedError_Type(Integer32):
    """Custom type whsdDisplayDetectedError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("errorOnDevice", 1))
    )


_WhsdDisplayDetectedError_Type.__name__ = "Integer32"
_WhsdDisplayDetectedError_Object = MibTableColumn
whsdDisplayDetectedError = _WhsdDisplayDetectedError_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 2, 1, 2),
    _WhsdDisplayDetectedError_Type()
)
whsdDisplayDetectedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayDetectedError.setStatus("mandatory")


class _WhsdDisplayCommunicationError_Type(Integer32):
    """Custom type whsdDisplayCommunicationError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("communicationOk", 0),
          ("communicationBreak", 1))
    )


_WhsdDisplayCommunicationError_Type.__name__ = "Integer32"
_WhsdDisplayCommunicationError_Object = MibTableColumn
whsdDisplayCommunicationError = _WhsdDisplayCommunicationError_Object(
    (1, 3, 6, 1, 4, 1, 50055, 16217, 3, 2, 1, 3),
    _WhsdDisplayCommunicationError_Type()
)
whsdDisplayCommunicationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whsdDisplayCommunicationError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WHSD",
    **{"telegra": telegra,
       "whsd": whsd,
       "whsdRoadOutstation": whsdRoadOutstation,
       "whsdRoadOutstationTable": whsdRoadOutstationTable,
       "whsdRoadOutstationEntry": whsdRoadOutstationEntry,
       "whsdRoadOutstationIndex": whsdRoadOutstationIndex,
       "whsdRoadOutstationStatusTableIndex": whsdRoadOutstationStatusTableIndex,
       "whsdRoadOutstationName": whsdRoadOutstationName,
       "whsdRoadOutstationDescription": whsdRoadOutstationDescription,
       "whsdRoadOutstationPosition": whsdRoadOutstationPosition,
       "whsdRoadOutstationSignalTable": whsdRoadOutstationSignalTable,
       "whsdRoadOutstationSignalEntry": whsdRoadOutstationSignalEntry,
       "whsdRoadOutstationSignalIndex": whsdRoadOutstationSignalIndex,
       "whsdRoadOutstationCommunicationStatusValue": whsdRoadOutstationCommunicationStatusValue,
       "whsdVms": whsdVms,
       "whsdVmsTable": whsdVmsTable,
       "whsdVmsEntry": whsdVmsEntry,
       "whsdVmsIndex": whsdVmsIndex,
       "whsdVmsStatusTableIndex": whsdVmsStatusTableIndex,
       "whsdVmsName": whsdVmsName,
       "whsdVmsDescription": whsdVmsDescription,
       "whsdVmsPosition": whsdVmsPosition,
       "whsdVmsSignalTable": whsdVmsSignalTable,
       "whsdVmsSignalEntry": whsdVmsSignalEntry,
       "whsdVmsSignalIndex": whsdVmsSignalIndex,
       "whsdVmsDetectedErrorValue": whsdVmsDetectedErrorValue,
       "whsdVmsCommunicationErrorValue": whsdVmsCommunicationErrorValue,
       "whsdDisplay": whsdDisplay,
       "whsdDisplayTable": whsdDisplayTable,
       "whsdDisplayEntry": whsdDisplayEntry,
       "whsdDisplayIndex": whsdDisplayIndex,
       "whsdDisplayStatusTableIndex": whsdDisplayStatusTableIndex,
       "whsdDisplayName": whsdDisplayName,
       "whsdDisplayDescription": whsdDisplayDescription,
       "whsdDisplayPosition": whsdDisplayPosition,
       "whsdDisplaySignalTable": whsdDisplaySignalTable,
       "whsdDisplaySignalEntry": whsdDisplaySignalEntry,
       "whsdDisplaySignalIndex": whsdDisplaySignalIndex,
       "whsdDisplayDetectedError": whsdDisplayDetectedError,
       "whsdDisplayCommunicationError": whsdDisplayCommunicationError}
)
