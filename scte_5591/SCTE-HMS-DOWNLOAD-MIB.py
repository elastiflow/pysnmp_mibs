# SNMP MIB module (SCTE-HMS-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-DOWNLOAD-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:31:05 2025
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

(commonLogicalID,
 commonPhysAddress) = mibBuilder.importSymbols(
    "SCTE-HMS-COMMON-MIB",
    "commonLogicalID",
    "commonPhysAddress")

(downloadIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "downloadIdent")

(scteHmsTree,) = mibBuilder.importSymbols(
    "SCTE-ROOT",
    "scteHmsTree")

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
 NotificationType,
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
    "NotificationType",
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

_DownLoad_ObjectIdentity = ObjectIdentity
downLoad = _DownLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1)
)
_DlDownloadDevice_Type = Integer32
_DlDownloadDevice_Object = MibScalar
dlDownloadDevice = _DlDownloadDevice_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 2),
    _DlDownloadDevice_Type()
)
dlDownloadDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadDevice.setStatus("mandatory")
_DlDownloadImage_Type = Integer32
_DlDownloadImage_Object = MibScalar
dlDownloadImage = _DlDownloadImage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 3),
    _DlDownloadImage_Type()
)
dlDownloadImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadImage.setStatus("mandatory")
_DlDownloadKey_Type = DisplayString
_DlDownloadKey_Object = MibScalar
dlDownloadKey = _DlDownloadKey_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 4),
    _DlDownloadKey_Type()
)
dlDownloadKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadKey.setStatus("mandatory")


class _DlDownloadControl_Type(Integer32):
    """Custom type dlDownloadControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("download", 2),
          ("finish", 3))
    )


_DlDownloadControl_Type.__name__ = "Integer32"
_DlDownloadControl_Object = MibScalar
dlDownloadControl = _DlDownloadControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 5),
    _DlDownloadControl_Type()
)
dlDownloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadControl.setStatus("mandatory")


class _DlDownloadStatus_Type(Integer32):
    """Custom type dlDownloadStatus based on Integer32"""
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
        *(("initiateInProgress", 1),
          ("initiateComplete", 2),
          ("waitingForLine", 3),
          ("processingLine", 4),
          ("finishInProgress", 5),
          ("done", 6))
    )


_DlDownloadStatus_Type.__name__ = "Integer32"
_DlDownloadStatus_Object = MibScalar
dlDownloadStatus = _DlDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 6),
    _DlDownloadStatus_Type()
)
dlDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlDownloadStatus.setStatus("mandatory")


class _DlDownloadErrorStatus_Type(DisplayString):
    """Custom type dlDownloadErrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DlDownloadErrorStatus_Type.__name__ = "DisplayString"
_DlDownloadErrorStatus_Object = MibScalar
dlDownloadErrorStatus = _DlDownloadErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 7),
    _DlDownloadErrorStatus_Type()
)
dlDownloadErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlDownloadErrorStatus.setStatus("mandatory")
_DlDownloadLine_Type = OctetString
_DlDownloadLine_Object = MibScalar
dlDownloadLine = _DlDownloadLine_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 1, 8),
    _DlDownloadLine_Type()
)
dlDownloadLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadLine.setStatus("mandatory")
_TransponderImage_ObjectIdentity = ObjectIdentity
transponderImage = _TransponderImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2)
)
_TransponderTable_Object = MibTable
transponderTable = _TransponderTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    transponderTable.setStatus("mandatory")
_TransponderEntry_Object = MibTableRow
transponderEntry = _TransponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1)
)
transponderEntry.setIndexNames(
    (0, "SCTE-HMS-DOWNLOAD-MIB", "dlTransponderDevice"),
)
if mibBuilder.loadTexts:
    transponderEntry.setStatus("mandatory")
_DlTransponderDevice_Type = Integer32
_DlTransponderDevice_Object = MibTableColumn
dlTransponderDevice = _DlTransponderDevice_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 1),
    _DlTransponderDevice_Type()
)
dlTransponderDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlTransponderDevice.setStatus("mandatory")
_DlNumberImages_Type = Integer32
_DlNumberImages_Object = MibTableColumn
dlNumberImages = _DlNumberImages_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 2),
    _DlNumberImages_Type()
)
dlNumberImages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlNumberImages.setStatus("mandatory")
_DlActiveImage_Type = Integer32
_DlActiveImage_Object = MibTableColumn
dlActiveImage = _DlActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 3),
    _DlActiveImage_Type()
)
dlActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlActiveImage.setStatus("mandatory")


class _DlActiveImageVersion_Type(DisplayString):
    """Custom type dlActiveImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlActiveImageVersion_Type.__name__ = "DisplayString"
_DlActiveImageVersion_Object = MibTableColumn
dlActiveImageVersion = _DlActiveImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 4),
    _DlActiveImageVersion_Type()
)
dlActiveImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlActiveImageVersion.setStatus("mandatory")


class _DlActiveImageDescription_Type(DisplayString):
    """Custom type dlActiveImageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DlActiveImageDescription_Type.__name__ = "DisplayString"
_DlActiveImageDescription_Object = MibTableColumn
dlActiveImageDescription = _DlActiveImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 5),
    _DlActiveImageDescription_Type()
)
dlActiveImageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlActiveImageDescription.setStatus("mandatory")


class _DlActiveImageAccess_Type(Integer32):
    """Custom type dlActiveImageAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overwriteAllowed", 1),
          ("overwriteNotAllowed", 2))
    )


_DlActiveImageAccess_Type.__name__ = "Integer32"
_DlActiveImageAccess_Object = MibTableColumn
dlActiveImageAccess = _DlActiveImageAccess_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 6),
    _DlActiveImageAccess_Type()
)
dlActiveImageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlActiveImageAccess.setStatus("mandatory")
_DlStartupImage_Type = Integer32
_DlStartupImage_Object = MibTableColumn
dlStartupImage = _DlStartupImage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 7),
    _DlStartupImage_Type()
)
dlStartupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlStartupImage.setStatus("mandatory")
_DlDeviceKey_Type = DisplayString
_DlDeviceKey_Object = MibTableColumn
dlDeviceKey = _DlDeviceKey_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 8),
    _DlDeviceKey_Type()
)
dlDeviceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlDeviceKey.setStatus("mandatory")


class _DlDownloadOption_Type(Integer32):
    """Custom type dlDownloadOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setStartupAndReset", 1),
          ("noAction", 2))
    )


_DlDownloadOption_Type.__name__ = "Integer32"
_DlDownloadOption_Object = MibTableColumn
dlDownloadOption = _DlDownloadOption_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 9),
    _DlDownloadOption_Type()
)
dlDownloadOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadOption.setStatus("optional")


class _DlDownloadTimeout_Type(Integer32):
    """Custom type dlDownloadTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_DlDownloadTimeout_Type.__name__ = "Integer32"
_DlDownloadTimeout_Object = MibTableColumn
dlDownloadTimeout = _DlDownloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 1, 1, 10),
    _DlDownloadTimeout_Type()
)
dlDownloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlDownloadTimeout.setStatus("mandatory")
_DlImageTable_Object = MibTable
dlImageTable = _DlImageTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    dlImageTable.setStatus("mandatory")
_DlImageEntry_Object = MibTableRow
dlImageEntry = _DlImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1)
)
dlImageEntry.setIndexNames(
    (0, "SCTE-HMS-DOWNLOAD-MIB", "dlImageDevice"),
    (0, "SCTE-HMS-DOWNLOAD-MIB", "dlImageIndex"),
)
if mibBuilder.loadTexts:
    dlImageEntry.setStatus("mandatory")
_DlImageDevice_Type = Integer32
_DlImageDevice_Object = MibTableColumn
dlImageDevice = _DlImageDevice_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 1),
    _DlImageDevice_Type()
)
dlImageDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageDevice.setStatus("mandatory")
_DlImageIndex_Type = Integer32
_DlImageIndex_Object = MibTableColumn
dlImageIndex = _DlImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 2),
    _DlImageIndex_Type()
)
dlImageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageIndex.setStatus("mandatory")


class _DlImageStatus_Type(Integer32):
    """Custom type dlImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("validApplication", 2),
          ("validData", 3))
    )


_DlImageStatus_Type.__name__ = "Integer32"
_DlImageStatus_Object = MibTableColumn
dlImageStatus = _DlImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 3),
    _DlImageStatus_Type()
)
dlImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageStatus.setStatus("mandatory")


class _DlImageAccess_Type(Integer32):
    """Custom type dlImageAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imageAccessReadWrite", 1),
          ("imageAccessReadOnly", 2))
    )


_DlImageAccess_Type.__name__ = "Integer32"
_DlImageAccess_Object = MibTableColumn
dlImageAccess = _DlImageAccess_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 4),
    _DlImageAccess_Type()
)
dlImageAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageAccess.setStatus("mandatory")


class _DlImageVersion_Type(DisplayString):
    """Custom type dlImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlImageVersion_Type.__name__ = "DisplayString"
_DlImageVersion_Object = MibTableColumn
dlImageVersion = _DlImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 5),
    _DlImageVersion_Type()
)
dlImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageVersion.setStatus("mandatory")


class _DlImageDescription_Type(DisplayString):
    """Custom type dlImageDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DlImageDescription_Type.__name__ = "DisplayString"
_DlImageDescription_Object = MibTableColumn
dlImageDescription = _DlImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 8, 2, 2, 1, 6),
    _DlImageDescription_Type()
)
dlImageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlImageDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hmsDownloadStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 5591, 1, 0, 3)
)
hmsDownloadStatus.setObjects(
      *(("SCTE-HMS-COMMON-MIB", "commonPhysAddress"),
        ("SCTE-HMS-COMMON-MIB", "commonLogicalID"),
        ("SCTE-HMS-DOWNLOAD-MIB", "dlDownloadErrorStatus"),
        ("SCTE-HMS-DOWNLOAD-MIB", "dlDownloadImage"),
        ("SCTE-HMS-DOWNLOAD-MIB", "dlDownloadDevice"))
)
if mibBuilder.loadTexts:
    hmsDownloadStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-DOWNLOAD-MIB",
    **{"hmsDownloadStatus": hmsDownloadStatus,
       "downLoad": downLoad,
       "dlDownloadDevice": dlDownloadDevice,
       "dlDownloadImage": dlDownloadImage,
       "dlDownloadKey": dlDownloadKey,
       "dlDownloadControl": dlDownloadControl,
       "dlDownloadStatus": dlDownloadStatus,
       "dlDownloadErrorStatus": dlDownloadErrorStatus,
       "dlDownloadLine": dlDownloadLine,
       "transponderImage": transponderImage,
       "transponderTable": transponderTable,
       "transponderEntry": transponderEntry,
       "dlTransponderDevice": dlTransponderDevice,
       "dlNumberImages": dlNumberImages,
       "dlActiveImage": dlActiveImage,
       "dlActiveImageVersion": dlActiveImageVersion,
       "dlActiveImageDescription": dlActiveImageDescription,
       "dlActiveImageAccess": dlActiveImageAccess,
       "dlStartupImage": dlStartupImage,
       "dlDeviceKey": dlDeviceKey,
       "dlDownloadOption": dlDownloadOption,
       "dlDownloadTimeout": dlDownloadTimeout,
       "dlImageTable": dlImageTable,
       "dlImageEntry": dlImageEntry,
       "dlImageDevice": dlImageDevice,
       "dlImageIndex": dlImageIndex,
       "dlImageStatus": dlImageStatus,
       "dlImageAccess": dlImageAccess,
       "dlImageVersion": dlImageVersion,
       "dlImageDescription": dlImageDescription}
)
