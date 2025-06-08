# SNMP MIB module (SCTE-HMS-FIBERNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-FIBERNODE-MIB.mib
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

(fnIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "fnIdent")

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

_FnAdminGroup_ObjectIdentity = ObjectIdentity
fnAdminGroup = _FnAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 1)
)
_FnVendorOID_Type = ObjectIdentifier
_FnVendorOID_Object = MibScalar
fnVendorOID = _FnVendorOID_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 1, 1),
    _FnVendorOID_Type()
)
fnVendorOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnVendorOID.setStatus("optional")


class _FnDeviceId_Type(DisplayString):
    """Custom type fnDeviceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FnDeviceId_Type.__name__ = "DisplayString"
_FnDeviceId_Object = MibScalar
fnDeviceId = _FnDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 1, 2),
    _FnDeviceId_Type()
)
fnDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDeviceId.setStatus("mandatory")


class _FnNumberReturnLaser_Type(Integer32):
    """Custom type fnNumberReturnLaser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FnNumberReturnLaser_Type.__name__ = "Integer32"
_FnNumberReturnLaser_Object = MibScalar
fnNumberReturnLaser = _FnNumberReturnLaser_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 2),
    _FnNumberReturnLaser_Type()
)
fnNumberReturnLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberReturnLaser.setStatus("mandatory")
_FnReturnLaserTable_Object = MibTable
fnReturnLaserTable = _FnReturnLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3)
)
if mibBuilder.loadTexts:
    fnReturnLaserTable.setStatus("mandatory")
_FnReturnLaserEntry_Object = MibTableRow
fnReturnLaserEntry = _FnReturnLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1)
)
fnReturnLaserEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnReturnLaserIndex"),
)
if mibBuilder.loadTexts:
    fnReturnLaserEntry.setStatus("mandatory")
_FnReturnLaserIndex_Type = Integer32
_FnReturnLaserIndex_Object = MibTableColumn
fnReturnLaserIndex = _FnReturnLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 1),
    _FnReturnLaserIndex_Type()
)
fnReturnLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserIndex.setStatus("mandatory")


class _FnReturnLaserCurrent_Type(Integer32):
    """Custom type fnReturnLaserCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnReturnLaserCurrent_Type.__name__ = "Integer32"
_FnReturnLaserCurrent_Object = MibTableColumn
fnReturnLaserCurrent = _FnReturnLaserCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 2),
    _FnReturnLaserCurrent_Type()
)
fnReturnLaserCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserCurrent.setStatus("optional")


class _FnReturnLaserTemp_Type(Integer32):
    """Custom type fnReturnLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 80),
    )


_FnReturnLaserTemp_Type.__name__ = "Integer32"
_FnReturnLaserTemp_Object = MibTableColumn
fnReturnLaserTemp = _FnReturnLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 3),
    _FnReturnLaserTemp_Type()
)
fnReturnLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserTemp.setStatus("optional")


class _FnReturnLaserControl_Type(Integer32):
    """Custom type fnReturnLaserControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FnReturnLaserControl_Type.__name__ = "Integer32"
_FnReturnLaserControl_Object = MibTableColumn
fnReturnLaserControl = _FnReturnLaserControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 4),
    _FnReturnLaserControl_Type()
)
fnReturnLaserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnReturnLaserControl.setStatus("optional")


class _FnReturnLaserType_Type(DisplayString):
    """Custom type fnReturnLaserType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FnReturnLaserType_Type.__name__ = "DisplayString"
_FnReturnLaserType_Object = MibTableColumn
fnReturnLaserType = _FnReturnLaserType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 5),
    _FnReturnLaserType_Type()
)
fnReturnLaserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserType.setStatus("optional")


class _FnReturnLaserWavelength_Type(Integer32):
    """Custom type fnReturnLaserWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FnReturnLaserWavelength_Type.__name__ = "Integer32"
_FnReturnLaserWavelength_Object = MibTableColumn
fnReturnLaserWavelength = _FnReturnLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 6),
    _FnReturnLaserWavelength_Type()
)
fnReturnLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserWavelength.setStatus("optional")


class _FnReturnLaserOpticalPower_Type(Integer32):
    """Custom type fnReturnLaserOpticalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnReturnLaserOpticalPower_Type.__name__ = "Integer32"
_FnReturnLaserOpticalPower_Object = MibTableColumn
fnReturnLaserOpticalPower = _FnReturnLaserOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 7),
    _FnReturnLaserOpticalPower_Type()
)
fnReturnLaserOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnReturnLaserOpticalPower.setStatus("mandatory")
_FnReturnLaserRFActive_Type = Integer32
_FnReturnLaserRFActive_Object = MibTableColumn
fnReturnLaserRFActive = _FnReturnLaserRFActive_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 3, 1, 8),
    _FnReturnLaserRFActive_Type()
)
fnReturnLaserRFActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnReturnLaserRFActive.setStatus("mandatory")


class _FnNumberOpticalReceiver_Type(Integer32):
    """Custom type fnNumberOpticalReceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FnNumberOpticalReceiver_Type.__name__ = "Integer32"
_FnNumberOpticalReceiver_Object = MibScalar
fnNumberOpticalReceiver = _FnNumberOpticalReceiver_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 4),
    _FnNumberOpticalReceiver_Type()
)
fnNumberOpticalReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberOpticalReceiver.setStatus("mandatory")
_FnOpticalReceiverTable_Object = MibTable
fnOpticalReceiverTable = _FnOpticalReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5)
)
if mibBuilder.loadTexts:
    fnOpticalReceiverTable.setStatus("mandatory")
_FnOpticalReceiverEntry_Object = MibTableRow
fnOpticalReceiverEntry = _FnOpticalReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1)
)
fnOpticalReceiverEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnOpticalReceiverIndex"),
)
if mibBuilder.loadTexts:
    fnOpticalReceiverEntry.setStatus("mandatory")
_FnOpticalReceiverIndex_Type = Integer32
_FnOpticalReceiverIndex_Object = MibTableColumn
fnOpticalReceiverIndex = _FnOpticalReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1, 1),
    _FnOpticalReceiverIndex_Type()
)
fnOpticalReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverIndex.setStatus("mandatory")


class _FnOpticalReceiverPower_Type(Integer32):
    """Custom type fnOpticalReceiverPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnOpticalReceiverPower_Type.__name__ = "Integer32"
_FnOpticalReceiverPower_Object = MibTableColumn
fnOpticalReceiverPower = _FnOpticalReceiverPower_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1, 2),
    _FnOpticalReceiverPower_Type()
)
fnOpticalReceiverPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverPower.setStatus("mandatory")


class _FnOpticalReceiverState_Type(Integer32):
    """Custom type fnOpticalReceiverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FnOpticalReceiverState_Type.__name__ = "Integer32"
_FnOpticalReceiverState_Object = MibTableColumn
fnOpticalReceiverState = _FnOpticalReceiverState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1, 3),
    _FnOpticalReceiverState_Type()
)
fnOpticalReceiverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverState.setStatus("optional")
_FnOpticalReceiverRFActive_Type = Integer32
_FnOpticalReceiverRFActive_Object = MibTableColumn
fnOpticalReceiverRFActive = _FnOpticalReceiverRFActive_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1, 4),
    _FnOpticalReceiverRFActive_Type()
)
fnOpticalReceiverRFActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnOpticalReceiverRFActive.setStatus("mandatory")


class _FnOpticalReceiverCurrent_Type(Integer32):
    """Custom type fnOpticalReceiverCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnOpticalReceiverCurrent_Type.__name__ = "Integer32"
_FnOpticalReceiverCurrent_Object = MibTableColumn
fnOpticalReceiverCurrent = _FnOpticalReceiverCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 5, 1, 5),
    _FnOpticalReceiverCurrent_Type()
)
fnOpticalReceiverCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverCurrent.setStatus("optional")


class _FnOpticalAmpPresent_Type(Integer32):
    """Custom type fnOpticalAmpPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FnOpticalAmpPresent_Type.__name__ = "Integer32"
_FnOpticalAmpPresent_Object = MibScalar
fnOpticalAmpPresent = _FnOpticalAmpPresent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 6),
    _FnOpticalAmpPresent_Type()
)
fnOpticalAmpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalAmpPresent.setStatus("mandatory")


class _FnNumberRFActives_Type(Integer32):
    """Custom type fnNumberRFActives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FnNumberRFActives_Type.__name__ = "Integer32"
_FnNumberRFActives_Object = MibScalar
fnNumberRFActives = _FnNumberRFActives_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 7),
    _FnNumberRFActives_Type()
)
fnNumberRFActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberRFActives.setStatus("mandatory")
_FnRFActiveTable_Object = MibTable
fnRFActiveTable = _FnRFActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8)
)
if mibBuilder.loadTexts:
    fnRFActiveTable.setStatus("mandatory")
_FnRFActiveEntry_Object = MibTableRow
fnRFActiveEntry = _FnRFActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1)
)
fnRFActiveEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnRFActiveIndex"),
)
if mibBuilder.loadTexts:
    fnRFActiveEntry.setStatus("mandatory")
_FnRFActiveIndex_Type = Integer32
_FnRFActiveIndex_Object = MibTableColumn
fnRFActiveIndex = _FnRFActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1, 1),
    _FnRFActiveIndex_Type()
)
fnRFActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFActiveIndex.setStatus("mandatory")


class _FnRFActiveControlType_Type(DisplayString):
    """Custom type fnRFActiveControlType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FnRFActiveControlType_Type.__name__ = "DisplayString"
_FnRFActiveControlType_Object = MibTableColumn
fnRFActiveControlType = _FnRFActiveControlType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1, 2),
    _FnRFActiveControlType_Type()
)
fnRFActiveControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFActiveControlType.setStatus("optional")


class _FnRFActiveOutputLevel_Type(Integer32):
    """Custom type fnRFActiveOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnRFActiveOutputLevel_Type.__name__ = "Integer32"
_FnRFActiveOutputLevel_Object = MibTableColumn
fnRFActiveOutputLevel = _FnRFActiveOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1, 3),
    _FnRFActiveOutputLevel_Type()
)
fnRFActiveOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFActiveOutputLevel.setStatus("optional")


class _FnRFActiveCurrent_Type(Integer32):
    """Custom type fnRFActiveCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnRFActiveCurrent_Type.__name__ = "Integer32"
_FnRFActiveCurrent_Object = MibTableColumn
fnRFActiveCurrent = _FnRFActiveCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1, 4),
    _FnRFActiveCurrent_Type()
)
fnRFActiveCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFActiveCurrent.setStatus("optional")
_FnRFActiveControlLevel_Type = Integer32
_FnRFActiveControlLevel_Object = MibTableColumn
fnRFActiveControlLevel = _FnRFActiveControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 8, 1, 5),
    _FnRFActiveControlLevel_Type()
)
fnRFActiveControlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFActiveControlLevel.setStatus("optional")


class _FnNumberRFPort_Type(Integer32):
    """Custom type fnNumberRFPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FnNumberRFPort_Type.__name__ = "Integer32"
_FnNumberRFPort_Object = MibScalar
fnNumberRFPort = _FnNumberRFPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 9),
    _FnNumberRFPort_Type()
)
fnNumberRFPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberRFPort.setStatus("mandatory")


class _FnPortMasterAttenuationControl_Type(Integer32):
    """Custom type fnPortMasterAttenuationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("pad", 3))
    )


_FnPortMasterAttenuationControl_Type.__name__ = "Integer32"
_FnPortMasterAttenuationControl_Object = MibScalar
fnPortMasterAttenuationControl = _FnPortMasterAttenuationControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 10),
    _FnPortMasterAttenuationControl_Type()
)
fnPortMasterAttenuationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnPortMasterAttenuationControl.setStatus("optional")
_FnRFPortTable_Object = MibTable
fnRFPortTable = _FnRFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11)
)
if mibBuilder.loadTexts:
    fnRFPortTable.setStatus("mandatory")
_FnRFPortEntry_Object = MibTableRow
fnRFPortEntry = _FnRFPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1)
)
fnRFPortEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnRFPortIndex"),
)
if mibBuilder.loadTexts:
    fnRFPortEntry.setStatus("mandatory")
_FnRFPortIndex_Type = Integer32
_FnRFPortIndex_Object = MibTableColumn
fnRFPortIndex = _FnRFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 1),
    _FnRFPortIndex_Type()
)
fnRFPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortIndex.setStatus("mandatory")


class _FnRFPortControlType_Type(DisplayString):
    """Custom type fnRFPortControlType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_FnRFPortControlType_Type.__name__ = "DisplayString"
_FnRFPortControlType_Object = MibTableColumn
fnRFPortControlType = _FnRFPortControlType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 2),
    _FnRFPortControlType_Type()
)
fnRFPortControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortControlType.setStatus("optional")
_FnRFPortControlLevel_Type = Integer32
_FnRFPortControlLevel_Object = MibTableColumn
fnRFPortControlLevel = _FnRFPortControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 3),
    _FnRFPortControlLevel_Type()
)
fnRFPortControlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortControlLevel.setStatus("optional")


class _FnRFPortOutputRFLevel_Type(Integer32):
    """Custom type fnRFPortOutputRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnRFPortOutputRFLevel_Type.__name__ = "Integer32"
_FnRFPortOutputRFLevel_Object = MibTableColumn
fnRFPortOutputRFLevel = _FnRFPortOutputRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 4),
    _FnRFPortOutputRFLevel_Type()
)
fnRFPortOutputRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortOutputRFLevel.setStatus("optional")
_FnRFPortRFActive_Type = Integer32
_FnRFPortRFActive_Object = MibTableColumn
fnRFPortRFActive = _FnRFPortRFActive_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 5),
    _FnRFPortRFActive_Type()
)
fnRFPortRFActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortRFActive.setStatus("mandatory")
_FnRFPortName_Type = DisplayString
_FnRFPortName_Object = MibTableColumn
fnRFPortName = _FnRFPortName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 6),
    _FnRFPortName_Type()
)
fnRFPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnRFPortName.setStatus("mandatory")


class _FnRFPortReverseAttenuationControl_Type(Integer32):
    """Custom type fnRFPortReverseAttenuationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2),
          ("pad", 3))
    )


_FnRFPortReverseAttenuationControl_Type.__name__ = "Integer32"
_FnRFPortReverseAttenuationControl_Object = MibTableColumn
fnRFPortReverseAttenuationControl = _FnRFPortReverseAttenuationControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 11, 1, 7),
    _FnRFPortReverseAttenuationControl_Type()
)
fnRFPortReverseAttenuationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnRFPortReverseAttenuationControl.setStatus("optional")


class _FnNumberABSwitch_Type(Integer32):
    """Custom type fnNumberABSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FnNumberABSwitch_Type.__name__ = "Integer32"
_FnNumberABSwitch_Object = MibScalar
fnNumberABSwitch = _FnNumberABSwitch_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 12),
    _FnNumberABSwitch_Type()
)
fnNumberABSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberABSwitch.setStatus("mandatory")
_FnABSwitchTable_Object = MibTable
fnABSwitchTable = _FnABSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13)
)
if mibBuilder.loadTexts:
    fnABSwitchTable.setStatus("mandatory")
_FnABSwitchEntry_Object = MibTableRow
fnABSwitchEntry = _FnABSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1)
)
fnABSwitchEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnABSwitchIndex"),
)
if mibBuilder.loadTexts:
    fnABSwitchEntry.setStatus("mandatory")
_FnABSwitchIndex_Type = Integer32
_FnABSwitchIndex_Object = MibTableColumn
fnABSwitchIndex = _FnABSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 1),
    _FnABSwitchIndex_Type()
)
fnABSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnABSwitchIndex.setStatus("mandatory")
_FnOpticalReceiverABSwitchFeedA_Type = Integer32
_FnOpticalReceiverABSwitchFeedA_Object = MibTableColumn
fnOpticalReceiverABSwitchFeedA = _FnOpticalReceiverABSwitchFeedA_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 2),
    _FnOpticalReceiverABSwitchFeedA_Type()
)
fnOpticalReceiverABSwitchFeedA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchFeedA.setStatus("mandatory")
_FnOpticalReceiverABSwitchFeedB_Type = Integer32
_FnOpticalReceiverABSwitchFeedB_Object = MibTableColumn
fnOpticalReceiverABSwitchFeedB = _FnOpticalReceiverABSwitchFeedB_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 3),
    _FnOpticalReceiverABSwitchFeedB_Type()
)
fnOpticalReceiverABSwitchFeedB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchFeedB.setStatus("mandatory")


class _FnOpticalReceiverABSwitchState_Type(Integer32):
    """Custom type fnOpticalReceiverABSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pathA", 1),
          ("pathB", 2))
    )


_FnOpticalReceiverABSwitchState_Type.__name__ = "Integer32"
_FnOpticalReceiverABSwitchState_Object = MibTableColumn
fnOpticalReceiverABSwitchState = _FnOpticalReceiverABSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 4),
    _FnOpticalReceiverABSwitchState_Type()
)
fnOpticalReceiverABSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchState.setStatus("mandatory")


class _FnOpticalReceiverABSwitchSetting_Type(Integer32):
    """Custom type fnOpticalReceiverABSwitchSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("forcePathA", 1),
          ("forcePathB", 2),
          ("preferPathA", 3),
          ("preferPathB", 4),
          ("default", 5))
    )


_FnOpticalReceiverABSwitchSetting_Type.__name__ = "Integer32"
_FnOpticalReceiverABSwitchSetting_Object = MibTableColumn
fnOpticalReceiverABSwitchSetting = _FnOpticalReceiverABSwitchSetting_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 5),
    _FnOpticalReceiverABSwitchSetting_Type()
)
fnOpticalReceiverABSwitchSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchSetting.setStatus("optional")


class _FnOpticalReceiverABSwitchSettingAccess_Type(Integer32):
    """Custom type fnOpticalReceiverABSwitchSettingAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("noAccess", 2))
    )


_FnOpticalReceiverABSwitchSettingAccess_Type.__name__ = "Integer32"
_FnOpticalReceiverABSwitchSettingAccess_Object = MibTableColumn
fnOpticalReceiverABSwitchSettingAccess = _FnOpticalReceiverABSwitchSettingAccess_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 6),
    _FnOpticalReceiverABSwitchSettingAccess_Type()
)
fnOpticalReceiverABSwitchSettingAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchSettingAccess.setStatus("optional")


class _FnOpticalReceiverABSwitchControl_Type(Integer32):
    """Custom type fnOpticalReceiverABSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FnOpticalReceiverABSwitchControl_Type.__name__ = "Integer32"
_FnOpticalReceiverABSwitchControl_Object = MibTableColumn
fnOpticalReceiverABSwitchControl = _FnOpticalReceiverABSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 13, 1, 7),
    _FnOpticalReceiverABSwitchControl_Type()
)
fnOpticalReceiverABSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fnOpticalReceiverABSwitchControl.setStatus("optional")


class _FnLinePowerVoltage1_Type(Integer32):
    """Custom type fnLinePowerVoltage1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnLinePowerVoltage1_Type.__name__ = "Integer32"
_FnLinePowerVoltage1_Object = MibScalar
fnLinePowerVoltage1 = _FnLinePowerVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 14),
    _FnLinePowerVoltage1_Type()
)
fnLinePowerVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLinePowerVoltage1.setStatus("optional")


class _FnLinePowerVoltage2_Type(Integer32):
    """Custom type fnLinePowerVoltage2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnLinePowerVoltage2_Type.__name__ = "Integer32"
_FnLinePowerVoltage2_Object = MibScalar
fnLinePowerVoltage2 = _FnLinePowerVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 15),
    _FnLinePowerVoltage2_Type()
)
fnLinePowerVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLinePowerVoltage2.setStatus("optional")


class _FnLinePowerCurrent_Type(Integer32):
    """Custom type fnLinePowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnLinePowerCurrent_Type.__name__ = "Integer32"
_FnLinePowerCurrent_Object = MibScalar
fnLinePowerCurrent = _FnLinePowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 16),
    _FnLinePowerCurrent_Type()
)
fnLinePowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnLinePowerCurrent.setStatus("optional")


class _FnNumberDCPowerSupply_Type(Integer32):
    """Custom type fnNumberDCPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FnNumberDCPowerSupply_Type.__name__ = "Integer32"
_FnNumberDCPowerSupply_Object = MibScalar
fnNumberDCPowerSupply = _FnNumberDCPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 17),
    _FnNumberDCPowerSupply_Type()
)
fnNumberDCPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnNumberDCPowerSupply.setStatus("mandatory")


class _FnDCPowerSupplyMode_Type(Integer32):
    """Custom type fnDCPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadsharing", 1),
          ("switchedRedundant", 2))
    )


_FnDCPowerSupplyMode_Type.__name__ = "Integer32"
_FnDCPowerSupplyMode_Object = MibScalar
fnDCPowerSupplyMode = _FnDCPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 18),
    _FnDCPowerSupplyMode_Type()
)
fnDCPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDCPowerSupplyMode.setStatus("optional")
_FnDCPowerTable_Object = MibTable
fnDCPowerTable = _FnDCPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19)
)
if mibBuilder.loadTexts:
    fnDCPowerTable.setStatus("mandatory")
_FnDCPowerEntry_Object = MibTableRow
fnDCPowerEntry = _FnDCPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19, 1)
)
fnDCPowerEntry.setIndexNames(
    (0, "SCTE-HMS-FIBERNODE-MIB", "fnDCPowerIndex"),
)
if mibBuilder.loadTexts:
    fnDCPowerEntry.setStatus("mandatory")
_FnDCPowerIndex_Type = Integer32
_FnDCPowerIndex_Object = MibTableColumn
fnDCPowerIndex = _FnDCPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19, 1, 1),
    _FnDCPowerIndex_Type()
)
fnDCPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDCPowerIndex.setStatus("mandatory")


class _FnDCPowerVoltage_Type(Integer32):
    """Custom type fnDCPowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_FnDCPowerVoltage_Type.__name__ = "Integer32"
_FnDCPowerVoltage_Object = MibTableColumn
fnDCPowerVoltage = _FnDCPowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19, 1, 2),
    _FnDCPowerVoltage_Type()
)
fnDCPowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDCPowerVoltage.setStatus("mandatory")


class _FnDCPowerCurrent_Type(Integer32):
    """Custom type fnDCPowerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FnDCPowerCurrent_Type.__name__ = "Integer32"
_FnDCPowerCurrent_Object = MibTableColumn
fnDCPowerCurrent = _FnDCPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19, 1, 3),
    _FnDCPowerCurrent_Type()
)
fnDCPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDCPowerCurrent.setStatus("optional")
_FnDCPowerName_Type = DisplayString
_FnDCPowerName_Object = MibTableColumn
fnDCPowerName = _FnDCPowerName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 5, 19, 1, 4),
    _FnDCPowerName_Type()
)
fnDCPowerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fnDCPowerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-FIBERNODE-MIB",
    **{"fnAdminGroup": fnAdminGroup,
       "fnVendorOID": fnVendorOID,
       "fnDeviceId": fnDeviceId,
       "fnNumberReturnLaser": fnNumberReturnLaser,
       "fnReturnLaserTable": fnReturnLaserTable,
       "fnReturnLaserEntry": fnReturnLaserEntry,
       "fnReturnLaserIndex": fnReturnLaserIndex,
       "fnReturnLaserCurrent": fnReturnLaserCurrent,
       "fnReturnLaserTemp": fnReturnLaserTemp,
       "fnReturnLaserControl": fnReturnLaserControl,
       "fnReturnLaserType": fnReturnLaserType,
       "fnReturnLaserWavelength": fnReturnLaserWavelength,
       "fnReturnLaserOpticalPower": fnReturnLaserOpticalPower,
       "fnReturnLaserRFActive": fnReturnLaserRFActive,
       "fnNumberOpticalReceiver": fnNumberOpticalReceiver,
       "fnOpticalReceiverTable": fnOpticalReceiverTable,
       "fnOpticalReceiverEntry": fnOpticalReceiverEntry,
       "fnOpticalReceiverIndex": fnOpticalReceiverIndex,
       "fnOpticalReceiverPower": fnOpticalReceiverPower,
       "fnOpticalReceiverState": fnOpticalReceiverState,
       "fnOpticalReceiverRFActive": fnOpticalReceiverRFActive,
       "fnOpticalReceiverCurrent": fnOpticalReceiverCurrent,
       "fnOpticalAmpPresent": fnOpticalAmpPresent,
       "fnNumberRFActives": fnNumberRFActives,
       "fnRFActiveTable": fnRFActiveTable,
       "fnRFActiveEntry": fnRFActiveEntry,
       "fnRFActiveIndex": fnRFActiveIndex,
       "fnRFActiveControlType": fnRFActiveControlType,
       "fnRFActiveOutputLevel": fnRFActiveOutputLevel,
       "fnRFActiveCurrent": fnRFActiveCurrent,
       "fnRFActiveControlLevel": fnRFActiveControlLevel,
       "fnNumberRFPort": fnNumberRFPort,
       "fnPortMasterAttenuationControl": fnPortMasterAttenuationControl,
       "fnRFPortTable": fnRFPortTable,
       "fnRFPortEntry": fnRFPortEntry,
       "fnRFPortIndex": fnRFPortIndex,
       "fnRFPortControlType": fnRFPortControlType,
       "fnRFPortControlLevel": fnRFPortControlLevel,
       "fnRFPortOutputRFLevel": fnRFPortOutputRFLevel,
       "fnRFPortRFActive": fnRFPortRFActive,
       "fnRFPortName": fnRFPortName,
       "fnRFPortReverseAttenuationControl": fnRFPortReverseAttenuationControl,
       "fnNumberABSwitch": fnNumberABSwitch,
       "fnABSwitchTable": fnABSwitchTable,
       "fnABSwitchEntry": fnABSwitchEntry,
       "fnABSwitchIndex": fnABSwitchIndex,
       "fnOpticalReceiverABSwitchFeedA": fnOpticalReceiverABSwitchFeedA,
       "fnOpticalReceiverABSwitchFeedB": fnOpticalReceiverABSwitchFeedB,
       "fnOpticalReceiverABSwitchState": fnOpticalReceiverABSwitchState,
       "fnOpticalReceiverABSwitchSetting": fnOpticalReceiverABSwitchSetting,
       "fnOpticalReceiverABSwitchSettingAccess": fnOpticalReceiverABSwitchSettingAccess,
       "fnOpticalReceiverABSwitchControl": fnOpticalReceiverABSwitchControl,
       "fnLinePowerVoltage1": fnLinePowerVoltage1,
       "fnLinePowerVoltage2": fnLinePowerVoltage2,
       "fnLinePowerCurrent": fnLinePowerCurrent,
       "fnNumberDCPowerSupply": fnNumberDCPowerSupply,
       "fnDCPowerSupplyMode": fnDCPowerSupplyMode,
       "fnDCPowerTable": fnDCPowerTable,
       "fnDCPowerEntry": fnDCPowerEntry,
       "fnDCPowerIndex": fnDCPowerIndex,
       "fnDCPowerVoltage": fnDCPowerVoltage,
       "fnDCPowerCurrent": fnDCPowerCurrent,
       "fnDCPowerName": fnDCPowerName}
)
