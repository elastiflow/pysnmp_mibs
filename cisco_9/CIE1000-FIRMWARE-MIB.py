# SNMP MIB module (CIE1000-FIRMWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CIE1000-FIRMWARE-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 20:26:41 2025
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

(CIE1000DisplayString,) = mibBuilder.importSymbols(
    "CIE1000-TC",
    "CIE1000DisplayString")

(cie1000SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCO-IE1000-MIB",
    "cie1000SwitchMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cie1000FirmwareMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28)
)
if mibBuilder.loadTexts:
    cie1000FirmwareMib.setRevisions(
        ("2014-12-16 00:00",
         "2014-10-10 00:00",
         "2014-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CIE1000FirmwareStatusImageEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 0),
          ("stage2Bootloader", 1),
          ("activeFirmware", 2),
          ("alternativeFirmware", 3))
    )



class CIE1000FirmwareUploadImageEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bootloader", 0),
          ("firmware", 1))
    )



class CIE1000FirmwareUploadStatusEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("inProgress", 2),
          ("errIvalidIp", 3),
          ("errTftpFailed", 4),
          ("errBusy", 5),
          ("errMemoryInsufficient", 6),
          ("errInvalidImage", 7),
          ("errWriteFlash", 8),
          ("errSameImageExisted", 9),
          ("errUnknownImage", 10),
          ("errFlashImageNotFound", 11),
          ("errFlashEntryNotFound", 12),
          ("errCrc", 13),
          ("errImageSize", 14),
          ("errEraseFlash", 15),
          ("errIncorrectImageVersion", 16),
          ("errDownloadUrl", 17),
          ("errInvalidUrl", 18),
          ("errInvalidPath", 19),
          ("errInvalidFilename", 20))
    )



# MIB Managed Objects in the order of their OIDs

_Cie1000FirmwareMibObjects_ObjectIdentity = ObjectIdentity
cie1000FirmwareMibObjects = _Cie1000FirmwareMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1)
)
_Cie1000FirmwareStatus_ObjectIdentity = ObjectIdentity
cie1000FirmwareStatus = _Cie1000FirmwareStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3)
)
_Cie1000FirmwareStatusImageTable_Object = MibTable
cie1000FirmwareStatusImageTable = _Cie1000FirmwareStatusImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageTable.setStatus("current")
_Cie1000FirmwareStatusImageEntry_Object = MibTableRow
cie1000FirmwareStatusImageEntry = _Cie1000FirmwareStatusImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1)
)
cie1000FirmwareStatusImageEntry.setIndexNames(
    (0, "CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageNumber"),
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageEntry.setStatus("current")


class _Cie1000FirmwareStatusImageNumber_Type(Integer32):
    """Custom type cie1000FirmwareStatusImageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Cie1000FirmwareStatusImageNumber_Type.__name__ = "Integer32"
_Cie1000FirmwareStatusImageNumber_Object = MibTableColumn
cie1000FirmwareStatusImageNumber = _Cie1000FirmwareStatusImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 1),
    _Cie1000FirmwareStatusImageNumber_Type()
)
cie1000FirmwareStatusImageNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageNumber.setStatus("current")
_Cie1000FirmwareStatusImageType_Type = CIE1000FirmwareStatusImageEnum
_Cie1000FirmwareStatusImageType_Object = MibTableColumn
cie1000FirmwareStatusImageType = _Cie1000FirmwareStatusImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 2),
    _Cie1000FirmwareStatusImageType_Type()
)
cie1000FirmwareStatusImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageType.setStatus("current")


class _Cie1000FirmwareStatusImageName_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusImageName based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000FirmwareStatusImageName_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusImageName_Object = MibTableColumn
cie1000FirmwareStatusImageName = _Cie1000FirmwareStatusImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 3),
    _Cie1000FirmwareStatusImageName_Type()
)
cie1000FirmwareStatusImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageName.setStatus("current")


class _Cie1000FirmwareStatusImageVersion_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusImageVersion based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000FirmwareStatusImageVersion_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusImageVersion_Object = MibTableColumn
cie1000FirmwareStatusImageVersion = _Cie1000FirmwareStatusImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 4),
    _Cie1000FirmwareStatusImageVersion_Type()
)
cie1000FirmwareStatusImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageVersion.setStatus("current")


class _Cie1000FirmwareStatusImageBuiltDate_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusImageBuiltDate based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000FirmwareStatusImageBuiltDate_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusImageBuiltDate_Object = MibTableColumn
cie1000FirmwareStatusImageBuiltDate = _Cie1000FirmwareStatusImageBuiltDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 5),
    _Cie1000FirmwareStatusImageBuiltDate_Type()
)
cie1000FirmwareStatusImageBuiltDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageBuiltDate.setStatus("current")


class _Cie1000FirmwareStatusImageCodeRevision_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusImageCodeRevision based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Cie1000FirmwareStatusImageCodeRevision_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusImageCodeRevision_Object = MibTableColumn
cie1000FirmwareStatusImageCodeRevision = _Cie1000FirmwareStatusImageCodeRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 1, 1, 6),
    _Cie1000FirmwareStatusImageCodeRevision_Type()
)
cie1000FirmwareStatusImageCodeRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageCodeRevision.setStatus("current")
_Cie1000FirmwareStatusImageUpload_ObjectIdentity = ObjectIdentity
cie1000FirmwareStatusImageUpload = _Cie1000FirmwareStatusImageUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 2)
)
_Cie1000FirmwareStatusImageUploadStatus_Type = CIE1000FirmwareUploadStatusEnum
_Cie1000FirmwareStatusImageUploadStatus_Object = MibScalar
cie1000FirmwareStatusImageUploadStatus = _Cie1000FirmwareStatusImageUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 2, 1),
    _Cie1000FirmwareStatusImageUploadStatus_Type()
)
cie1000FirmwareStatusImageUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageUploadStatus.setStatus("current")
_Cie1000FirmwareStatusSwitchTable_Object = MibTable
cie1000FirmwareStatusSwitchTable = _Cie1000FirmwareStatusSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchTable.setStatus("current")
_Cie1000FirmwareStatusSwitchEntry_Object = MibTableRow
cie1000FirmwareStatusSwitchEntry = _Cie1000FirmwareStatusSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1)
)
cie1000FirmwareStatusSwitchEntry.setIndexNames(
    (0, "CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchSwitchId"),
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchEntry.setStatus("current")


class _Cie1000FirmwareStatusSwitchSwitchId_Type(Integer32):
    """Custom type cie1000FirmwareStatusSwitchSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cie1000FirmwareStatusSwitchSwitchId_Type.__name__ = "Integer32"
_Cie1000FirmwareStatusSwitchSwitchId_Object = MibTableColumn
cie1000FirmwareStatusSwitchSwitchId = _Cie1000FirmwareStatusSwitchSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 1),
    _Cie1000FirmwareStatusSwitchSwitchId_Type()
)
cie1000FirmwareStatusSwitchSwitchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchSwitchId.setStatus("current")


class _Cie1000FirmwareStatusSwitchChipId_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusSwitchChipId based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Cie1000FirmwareStatusSwitchChipId_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusSwitchChipId_Object = MibTableColumn
cie1000FirmwareStatusSwitchChipId = _Cie1000FirmwareStatusSwitchChipId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 2),
    _Cie1000FirmwareStatusSwitchChipId_Type()
)
cie1000FirmwareStatusSwitchChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchChipId.setStatus("current")


class _Cie1000FirmwareStatusSwitchBoardType_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusSwitchBoardType based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000FirmwareStatusSwitchBoardType_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusSwitchBoardType_Object = MibTableColumn
cie1000FirmwareStatusSwitchBoardType = _Cie1000FirmwareStatusSwitchBoardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 3),
    _Cie1000FirmwareStatusSwitchBoardType_Type()
)
cie1000FirmwareStatusSwitchBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchBoardType.setStatus("current")
_Cie1000FirmwareStatusSwitchPortCnt_Type = Unsigned32
_Cie1000FirmwareStatusSwitchPortCnt_Object = MibTableColumn
cie1000FirmwareStatusSwitchPortCnt = _Cie1000FirmwareStatusSwitchPortCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 4),
    _Cie1000FirmwareStatusSwitchPortCnt_Type()
)
cie1000FirmwareStatusSwitchPortCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchPortCnt.setStatus("current")


class _Cie1000FirmwareStatusSwitchProduct_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusSwitchProduct based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Cie1000FirmwareStatusSwitchProduct_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusSwitchProduct_Object = MibTableColumn
cie1000FirmwareStatusSwitchProduct = _Cie1000FirmwareStatusSwitchProduct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 5),
    _Cie1000FirmwareStatusSwitchProduct_Type()
)
cie1000FirmwareStatusSwitchProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchProduct.setStatus("current")


class _Cie1000FirmwareStatusSwitchVersion_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusSwitchVersion based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000FirmwareStatusSwitchVersion_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusSwitchVersion_Object = MibTableColumn
cie1000FirmwareStatusSwitchVersion = _Cie1000FirmwareStatusSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 6),
    _Cie1000FirmwareStatusSwitchVersion_Type()
)
cie1000FirmwareStatusSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchVersion.setStatus("current")


class _Cie1000FirmwareStatusSwitchBuiltDate_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareStatusSwitchBuiltDate based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000FirmwareStatusSwitchBuiltDate_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareStatusSwitchBuiltDate_Object = MibTableColumn
cie1000FirmwareStatusSwitchBuiltDate = _Cie1000FirmwareStatusSwitchBuiltDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 3, 3, 1, 7),
    _Cie1000FirmwareStatusSwitchBuiltDate_Type()
)
cie1000FirmwareStatusSwitchBuiltDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchBuiltDate.setStatus("current")
_Cie1000FirmwareControl_ObjectIdentity = ObjectIdentity
cie1000FirmwareControl = _Cie1000FirmwareControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4)
)
_Cie1000FirmwareControlGlobals_ObjectIdentity = ObjectIdentity
cie1000FirmwareControlGlobals = _Cie1000FirmwareControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 1)
)
_Cie1000FirmwareControlGlobalsSwapFirmware_Type = TruthValue
_Cie1000FirmwareControlGlobalsSwapFirmware_Object = MibScalar
cie1000FirmwareControlGlobalsSwapFirmware = _Cie1000FirmwareControlGlobalsSwapFirmware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 1, 1),
    _Cie1000FirmwareControlGlobalsSwapFirmware_Type()
)
cie1000FirmwareControlGlobalsSwapFirmware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000FirmwareControlGlobalsSwapFirmware.setStatus("current")
_Cie1000FirmwareControlImageUpload_ObjectIdentity = ObjectIdentity
cie1000FirmwareControlImageUpload = _Cie1000FirmwareControlImageUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2)
)
_Cie1000FirmwareControlImageUploadDoUpload_Type = TruthValue
_Cie1000FirmwareControlImageUploadDoUpload_Object = MibScalar
cie1000FirmwareControlImageUploadDoUpload = _Cie1000FirmwareControlImageUploadDoUpload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 1),
    _Cie1000FirmwareControlImageUploadDoUpload_Type()
)
cie1000FirmwareControlImageUploadDoUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000FirmwareControlImageUploadDoUpload.setStatus("current")
_Cie1000FirmwareControlImageUploadImageType_Type = CIE1000FirmwareUploadImageEnum
_Cie1000FirmwareControlImageUploadImageType_Object = MibScalar
cie1000FirmwareControlImageUploadImageType = _Cie1000FirmwareControlImageUploadImageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 2),
    _Cie1000FirmwareControlImageUploadImageType_Type()
)
cie1000FirmwareControlImageUploadImageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000FirmwareControlImageUploadImageType.setStatus("current")


class _Cie1000FirmwareControlImageUploadUrl_Type(CIE1000DisplayString):
    """Custom type cie1000FirmwareControlImageUploadUrl based on CIE1000DisplayString"""
    subtypeSpec = CIE1000DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Cie1000FirmwareControlImageUploadUrl_Type.__name__ = "CIE1000DisplayString"
_Cie1000FirmwareControlImageUploadUrl_Object = MibScalar
cie1000FirmwareControlImageUploadUrl = _Cie1000FirmwareControlImageUploadUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 1, 4, 2, 3),
    _Cie1000FirmwareControlImageUploadUrl_Type()
)
cie1000FirmwareControlImageUploadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cie1000FirmwareControlImageUploadUrl.setStatus("current")
_Cie1000FirmwareMibConformance_ObjectIdentity = ObjectIdentity
cie1000FirmwareMibConformance = _Cie1000FirmwareMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2)
)
_Cie1000FirmwareMibCompliances_ObjectIdentity = ObjectIdentity
cie1000FirmwareMibCompliances = _Cie1000FirmwareMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 1)
)
_Cie1000FirmwareMibGroups_ObjectIdentity = ObjectIdentity
cie1000FirmwareMibGroups = _Cie1000FirmwareMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2)
)

# Managed Objects groups

cie1000FirmwareStatusImageTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 1)
)
cie1000FirmwareStatusImageTableInfoGroup.setObjects(
      *(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageNumber"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageType"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageName"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageVersion"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageBuiltDate"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageCodeRevision"))
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageTableInfoGroup.setStatus("current")

cie1000FirmwareStatusImageUploadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 2)
)
cie1000FirmwareStatusImageUploadInfoGroup.setObjects(
    ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageUploadStatus")
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusImageUploadInfoGroup.setStatus("current")

cie1000FirmwareStatusSwitchTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 3)
)
cie1000FirmwareStatusSwitchTableInfoGroup.setObjects(
      *(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchSwitchId"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchChipId"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchBoardType"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchPortCnt"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchProduct"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchVersion"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchBuiltDate"))
)
if mibBuilder.loadTexts:
    cie1000FirmwareStatusSwitchTableInfoGroup.setStatus("current")

cie1000FirmwareControlGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 4)
)
cie1000FirmwareControlGlobalsInfoGroup.setObjects(
    ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlGlobalsSwapFirmware")
)
if mibBuilder.loadTexts:
    cie1000FirmwareControlGlobalsInfoGroup.setStatus("current")

cie1000FirmwareControlImageUploadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 2, 5)
)
cie1000FirmwareControlImageUploadInfoGroup.setObjects(
      *(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadDoUpload"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadImageType"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadUrl"))
)
if mibBuilder.loadTexts:
    cie1000FirmwareControlImageUploadInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cie1000FirmwareMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 832, 1, 28, 2, 1, 1)
)
cie1000FirmwareMibCompliance.setObjects(
      *(("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageTableInfoGroup"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusImageUploadInfoGroup"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareStatusSwitchTableInfoGroup"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlGlobalsInfoGroup"),
        ("CIE1000-FIRMWARE-MIB", "cie1000FirmwareControlImageUploadInfoGroup"))
)
if mibBuilder.loadTexts:
    cie1000FirmwareMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIE1000-FIRMWARE-MIB",
    **{"CIE1000FirmwareStatusImageEnum": CIE1000FirmwareStatusImageEnum,
       "CIE1000FirmwareUploadImageEnum": CIE1000FirmwareUploadImageEnum,
       "CIE1000FirmwareUploadStatusEnum": CIE1000FirmwareUploadStatusEnum,
       "cie1000FirmwareMib": cie1000FirmwareMib,
       "cie1000FirmwareMibObjects": cie1000FirmwareMibObjects,
       "cie1000FirmwareStatus": cie1000FirmwareStatus,
       "cie1000FirmwareStatusImageTable": cie1000FirmwareStatusImageTable,
       "cie1000FirmwareStatusImageEntry": cie1000FirmwareStatusImageEntry,
       "cie1000FirmwareStatusImageNumber": cie1000FirmwareStatusImageNumber,
       "cie1000FirmwareStatusImageType": cie1000FirmwareStatusImageType,
       "cie1000FirmwareStatusImageName": cie1000FirmwareStatusImageName,
       "cie1000FirmwareStatusImageVersion": cie1000FirmwareStatusImageVersion,
       "cie1000FirmwareStatusImageBuiltDate": cie1000FirmwareStatusImageBuiltDate,
       "cie1000FirmwareStatusImageCodeRevision": cie1000FirmwareStatusImageCodeRevision,
       "cie1000FirmwareStatusImageUpload": cie1000FirmwareStatusImageUpload,
       "cie1000FirmwareStatusImageUploadStatus": cie1000FirmwareStatusImageUploadStatus,
       "cie1000FirmwareStatusSwitchTable": cie1000FirmwareStatusSwitchTable,
       "cie1000FirmwareStatusSwitchEntry": cie1000FirmwareStatusSwitchEntry,
       "cie1000FirmwareStatusSwitchSwitchId": cie1000FirmwareStatusSwitchSwitchId,
       "cie1000FirmwareStatusSwitchChipId": cie1000FirmwareStatusSwitchChipId,
       "cie1000FirmwareStatusSwitchBoardType": cie1000FirmwareStatusSwitchBoardType,
       "cie1000FirmwareStatusSwitchPortCnt": cie1000FirmwareStatusSwitchPortCnt,
       "cie1000FirmwareStatusSwitchProduct": cie1000FirmwareStatusSwitchProduct,
       "cie1000FirmwareStatusSwitchVersion": cie1000FirmwareStatusSwitchVersion,
       "cie1000FirmwareStatusSwitchBuiltDate": cie1000FirmwareStatusSwitchBuiltDate,
       "cie1000FirmwareControl": cie1000FirmwareControl,
       "cie1000FirmwareControlGlobals": cie1000FirmwareControlGlobals,
       "cie1000FirmwareControlGlobalsSwapFirmware": cie1000FirmwareControlGlobalsSwapFirmware,
       "cie1000FirmwareControlImageUpload": cie1000FirmwareControlImageUpload,
       "cie1000FirmwareControlImageUploadDoUpload": cie1000FirmwareControlImageUploadDoUpload,
       "cie1000FirmwareControlImageUploadImageType": cie1000FirmwareControlImageUploadImageType,
       "cie1000FirmwareControlImageUploadUrl": cie1000FirmwareControlImageUploadUrl,
       "cie1000FirmwareMibConformance": cie1000FirmwareMibConformance,
       "cie1000FirmwareMibCompliances": cie1000FirmwareMibCompliances,
       "cie1000FirmwareMibCompliance": cie1000FirmwareMibCompliance,
       "cie1000FirmwareMibGroups": cie1000FirmwareMibGroups,
       "cie1000FirmwareStatusImageTableInfoGroup": cie1000FirmwareStatusImageTableInfoGroup,
       "cie1000FirmwareStatusImageUploadInfoGroup": cie1000FirmwareStatusImageUploadInfoGroup,
       "cie1000FirmwareStatusSwitchTableInfoGroup": cie1000FirmwareStatusSwitchTableInfoGroup,
       "cie1000FirmwareControlGlobalsInfoGroup": cie1000FirmwareControlGlobalsInfoGroup,
       "cie1000FirmwareControlImageUploadInfoGroup": cie1000FirmwareControlImageUploadInfoGroup}
)
