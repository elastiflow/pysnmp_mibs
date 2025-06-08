# SNMP MIB module (OLD-CISCO-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/OLD-CISCO-FLASH-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:08 2025
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lflash_ObjectIdentity = ObjectIdentity
lflash = _Lflash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 10)
)
_FlashSize_Type = Integer32
_FlashSize_Object = MibScalar
flashSize = _FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 1),
    _FlashSize_Type()
)
flashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashSize.setStatus("deprecated")
_FlashFree_Type = Integer32
_FlashFree_Object = MibScalar
flashFree = _FlashFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 2),
    _FlashFree_Type()
)
flashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFree.setStatus("deprecated")
_FlashController_Type = DisplayString
_FlashController_Object = MibScalar
flashController = _FlashController_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 3),
    _FlashController_Type()
)
flashController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashController.setStatus("deprecated")
_FlashCard_Type = DisplayString
_FlashCard_Object = MibScalar
flashCard = _FlashCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 4),
    _FlashCard_Type()
)
flashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCard.setStatus("deprecated")


class _FlashVPP_Type(Integer32):
    """Custom type flashVPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("missing", 2))
    )


_FlashVPP_Type.__name__ = "Integer32"
_FlashVPP_Object = MibScalar
flashVPP = _FlashVPP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 5),
    _FlashVPP_Type()
)
flashVPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVPP.setStatus("deprecated")
_FlashErase_Type = Integer32
_FlashErase_Object = MibScalar
flashErase = _FlashErase_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 6),
    _FlashErase_Type()
)
flashErase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashErase.setStatus("deprecated")
_FlashEraseTime_Type = TimeTicks
_FlashEraseTime_Object = MibScalar
flashEraseTime = _FlashEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 7),
    _FlashEraseTime_Type()
)
flashEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseTime.setStatus("deprecated")


class _FlashEraseStatus_Type(Integer32):
    """Custom type flashEraseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpFailure", 3),
          ("flashReadOnly", 4),
          ("flashOpenFailure", 5),
          ("bufferAllocationFailure", 6),
          ("noOpAfterPowerOn", 7))
    )


_FlashEraseStatus_Type.__name__ = "Integer32"
_FlashEraseStatus_Object = MibScalar
flashEraseStatus = _FlashEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 8),
    _FlashEraseStatus_Type()
)
flashEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseStatus.setStatus("deprecated")
_FlashToNet_Type = DisplayString
_FlashToNet_Object = MibScalar
flashToNet = _FlashToNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 9),
    _FlashToNet_Type()
)
flashToNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashToNet.setStatus("deprecated")
_FlashToNetTime_Type = TimeTicks
_FlashToNetTime_Object = MibScalar
flashToNetTime = _FlashToNetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 10),
    _FlashToNetTime_Type()
)
flashToNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetTime.setStatus("deprecated")


class _FlashToNetStatus_Type(Integer32):
    """Custom type flashToNetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpFailure", 3),
          ("flashReadOnly", 4),
          ("flashOpenFailure", 5),
          ("bufferAllocationFailure", 6),
          ("noOpAfterPowerOn", 7))
    )


_FlashToNetStatus_Type.__name__ = "Integer32"
_FlashToNetStatus_Object = MibScalar
flashToNetStatus = _FlashToNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 11),
    _FlashToNetStatus_Type()
)
flashToNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetStatus.setStatus("deprecated")
_NetToFlash_Type = DisplayString
_NetToFlash_Object = MibScalar
netToFlash = _NetToFlash_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 12),
    _NetToFlash_Type()
)
netToFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    netToFlash.setStatus("deprecated")
_NetToFlashTime_Type = TimeTicks
_NetToFlashTime_Object = MibScalar
netToFlashTime = _NetToFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 13),
    _NetToFlashTime_Type()
)
netToFlashTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashTime.setStatus("deprecated")


class _NetToFlashStatus_Type(Integer32):
    """Custom type netToFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpFailure", 3),
          ("flashReadOnly", 4),
          ("flashOpenFailure", 5),
          ("bufferAllocationFailure", 6),
          ("noOpAfterPowerOn", 7))
    )


_NetToFlashStatus_Type.__name__ = "Integer32"
_NetToFlashStatus_Object = MibScalar
netToFlashStatus = _NetToFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 14),
    _NetToFlashStatus_Type()
)
netToFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashStatus.setStatus("deprecated")


class _FlashStatus_Type(Integer32):
    """Custom type flashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("available", 2))
    )


_FlashStatus_Type.__name__ = "Integer32"
_FlashStatus_Object = MibScalar
flashStatus = _FlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 15),
    _FlashStatus_Type()
)
flashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashStatus.setStatus("deprecated")
_FlashEntries_Type = Integer32
_FlashEntries_Object = MibScalar
flashEntries = _FlashEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 16),
    _FlashEntries_Type()
)
flashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEntries.setStatus("deprecated")
_LflashFileDirTable_Object = MibTable
lflashFileDirTable = _LflashFileDirTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17)
)
if mibBuilder.loadTexts:
    lflashFileDirTable.setStatus("deprecated")
_LflashFileDirEntry_Object = MibTableRow
lflashFileDirEntry = _LflashFileDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1)
)
lflashFileDirEntry.setIndexNames(
    (0, "OLD-CISCO-FLASH-MIB", "flashEntries"),
)
if mibBuilder.loadTexts:
    lflashFileDirEntry.setStatus("deprecated")
_FlashDirName_Type = DisplayString
_FlashDirName_Object = MibTableColumn
flashDirName = _FlashDirName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 1),
    _FlashDirName_Type()
)
flashDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirName.setStatus("deprecated")
_FlashDirSize_Type = Integer32
_FlashDirSize_Object = MibTableColumn
flashDirSize = _FlashDirSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 2),
    _FlashDirSize_Type()
)
flashDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirSize.setStatus("deprecated")


class _FlashDirStatus_Type(Integer32):
    """Custom type flashDirStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("deleted", 2))
    )


_FlashDirStatus_Type.__name__ = "Integer32"
_FlashDirStatus_Object = MibTableColumn
flashDirStatus = _FlashDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 3),
    _FlashDirStatus_Type()
)
flashDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirStatus.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-FLASH-MIB",
    **{"lflash": lflash,
       "flashSize": flashSize,
       "flashFree": flashFree,
       "flashController": flashController,
       "flashCard": flashCard,
       "flashVPP": flashVPP,
       "flashErase": flashErase,
       "flashEraseTime": flashEraseTime,
       "flashEraseStatus": flashEraseStatus,
       "flashToNet": flashToNet,
       "flashToNetTime": flashToNetTime,
       "flashToNetStatus": flashToNetStatus,
       "netToFlash": netToFlash,
       "netToFlashTime": netToFlashTime,
       "netToFlashStatus": netToFlashStatus,
       "flashStatus": flashStatus,
       "flashEntries": flashEntries,
       "lflashFileDirTable": lflashFileDirTable,
       "lflashFileDirEntry": lflashFileDirEntry,
       "flashDirName": flashDirName,
       "flashDirSize": flashDirSize,
       "flashDirStatus": flashDirStatus}
)
