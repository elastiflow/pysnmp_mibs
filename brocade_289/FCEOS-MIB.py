# SNMP MIB module (FCEOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_289/FCEOS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:30:56 2025
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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )





class FcEosSysOperStatus(Integer32):
    """Custom type FcEosSysOperStatus based on Integer32"""
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
        *(("operational", 1),
          ("redundant-failure", 2),
          ("minor-failure", 3),
          ("major-failure", 4),
          ("not-operational", 5))
    )





class FcEosFruCode(Integer32):
    """Custom type FcEosFruCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("fru-bkplane", 1),
          ("fru-ctp", 2),
          ("fru-sbar", 3),
          ("fru-fan2", 4),
          ("fru-fan", 5),
          ("fru-power", 6),
          ("fru-reserved", 7),
          ("fru-glsl", 8),
          ("fru-gsml", 9),
          ("fru-gxxl", 10),
          ("fru-gsf1", 11),
          ("fru-gsf2", 12),
          ("fru-glsr", 13),
          ("fru-gsmr", 14),
          ("fru-gxxr", 15),
          ("fru-fint1", 16),
          ("fru-xpm", 17),
          ("fru-ipm", 18),
          ("fru-qpm", 19))
    )





class FcEosFruPosition(Integer32):
    """Custom type FcEosFruPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class FcEosPortIndex(Integer32):
    """Custom type FcEosPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )





class FcEosPortPhyState(Integer32):
    """Custom type FcEosPortPhyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("psNotInstalled", 1),
          ("psAvailable", 2),
          ("psBlocked", 3),
          ("psUnavailable", 4),
          ("psLinkFailure", 5),
          ("psLinkFailLOL", 6),
          ("psIntDiags", 7),
          ("psExtLoop", 8),
          ("psPortFail", 9),
          ("psSR", 10),
          ("psLR", 11),
          ("psInaccessible", 12),
          ("psInactive", 13),
          ("psUnaddressable", 14),
          ("psDegraded", 15),
          ("psDisabled", 16),
          ("psInvalidAttach", 17),
          ("psSegmented", 18),
          ("other", 19))
    )





class FcEosPortWWN(OctetString):
    """Custom type FcEosPortWWN based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class FcEosPortList(OctetString):
    """Custom type FcEosPortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32





class LoopPortALPA(OctetString):
    """Custom type LoopPortALPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16





class VirtualPortNPIV(OctetString):
    """Custom type VirtualPortNPIV based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_McData_ObjectIdentity = ObjectIdentity
mcData = _McData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289)
)
_CommDev_ObjectIdentity = ObjectIdentity
commDev = _CommDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2)
)
_FibreChannel_ObjectIdentity = ObjectIdentity
fibreChannel = _FibreChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1)
)
_FcSwitch_ObjectIdentity = ObjectIdentity
fcSwitch = _FcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1)
)
_FcEos_ObjectIdentity = ObjectIdentity
fcEos = _FcEos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2)
)
_FcEosSys_ObjectIdentity = ObjectIdentity
fcEosSys = _FcEosSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1)
)


class _FcEosSysCurrentDate_Type(DisplayString):
    """Custom type fcEosSysCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysCurrentDate_Type.__name__ = "DisplayString"
_FcEosSysCurrentDate_Object = MibScalar
fcEosSysCurrentDate = _FcEosSysCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 1),
    _FcEosSysCurrentDate_Type()
)
fcEosSysCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysCurrentDate.setStatus("mandatory")


class _FcEosSysBootDate_Type(DisplayString):
    """Custom type fcEosSysBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysBootDate_Type.__name__ = "DisplayString"
_FcEosSysBootDate_Object = MibScalar
fcEosSysBootDate = _FcEosSysBootDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 2),
    _FcEosSysBootDate_Type()
)
fcEosSysBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysBootDate.setStatus("mandatory")


class _FcEosSysFirmwareVersion_Type(DisplayString):
    """Custom type fcEosSysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_FcEosSysFirmwareVersion_Type.__name__ = "DisplayString"
_FcEosSysFirmwareVersion_Object = MibScalar
fcEosSysFirmwareVersion = _FcEosSysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 3),
    _FcEosSysFirmwareVersion_Type()
)
fcEosSysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysFirmwareVersion.setStatus("mandatory")


class _FcEosSysTypeNum_Type(DisplayString):
    """Custom type fcEosSysTypeNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysTypeNum_Type.__name__ = "DisplayString"
_FcEosSysTypeNum_Object = MibScalar
fcEosSysTypeNum = _FcEosSysTypeNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 4),
    _FcEosSysTypeNum_Type()
)
fcEosSysTypeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysTypeNum.setStatus("mandatory")


class _FcEosSysModelNum_Type(DisplayString):
    """Custom type fcEosSysModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysModelNum_Type.__name__ = "DisplayString"
_FcEosSysModelNum_Object = MibScalar
fcEosSysModelNum = _FcEosSysModelNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 5),
    _FcEosSysModelNum_Type()
)
fcEosSysModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysModelNum.setStatus("mandatory")


class _FcEosSysMfg_Type(DisplayString):
    """Custom type fcEosSysMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysMfg_Type.__name__ = "DisplayString"
_FcEosSysMfg_Object = MibScalar
fcEosSysMfg = _FcEosSysMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 6),
    _FcEosSysMfg_Type()
)
fcEosSysMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysMfg.setStatus("mandatory")


class _FcEosSysPlantOfMfg_Type(DisplayString):
    """Custom type fcEosSysPlantOfMfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysPlantOfMfg_Type.__name__ = "DisplayString"
_FcEosSysPlantOfMfg_Object = MibScalar
fcEosSysPlantOfMfg = _FcEosSysPlantOfMfg_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 7),
    _FcEosSysPlantOfMfg_Type()
)
fcEosSysPlantOfMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysPlantOfMfg.setStatus("mandatory")


class _FcEosSysEcLevel_Type(DisplayString):
    """Custom type fcEosSysEcLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysEcLevel_Type.__name__ = "DisplayString"
_FcEosSysEcLevel_Object = MibScalar
fcEosSysEcLevel = _FcEosSysEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 8),
    _FcEosSysEcLevel_Type()
)
fcEosSysEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysEcLevel.setStatus("mandatory")


class _FcEosSysSerialNum_Type(DisplayString):
    """Custom type fcEosSysSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysSerialNum_Type.__name__ = "DisplayString"
_FcEosSysSerialNum_Object = MibScalar
fcEosSysSerialNum = _FcEosSysSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 9),
    _FcEosSysSerialNum_Type()
)
fcEosSysSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysSerialNum.setStatus("mandatory")
_FcEosSysOperStatus_Type = FcEosSysOperStatus
_FcEosSysOperStatus_Object = MibScalar
fcEosSysOperStatus = _FcEosSysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 10),
    _FcEosSysOperStatus_Type()
)
fcEosSysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysOperStatus.setStatus("mandatory")


class _FcEosSysState_Type(Integer32):
    """Custom type fcEosSysState based on Integer32"""
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
        *(("online", 1),
          ("coming-online", 2),
          ("offline", 3),
          ("going-offline", 4))
    )


_FcEosSysState_Type.__name__ = "Integer32"
_FcEosSysState_Object = MibScalar
fcEosSysState = _FcEosSysState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 11),
    _FcEosSysState_Type()
)
fcEosSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysState.setStatus("mandatory")


class _FcEosSysAdmStatus_Type(Integer32):
    """Custom type fcEosSysAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_FcEosSysAdmStatus_Type.__name__ = "Integer32"
_FcEosSysAdmStatus_Object = MibScalar
fcEosSysAdmStatus = _FcEosSysAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 12),
    _FcEosSysAdmStatus_Type()
)
fcEosSysAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysAdmStatus.setStatus("mandatory")


class _FcEosSysConfigSpeed_Type(Integer32):
    """Custom type fcEosSysConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("one-gig", 1),
          ("two-gig", 2),
          ("four-gig", 4))
    )


_FcEosSysConfigSpeed_Type.__name__ = "Integer32"
_FcEosSysConfigSpeed_Object = MibScalar
fcEosSysConfigSpeed = _FcEosSysConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 13),
    _FcEosSysConfigSpeed_Type()
)
fcEosSysConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysConfigSpeed.setStatus("mandatory")
_FcEosSysOpenTrunking_Type = TruthValue
_FcEosSysOpenTrunking_Object = MibScalar
fcEosSysOpenTrunking = _FcEosSysOpenTrunking_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 14),
    _FcEosSysOpenTrunking_Type()
)
fcEosSysOpenTrunking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysOpenTrunking.setStatus("mandatory")


class _FcEosSysSwitchName_Type(DisplayString):
    """Custom type fcEosSysSwitchName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosSysSwitchName_Type.__name__ = "DisplayString"
_FcEosSysSwitchName_Object = MibScalar
fcEosSysSwitchName = _FcEosSysSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 15),
    _FcEosSysSwitchName_Type()
)
fcEosSysSwitchName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysSwitchName.setStatus("mandatory")


class _FcEosSysSwitchId_Type(OctetString):
    """Custom type fcEosSysSwitchId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosSysSwitchId_Type.__name__ = "OctetString"
_FcEosSysSwitchId_Object = MibScalar
fcEosSysSwitchId = _FcEosSysSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 16),
    _FcEosSysSwitchId_Type()
)
fcEosSysSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosSysSwitchId.setStatus("mandatory")
_FcEosSysNPIV_Type = TruthValue
_FcEosSysNPIV_Object = MibScalar
fcEosSysNPIV = _FcEosSysNPIV_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 17),
    _FcEosSysNPIV_Type()
)
fcEosSysNPIV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysNPIV.setStatus("mandatory")


class _FcEosSysDomainIDOffset_Type(Integer32):
    """Custom type fcEosSysDomainIDOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              64,
              96,
              128,
              160,
              192,
              239)
        )
    )
    namedValues = NamedValues(
        *(("offset-0x00", 0),
          ("offset-0x20", 32),
          ("offset-0x40", 64),
          ("offset-0x60", 96),
          ("offset-0x80", 128),
          ("offset-0xA0", 160),
          ("offset-0xC0", 192),
          ("offset-0xEF", 239))
    )


_FcEosSysDomainIDOffset_Type.__name__ = "Integer32"
_FcEosSysDomainIDOffset_Object = MibScalar
fcEosSysDomainIDOffset = _FcEosSysDomainIDOffset_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 1, 18),
    _FcEosSysDomainIDOffset_Type()
)
fcEosSysDomainIDOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosSysDomainIDOffset.setStatus("mandatory")
_FcEosFru_ObjectIdentity = ObjectIdentity
fcEosFru = _FcEosFru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2)
)
_FcEosFruTable_Object = MibTable
fcEosFruTable = _FcEosFruTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fcEosFruTable.setStatus("mandatory")
_FcEosFruEntry_Object = MibTableRow
fcEosFruEntry = _FcEosFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1)
)
fcEosFruEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosFruCode"),
    (0, "FCEOS-MIB", "fcEosFruPosition"),
)
if mibBuilder.loadTexts:
    fcEosFruEntry.setStatus("mandatory")
_FcEosFruCode_Type = FcEosFruCode
_FcEosFruCode_Object = MibTableColumn
fcEosFruCode = _FcEosFruCode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 1),
    _FcEosFruCode_Type()
)
fcEosFruCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruCode.setStatus("mandatory")
_FcEosFruPosition_Type = FcEosFruPosition
_FcEosFruPosition_Object = MibTableColumn
fcEosFruPosition = _FcEosFruPosition_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 2),
    _FcEosFruPosition_Type()
)
fcEosFruPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruPosition.setStatus("mandatory")


class _FcEosFruStatus_Type(Integer32):
    """Custom type fcEosFruStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("backup", 2),
          ("update-busy", 3),
          ("failed", 4))
    )


_FcEosFruStatus_Type.__name__ = "Integer32"
_FcEosFruStatus_Object = MibTableColumn
fcEosFruStatus = _FcEosFruStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 3),
    _FcEosFruStatus_Type()
)
fcEosFruStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruStatus.setStatus("mandatory")


class _FcEosFruPartNumber_Type(DisplayString):
    """Custom type fcEosFruPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FcEosFruPartNumber_Type.__name__ = "DisplayString"
_FcEosFruPartNumber_Object = MibTableColumn
fcEosFruPartNumber = _FcEosFruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 4),
    _FcEosFruPartNumber_Type()
)
fcEosFruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruPartNumber.setStatus("mandatory")


class _FcEosFruSerialNumber_Type(DisplayString):
    """Custom type fcEosFruSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FcEosFruSerialNumber_Type.__name__ = "DisplayString"
_FcEosFruSerialNumber_Object = MibTableColumn
fcEosFruSerialNumber = _FcEosFruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 5),
    _FcEosFruSerialNumber_Type()
)
fcEosFruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruSerialNumber.setStatus("mandatory")
_FcEosFruPowerOnHours_Type = Counter32
_FcEosFruPowerOnHours_Object = MibTableColumn
fcEosFruPowerOnHours = _FcEosFruPowerOnHours_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 6),
    _FcEosFruPowerOnHours_Type()
)
fcEosFruPowerOnHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruPowerOnHours.setStatus("mandatory")


class _FcEosFruTestDate_Type(DisplayString):
    """Custom type fcEosFruTestDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FcEosFruTestDate_Type.__name__ = "DisplayString"
_FcEosFruTestDate_Object = MibTableColumn
fcEosFruTestDate = _FcEosFruTestDate_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 2, 1, 1, 7),
    _FcEosFruTestDate_Type()
)
fcEosFruTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosFruTestDate.setStatus("mandatory")
_FcEosPort_ObjectIdentity = ObjectIdentity
fcEosPort = _FcEosPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3)
)
_FcEosPortTable_Object = MibTable
fcEosPortTable = _FcEosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fcEosPortTable.setStatus("mandatory")
_FcEosPortEntry_Object = MibTableRow
fcEosPortEntry = _FcEosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1)
)
fcEosPortEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosPortIndex"),
)
if mibBuilder.loadTexts:
    fcEosPortEntry.setStatus("mandatory")
_FcEosPortIndex_Type = FcEosPortIndex
_FcEosPortIndex_Object = MibTableColumn
fcEosPortIndex = _FcEosPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 1),
    _FcEosPortIndex_Type()
)
fcEosPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortIndex.setStatus("mandatory")
_FcEosPortPhyState_Type = FcEosPortPhyState
_FcEosPortPhyState_Object = MibTableColumn
fcEosPortPhyState = _FcEosPortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 2),
    _FcEosPortPhyState_Type()
)
fcEosPortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortPhyState.setStatus("mandatory")


class _FcEosPortOpStatus_Type(Integer32):
    """Custom type fcEosPortOpStatus based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_FcEosPortOpStatus_Type.__name__ = "Integer32"
_FcEosPortOpStatus_Object = MibTableColumn
fcEosPortOpStatus = _FcEosPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 3),
    _FcEosPortOpStatus_Type()
)
fcEosPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortOpStatus.setStatus("mandatory")


class _FcEosPortAdmStatus_Type(Integer32):
    """Custom type fcEosPortAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("testing", 3))
    )


_FcEosPortAdmStatus_Type.__name__ = "Integer32"
_FcEosPortAdmStatus_Object = MibTableColumn
fcEosPortAdmStatus = _FcEosPortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 4),
    _FcEosPortAdmStatus_Type()
)
fcEosPortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortAdmStatus.setStatus("mandatory")


class _FcEosPortConnector_Type(Integer32):
    """Custom type fcEosPortConnector based on Integer32"""
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
        *(("unknown", 1),
          ("lc", 2),
          ("mt-rj", 3),
          ("mu", 4),
          ("internal-port", 5))
    )


_FcEosPortConnector_Type.__name__ = "Integer32"
_FcEosPortConnector_Object = MibTableColumn
fcEosPortConnector = _FcEosPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 5),
    _FcEosPortConnector_Type()
)
fcEosPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortConnector.setStatus("mandatory")


class _FcEosPortDistance_Type(Integer32):
    """Custom type fcEosPortDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcEosPortDistance_Type.__name__ = "Integer32"
_FcEosPortDistance_Object = MibTableColumn
fcEosPortDistance = _FcEosPortDistance_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 6),
    _FcEosPortDistance_Type()
)
fcEosPortDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortDistance.setStatus("mandatory")


class _FcEosPortXceiverType_Type(Integer32):
    """Custom type fcEosPortXceiverType based on Integer32"""
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
        *(("unknown", 1),
          ("longDistance", 2),
          ("longWaveLaser-LL", 3),
          ("shortWaveLaser-OFC", 4),
          ("shortWaveLaser-noOFC", 5),
          ("longWaveLaser-LC", 6))
    )


_FcEosPortXceiverType_Type.__name__ = "Integer32"
_FcEosPortXceiverType_Object = MibTableColumn
fcEosPortXceiverType = _FcEosPortXceiverType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 7),
    _FcEosPortXceiverType_Type()
)
fcEosPortXceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortXceiverType.setStatus("mandatory")


class _FcEosPortMedia_Type(Integer32):
    """Custom type fcEosPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcEosPortMedia_Type.__name__ = "Integer32"
_FcEosPortMedia_Object = MibTableColumn
fcEosPortMedia = _FcEosPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 8),
    _FcEosPortMedia_Type()
)
fcEosPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortMedia.setStatus("mandatory")


class _FcEosPortSpeedCap_Type(Integer32):
    """Custom type fcEosPortSpeedCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcEosPortSpeedCap_Type.__name__ = "Integer32"
_FcEosPortSpeedCap_Object = MibTableColumn
fcEosPortSpeedCap = _FcEosPortSpeedCap_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 9),
    _FcEosPortSpeedCap_Type()
)
fcEosPortSpeedCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortSpeedCap.setStatus("mandatory")


class _FcEosPortConfigSpeed_Type(Integer32):
    """Custom type fcEosPortConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("one-gig", 1),
          ("two-gig", 2),
          ("negotiate", 3),
          ("four-gig", 4),
          ("ten-gig", 10))
    )


_FcEosPortConfigSpeed_Type.__name__ = "Integer32"
_FcEosPortConfigSpeed_Object = MibTableColumn
fcEosPortConfigSpeed = _FcEosPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 10),
    _FcEosPortConfigSpeed_Type()
)
fcEosPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortConfigSpeed.setStatus("mandatory")


class _FcEosPortOpSpeed_Type(Integer32):
    """Custom type fcEosPortOpSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("one-gig", 2),
          ("two-gig", 3),
          ("negotiate", 4),
          ("four-gig", 5),
          ("ten-gig", 10))
    )


_FcEosPortOpSpeed_Type.__name__ = "Integer32"
_FcEosPortOpSpeed_Object = MibTableColumn
fcEosPortOpSpeed = _FcEosPortOpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 11),
    _FcEosPortOpSpeed_Type()
)
fcEosPortOpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortOpSpeed.setStatus("mandatory")


class _FcEosPortConfigType_Type(Integer32):
    """Custom type fcEosPortConfigType based on Integer32"""
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
        *(("gPort", 1),
          ("fPort", 2),
          ("ePort", 3),
          ("flPort", 4),
          ("fxPort", 5),
          ("gxPort", 6))
    )


_FcEosPortConfigType_Type.__name__ = "Integer32"
_FcEosPortConfigType_Object = MibTableColumn
fcEosPortConfigType = _FcEosPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 12),
    _FcEosPortConfigType_Type()
)
fcEosPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortConfigType.setStatus("mandatory")


class _FcEosPortOpType_Type(Integer32):
    """Custom type fcEosPortOpType based on Integer32"""
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
        *(("unknown", 1),
          ("ePort", 2),
          ("fPort", 3),
          ("flPort", 4))
    )


_FcEosPortOpType_Type.__name__ = "Integer32"
_FcEosPortOpType_Object = MibTableColumn
fcEosPortOpType = _FcEosPortOpType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 13),
    _FcEosPortOpType_Type()
)
fcEosPortOpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortOpType.setStatus("mandatory")
_FcEosPortALPAIndex_Type = LoopPortALPA
_FcEosPortALPAIndex_Object = MibTableColumn
fcEosPortALPAIndex = _FcEosPortALPAIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 14),
    _FcEosPortALPAIndex_Type()
)
fcEosPortALPAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortALPAIndex.setStatus("mandatory")
_FcEosPortFAN_Type = TruthValue
_FcEosPortFAN_Object = MibTableColumn
fcEosPortFAN = _FcEosPortFAN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 15),
    _FcEosPortFAN_Type()
)
fcEosPortFAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortFAN.setStatus("mandatory")
_FcEosPortTxWords32_Type = Counter32
_FcEosPortTxWords32_Object = MibTableColumn
fcEosPortTxWords32 = _FcEosPortTxWords32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 20),
    _FcEosPortTxWords32_Type()
)
fcEosPortTxWords32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxWords32.setStatus("mandatory")
_FcEosPortRxWords32_Type = Counter32
_FcEosPortRxWords32_Object = MibTableColumn
fcEosPortRxWords32 = _FcEosPortRxWords32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 21),
    _FcEosPortRxWords32_Type()
)
fcEosPortRxWords32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxWords32.setStatus("mandatory")
_FcEosPortTxFrames32_Type = Counter32
_FcEosPortTxFrames32_Object = MibTableColumn
fcEosPortTxFrames32 = _FcEosPortTxFrames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 22),
    _FcEosPortTxFrames32_Type()
)
fcEosPortTxFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxFrames32.setStatus("mandatory")
_FcEosPortRxFrames32_Type = Counter32
_FcEosPortRxFrames32_Object = MibTableColumn
fcEosPortRxFrames32 = _FcEosPortRxFrames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 23),
    _FcEosPortRxFrames32_Type()
)
fcEosPortRxFrames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxFrames32.setStatus("mandatory")
_FcEosPortTxThroughput_Type = Counter32
_FcEosPortTxThroughput_Object = MibTableColumn
fcEosPortTxThroughput = _FcEosPortTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 24),
    _FcEosPortTxThroughput_Type()
)
fcEosPortTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxThroughput.setStatus("mandatory")
_FcEosPortRxThroughput_Type = Counter32
_FcEosPortRxThroughput_Object = MibTableColumn
fcEosPortRxThroughput = _FcEosPortRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 25),
    _FcEosPortRxThroughput_Type()
)
fcEosPortRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxThroughput.setStatus("mandatory")
_FcEosPortTxC2Words32_Type = Counter32
_FcEosPortTxC2Words32_Object = MibTableColumn
fcEosPortTxC2Words32 = _FcEosPortTxC2Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 30),
    _FcEosPortTxC2Words32_Type()
)
fcEosPortTxC2Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Words32.setStatus("mandatory")
_FcEosPortRxC2Words32_Type = Counter32
_FcEosPortRxC2Words32_Object = MibTableColumn
fcEosPortRxC2Words32 = _FcEosPortRxC2Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 31),
    _FcEosPortRxC2Words32_Type()
)
fcEosPortRxC2Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Words32.setStatus("mandatory")
_FcEosPortTxC2Frames32_Type = Counter32
_FcEosPortTxC2Frames32_Object = MibTableColumn
fcEosPortTxC2Frames32 = _FcEosPortTxC2Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 32),
    _FcEosPortTxC2Frames32_Type()
)
fcEosPortTxC2Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Frames32.setStatus("mandatory")
_FcEosPortRxC2Frames32_Type = Counter32
_FcEosPortRxC2Frames32_Object = MibTableColumn
fcEosPortRxC2Frames32 = _FcEosPortRxC2Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 33),
    _FcEosPortRxC2Frames32_Type()
)
fcEosPortRxC2Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Frames32.setStatus("mandatory")
_FcEosPortTxC2Octets32_Type = Counter32
_FcEosPortTxC2Octets32_Object = MibTableColumn
fcEosPortTxC2Octets32 = _FcEosPortTxC2Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 34),
    _FcEosPortTxC2Octets32_Type()
)
fcEosPortTxC2Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Octets32.setStatus("mandatory")
_FcEosPortRxC2Octets32_Type = Counter32
_FcEosPortRxC2Octets32_Object = MibTableColumn
fcEosPortRxC2Octets32 = _FcEosPortRxC2Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 35),
    _FcEosPortRxC2Octets32_Type()
)
fcEosPortRxC2Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Octets32.setStatus("mandatory")
_FcEosPortRxC2FabricReject32_Type = Counter32
_FcEosPortRxC2FabricReject32_Object = MibTableColumn
fcEosPortRxC2FabricReject32 = _FcEosPortRxC2FabricReject32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 36),
    _FcEosPortRxC2FabricReject32_Type()
)
fcEosPortRxC2FabricReject32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2FabricReject32.setStatus("mandatory")
_FcEosPortRxC2FabricBusy32_Type = Counter32
_FcEosPortRxC2FabricBusy32_Object = MibTableColumn
fcEosPortRxC2FabricBusy32 = _FcEosPortRxC2FabricBusy32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 37),
    _FcEosPortRxC2FabricBusy32_Type()
)
fcEosPortRxC2FabricBusy32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2FabricBusy32.setStatus("mandatory")
_FcEosPortTxC3Words32_Type = Counter32
_FcEosPortTxC3Words32_Object = MibTableColumn
fcEosPortTxC3Words32 = _FcEosPortTxC3Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 40),
    _FcEosPortTxC3Words32_Type()
)
fcEosPortTxC3Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Words32.setStatus("mandatory")
_FcEosPortRxC3Words32_Type = Counter32
_FcEosPortRxC3Words32_Object = MibTableColumn
fcEosPortRxC3Words32 = _FcEosPortRxC3Words32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 41),
    _FcEosPortRxC3Words32_Type()
)
fcEosPortRxC3Words32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Words32.setStatus("mandatory")
_FcEosPortTxC3Frames32_Type = Counter32
_FcEosPortTxC3Frames32_Object = MibTableColumn
fcEosPortTxC3Frames32 = _FcEosPortTxC3Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 42),
    _FcEosPortTxC3Frames32_Type()
)
fcEosPortTxC3Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Frames32.setStatus("mandatory")
_FcEosPortRxC3Frames32_Type = Counter32
_FcEosPortRxC3Frames32_Object = MibTableColumn
fcEosPortRxC3Frames32 = _FcEosPortRxC3Frames32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 43),
    _FcEosPortRxC3Frames32_Type()
)
fcEosPortRxC3Frames32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Frames32.setStatus("mandatory")
_FcEosPortTxC3Octets32_Type = Counter32
_FcEosPortTxC3Octets32_Object = MibTableColumn
fcEosPortTxC3Octets32 = _FcEosPortTxC3Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 44),
    _FcEosPortTxC3Octets32_Type()
)
fcEosPortTxC3Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Octets32.setStatus("mandatory")
_FcEosPortRxC3Octets32_Type = Counter32
_FcEosPortRxC3Octets32_Object = MibTableColumn
fcEosPortRxC3Octets32 = _FcEosPortRxC3Octets32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 45),
    _FcEosPortRxC3Octets32_Type()
)
fcEosPortRxC3Octets32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Octets32.setStatus("mandatory")
_FcEosPortC3Discards32_Type = Counter32
_FcEosPortC3Discards32_Object = MibTableColumn
fcEosPortC3Discards32 = _FcEosPortC3Discards32_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 46),
    _FcEosPortC3Discards32_Type()
)
fcEosPortC3Discards32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortC3Discards32.setStatus("mandatory")
_FcEosPortDiscardFrames_Type = Counter32
_FcEosPortDiscardFrames_Object = MibTableColumn
fcEosPortDiscardFrames = _FcEosPortDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 50),
    _FcEosPortDiscardFrames_Type()
)
fcEosPortDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortDiscardFrames.setStatus("mandatory")
_FcEosPortTxLinkResets_Type = Counter32
_FcEosPortTxLinkResets_Object = MibTableColumn
fcEosPortTxLinkResets = _FcEosPortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 51),
    _FcEosPortTxLinkResets_Type()
)
fcEosPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxLinkResets.setStatus("mandatory")
_FcEosPortRxLinkResets_Type = Counter32
_FcEosPortRxLinkResets_Object = MibTableColumn
fcEosPortRxLinkResets = _FcEosPortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 52),
    _FcEosPortRxLinkResets_Type()
)
fcEosPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxLinkResets.setStatus("mandatory")
_FcEosPortTxOLSs_Type = Counter32
_FcEosPortTxOLSs_Object = MibTableColumn
fcEosPortTxOLSs = _FcEosPortTxOLSs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 53),
    _FcEosPortTxOLSs_Type()
)
fcEosPortTxOLSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxOLSs.setStatus("mandatory")
_FcEosPortRxOLSs_Type = Counter32
_FcEosPortRxOLSs_Object = MibTableColumn
fcEosPortRxOLSs = _FcEosPortRxOLSs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 54),
    _FcEosPortRxOLSs_Type()
)
fcEosPortRxOLSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxOLSs.setStatus("mandatory")
_FcEosPortLIPsGenerated_Type = Counter32
_FcEosPortLIPsGenerated_Object = MibTableColumn
fcEosPortLIPsGenerated = _FcEosPortLIPsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 55),
    _FcEosPortLIPsGenerated_Type()
)
fcEosPortLIPsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortLIPsGenerated.setStatus("mandatory")
_FcEosPortLIPsDetected_Type = Counter32
_FcEosPortLIPsDetected_Object = MibTableColumn
fcEosPortLIPsDetected = _FcEosPortLIPsDetected_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 56),
    _FcEosPortLIPsDetected_Type()
)
fcEosPortLIPsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortLIPsDetected.setStatus("mandatory")
_FcEosPortAddrIDErrors_Type = Counter32
_FcEosPortAddrIDErrors_Object = MibTableColumn
fcEosPortAddrIDErrors = _FcEosPortAddrIDErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 58),
    _FcEosPortAddrIDErrors_Type()
)
fcEosPortAddrIDErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortAddrIDErrors.setStatus("mandatory")
_FcEosPortDelimiterErrors_Type = Counter32
_FcEosPortDelimiterErrors_Object = MibTableColumn
fcEosPortDelimiterErrors = _FcEosPortDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 59),
    _FcEosPortDelimiterErrors_Type()
)
fcEosPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortDelimiterErrors.setStatus("mandatory")
_FcEosPortSyncLosses_Type = Counter32
_FcEosPortSyncLosses_Object = MibTableColumn
fcEosPortSyncLosses = _FcEosPortSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 60),
    _FcEosPortSyncLosses_Type()
)
fcEosPortSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortSyncLosses.setStatus("mandatory")
_FcEosPortSigLosses_Type = Counter32
_FcEosPortSigLosses_Object = MibTableColumn
fcEosPortSigLosses = _FcEosPortSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 61),
    _FcEosPortSigLosses_Type()
)
fcEosPortSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortSigLosses.setStatus("mandatory")
_FcEosPortProtocolErrors_Type = Counter32
_FcEosPortProtocolErrors_Object = MibTableColumn
fcEosPortProtocolErrors = _FcEosPortProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 62),
    _FcEosPortProtocolErrors_Type()
)
fcEosPortProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortProtocolErrors.setStatus("mandatory")
_FcEosPortInvalidTxWords_Type = Counter32
_FcEosPortInvalidTxWords_Object = MibTableColumn
fcEosPortInvalidTxWords = _FcEosPortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 63),
    _FcEosPortInvalidTxWords_Type()
)
fcEosPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortInvalidTxWords.setStatus("mandatory")
_FcEosPortLinkFailures_Type = Counter32
_FcEosPortLinkFailures_Object = MibTableColumn
fcEosPortLinkFailures = _FcEosPortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 64),
    _FcEosPortLinkFailures_Type()
)
fcEosPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortLinkFailures.setStatus("mandatory")
_FcEosPortCrcs_Type = Counter32
_FcEosPortCrcs_Object = MibTableColumn
fcEosPortCrcs = _FcEosPortCrcs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 65),
    _FcEosPortCrcs_Type()
)
fcEosPortCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortCrcs.setStatus("mandatory")
_FcEosPortTruncs_Type = Counter32
_FcEosPortTruncs_Object = MibTableColumn
fcEosPortTruncs = _FcEosPortTruncs_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 66),
    _FcEosPortTruncs_Type()
)
fcEosPortTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTruncs.setStatus("mandatory")


class _FcEosPortTxWords64_Type(OctetString):
    """Custom type fcEosPortTxWords64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxWords64_Type.__name__ = "OctetString"
_FcEosPortTxWords64_Object = MibTableColumn
fcEosPortTxWords64 = _FcEosPortTxWords64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 67),
    _FcEosPortTxWords64_Type()
)
fcEosPortTxWords64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxWords64.setStatus("mandatory")


class _FcEosPortRxWords64_Type(OctetString):
    """Custom type fcEosPortRxWords64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxWords64_Type.__name__ = "OctetString"
_FcEosPortRxWords64_Object = MibTableColumn
fcEosPortRxWords64 = _FcEosPortRxWords64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 68),
    _FcEosPortRxWords64_Type()
)
fcEosPortRxWords64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxWords64.setStatus("mandatory")


class _FcEosPortTxFrames64_Type(OctetString):
    """Custom type fcEosPortTxFrames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxFrames64_Type.__name__ = "OctetString"
_FcEosPortTxFrames64_Object = MibTableColumn
fcEosPortTxFrames64 = _FcEosPortTxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 69),
    _FcEosPortTxFrames64_Type()
)
fcEosPortTxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxFrames64.setStatus("mandatory")


class _FcEosPortRxFrames64_Type(OctetString):
    """Custom type fcEosPortRxFrames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxFrames64_Type.__name__ = "OctetString"
_FcEosPortRxFrames64_Object = MibTableColumn
fcEosPortRxFrames64 = _FcEosPortRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 70),
    _FcEosPortRxFrames64_Type()
)
fcEosPortRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxFrames64.setStatus("mandatory")


class _FcEosPortTxC2Words64_Type(OctetString):
    """Custom type fcEosPortTxC2Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC2Words64_Type.__name__ = "OctetString"
_FcEosPortTxC2Words64_Object = MibTableColumn
fcEosPortTxC2Words64 = _FcEosPortTxC2Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 71),
    _FcEosPortTxC2Words64_Type()
)
fcEosPortTxC2Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Words64.setStatus("mandatory")


class _FcEosPortRxC2Words64_Type(OctetString):
    """Custom type fcEosPortRxC2Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC2Words64_Type.__name__ = "OctetString"
_FcEosPortRxC2Words64_Object = MibTableColumn
fcEosPortRxC2Words64 = _FcEosPortRxC2Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 72),
    _FcEosPortRxC2Words64_Type()
)
fcEosPortRxC2Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Words64.setStatus("mandatory")


class _FcEosPortTxC2Frames64_Type(OctetString):
    """Custom type fcEosPortTxC2Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC2Frames64_Type.__name__ = "OctetString"
_FcEosPortTxC2Frames64_Object = MibTableColumn
fcEosPortTxC2Frames64 = _FcEosPortTxC2Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 73),
    _FcEosPortTxC2Frames64_Type()
)
fcEosPortTxC2Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Frames64.setStatus("mandatory")


class _FcEosPortRxC2Frames64_Type(OctetString):
    """Custom type fcEosPortRxC2Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC2Frames64_Type.__name__ = "OctetString"
_FcEosPortRxC2Frames64_Object = MibTableColumn
fcEosPortRxC2Frames64 = _FcEosPortRxC2Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 74),
    _FcEosPortRxC2Frames64_Type()
)
fcEosPortRxC2Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Frames64.setStatus("mandatory")


class _FcEosPortTxC2Octets64_Type(OctetString):
    """Custom type fcEosPortTxC2Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC2Octets64_Type.__name__ = "OctetString"
_FcEosPortTxC2Octets64_Object = MibTableColumn
fcEosPortTxC2Octets64 = _FcEosPortTxC2Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 75),
    _FcEosPortTxC2Octets64_Type()
)
fcEosPortTxC2Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC2Octets64.setStatus("mandatory")


class _FcEosPortRxC2Octets64_Type(OctetString):
    """Custom type fcEosPortRxC2Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC2Octets64_Type.__name__ = "OctetString"
_FcEosPortRxC2Octets64_Object = MibTableColumn
fcEosPortRxC2Octets64 = _FcEosPortRxC2Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 76),
    _FcEosPortRxC2Octets64_Type()
)
fcEosPortRxC2Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC2Octets64.setStatus("mandatory")


class _FcEosPortTxC3Words64_Type(OctetString):
    """Custom type fcEosPortTxC3Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC3Words64_Type.__name__ = "OctetString"
_FcEosPortTxC3Words64_Object = MibTableColumn
fcEosPortTxC3Words64 = _FcEosPortTxC3Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 77),
    _FcEosPortTxC3Words64_Type()
)
fcEosPortTxC3Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Words64.setStatus("mandatory")


class _FcEosPortRxC3Words64_Type(OctetString):
    """Custom type fcEosPortRxC3Words64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC3Words64_Type.__name__ = "OctetString"
_FcEosPortRxC3Words64_Object = MibTableColumn
fcEosPortRxC3Words64 = _FcEosPortRxC3Words64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 78),
    _FcEosPortRxC3Words64_Type()
)
fcEosPortRxC3Words64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Words64.setStatus("mandatory")


class _FcEosPortTxC3Frames64_Type(OctetString):
    """Custom type fcEosPortTxC3Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC3Frames64_Type.__name__ = "OctetString"
_FcEosPortTxC3Frames64_Object = MibTableColumn
fcEosPortTxC3Frames64 = _FcEosPortTxC3Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 79),
    _FcEosPortTxC3Frames64_Type()
)
fcEosPortTxC3Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Frames64.setStatus("mandatory")


class _FcEosPortRxC3Frames64_Type(OctetString):
    """Custom type fcEosPortRxC3Frames64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC3Frames64_Type.__name__ = "OctetString"
_FcEosPortRxC3Frames64_Object = MibTableColumn
fcEosPortRxC3Frames64 = _FcEosPortRxC3Frames64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 80),
    _FcEosPortRxC3Frames64_Type()
)
fcEosPortRxC3Frames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Frames64.setStatus("mandatory")


class _FcEosPortTxC3Octets64_Type(OctetString):
    """Custom type fcEosPortTxC3Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortTxC3Octets64_Type.__name__ = "OctetString"
_FcEosPortTxC3Octets64_Object = MibTableColumn
fcEosPortTxC3Octets64 = _FcEosPortTxC3Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 81),
    _FcEosPortTxC3Octets64_Type()
)
fcEosPortTxC3Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxC3Octets64.setStatus("mandatory")


class _FcEosPortRxC3Octets64_Type(OctetString):
    """Custom type fcEosPortRxC3Octets64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortRxC3Octets64_Type.__name__ = "OctetString"
_FcEosPortRxC3Octets64_Object = MibTableColumn
fcEosPortRxC3Octets64 = _FcEosPortRxC3Octets64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 82),
    _FcEosPortRxC3Octets64_Type()
)
fcEosPortRxC3Octets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxC3Octets64.setStatus("mandatory")


class _FcEosPortC3Discards64_Type(OctetString):
    """Custom type fcEosPortC3Discards64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FcEosPortC3Discards64_Type.__name__ = "OctetString"
_FcEosPortC3Discards64_Object = MibTableColumn
fcEosPortC3Discards64 = _FcEosPortC3Discards64_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 83),
    _FcEosPortC3Discards64_Type()
)
fcEosPortC3Discards64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortC3Discards64.setStatus("mandatory")
_FcEosPortTxFlows_Type = Counter32
_FcEosPortTxFlows_Object = MibTableColumn
fcEosPortTxFlows = _FcEosPortTxFlows_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 100),
    _FcEosPortTxFlows_Type()
)
fcEosPortTxFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortTxFlows.setStatus("mandatory")
_FcEosPortRxFlows_Type = Counter32
_FcEosPortRxFlows_Object = MibTableColumn
fcEosPortRxFlows = _FcEosPortRxFlows_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 101),
    _FcEosPortRxFlows_Type()
)
fcEosPortRxFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortRxFlows.setStatus("mandatory")
_FcEosPortLinkTrapEnable_Type = TruthValue
_FcEosPortLinkTrapEnable_Object = MibTableColumn
fcEosPortLinkTrapEnable = _FcEosPortLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 140),
    _FcEosPortLinkTrapEnable_Type()
)
fcEosPortLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortLinkTrapEnable.setStatus("mandatory")


class _FcEosPortLinkEvent_Type(Integer32):
    """Custom type fcEosPortLinkEvent based on Integer32"""
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
        *(("bit-error", 1),
          ("loss-of-signal", 2),
          ("nos-received", 3),
          ("link-failure", 4),
          ("invalid-primitive-sequence", 5),
          ("link-established", 6),
          ("no-information", 7))
    )


_FcEosPortLinkEvent_Type.__name__ = "Integer32"
_FcEosPortLinkEvent_Object = MibTableColumn
fcEosPortLinkEvent = _FcEosPortLinkEvent_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 150),
    _FcEosPortLinkEvent_Type()
)
fcEosPortLinkEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortLinkEvent.setStatus("mandatory")


class _FcEosPortLinkEventTime_Type(DisplayString):
    """Custom type fcEosPortLinkEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosPortLinkEventTime_Type.__name__ = "DisplayString"
_FcEosPortLinkEventTime_Object = MibTableColumn
fcEosPortLinkEventTime = _FcEosPortLinkEventTime_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 151),
    _FcEosPortLinkEventTime_Type()
)
fcEosPortLinkEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortLinkEventTime.setStatus("mandatory")


class _FcEosPortName_Type(DisplayString):
    """Custom type fcEosPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FcEosPortName_Type.__name__ = "DisplayString"
_FcEosPortName_Object = MibTableColumn
fcEosPortName = _FcEosPortName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 152),
    _FcEosPortName_Type()
)
fcEosPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortName.setStatus("mandatory")
_FcEosPortWWN_Type = FcEosPortWWN
_FcEosPortWWN_Object = MibTableColumn
fcEosPortWWN = _FcEosPortWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 153),
    _FcEosPortWWN_Type()
)
fcEosPortWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortWWN.setStatus("mandatory")
_FcEosPortNPIVIndex_Type = VirtualPortNPIV
_FcEosPortNPIVIndex_Object = MibTableColumn
fcEosPortNPIVIndex = _FcEosPortNPIVIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 154),
    _FcEosPortNPIVIndex_Type()
)
fcEosPortNPIVIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortNPIVIndex.setStatus("mandatory")


class _FcEosPortNPIVMaxLogins_Type(Integer32):
    """Custom type fcEosPortNPIVMaxLogins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_FcEosPortNPIVMaxLogins_Type.__name__ = "Integer32"
_FcEosPortNPIVMaxLogins_Object = MibTableColumn
fcEosPortNPIVMaxLogins = _FcEosPortNPIVMaxLogins_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 155),
    _FcEosPortNPIVMaxLogins_Type()
)
fcEosPortNPIVMaxLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortNPIVMaxLogins.setStatus("mandatory")


class _FcEosPortOpMode_Type(Integer32):
    """Custom type fcEosPortOpMode based on Integer32"""
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
        *(("none", 0),
          ("inactive", 1),
          ("burst", 2),
          ("sustained", 3))
    )


_FcEosPortOpMode_Type.__name__ = "Integer32"
_FcEosPortOpMode_Object = MibTableColumn
fcEosPortOpMode = _FcEosPortOpMode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 156),
    _FcEosPortOpMode_Type()
)
fcEosPortOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortOpMode.setStatus("mandatory")


class _FcEosPortSpeedMode_Type(Integer32):
    """Custom type fcEosPortSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("onegig-none", 1),
          ("twogig-none", 2),
          ("tengig-none", 4),
          ("neg-none", 8),
          ("fourgig-none", 16),
          ("onegig-burst", 64),
          ("twogig-burst", 128),
          ("fourgig-sustained", 256),
          ("fourgig-burst", 512),
          ("neg-sustained", 1024),
          ("neg-burst", 2048),
          ("neg-2GMax", 4096))
    )


_FcEosPortSpeedMode_Type.__name__ = "Integer32"
_FcEosPortSpeedMode_Object = MibTableColumn
fcEosPortSpeedMode = _FcEosPortSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 3, 1, 1, 157),
    _FcEosPortSpeedMode_Type()
)
fcEosPortSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortSpeedMode.setStatus("mandatory")
_FcEosPortBinding_ObjectIdentity = ObjectIdentity
fcEosPortBinding = _FcEosPortBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4)
)
_FcEosPortBindingTable_Object = MibTable
fcEosPortBindingTable = _FcEosPortBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fcEosPortBindingTable.setStatus("mandatory")
_FcEosPortBindingEntry_Object = MibTableRow
fcEosPortBindingEntry = _FcEosPortBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1)
)
fcEosPortBindingEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosPortBindingIndex"),
)
if mibBuilder.loadTexts:
    fcEosPortBindingEntry.setStatus("mandatory")
_FcEosPortBindingIndex_Type = FcEosPortIndex
_FcEosPortBindingIndex_Object = MibTableColumn
fcEosPortBindingIndex = _FcEosPortBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 1),
    _FcEosPortBindingIndex_Type()
)
fcEosPortBindingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortBindingIndex.setStatus("mandatory")


class _FcEosPortBindingFlag_Type(Integer32):
    """Custom type fcEosPortBindingFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FcEosPortBindingFlag_Type.__name__ = "Integer32"
_FcEosPortBindingFlag_Object = MibTableColumn
fcEosPortBindingFlag = _FcEosPortBindingFlag_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 2),
    _FcEosPortBindingFlag_Type()
)
fcEosPortBindingFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortBindingFlag.setStatus("mandatory")
_FcEosPortConfiguredWWN_Type = FcEosPortWWN
_FcEosPortConfiguredWWN_Object = MibTableColumn
fcEosPortConfiguredWWN = _FcEosPortConfiguredWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 3),
    _FcEosPortConfiguredWWN_Type()
)
fcEosPortConfiguredWWN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcEosPortConfiguredWWN.setStatus("mandatory")
_FcEosPortAttachedWWN_Type = FcEosPortWWN
_FcEosPortAttachedWWN_Object = MibTableColumn
fcEosPortAttachedWWN = _FcEosPortAttachedWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 4, 1, 1, 4),
    _FcEosPortAttachedWWN_Type()
)
fcEosPortAttachedWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosPortAttachedWWN.setStatus("mandatory")
_FcEosZoning_ObjectIdentity = ObjectIdentity
fcEosZoning = _FcEosZoning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5)
)
_FcEosActiveZoneSetName_Type = DisplayString
_FcEosActiveZoneSetName_Object = MibScalar
fcEosActiveZoneSetName = _FcEosActiveZoneSetName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 1),
    _FcEosActiveZoneSetName_Type()
)
fcEosActiveZoneSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosActiveZoneSetName.setStatus("mandatory")
_FcEosActiveZoneCount_Type = Integer32
_FcEosActiveZoneCount_Object = MibScalar
fcEosActiveZoneCount = _FcEosActiveZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 2),
    _FcEosActiveZoneCount_Type()
)
fcEosActiveZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosActiveZoneCount.setStatus("mandatory")


class _FcEosDefaultZoneSetState_Type(Integer32):
    """Custom type fcEosDefaultZoneSetState based on Integer32"""
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


_FcEosDefaultZoneSetState_Type.__name__ = "Integer32"
_FcEosDefaultZoneSetState_Object = MibScalar
fcEosDefaultZoneSetState = _FcEosDefaultZoneSetState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 3),
    _FcEosDefaultZoneSetState_Type()
)
fcEosDefaultZoneSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosDefaultZoneSetState.setStatus("mandatory")


class _FcEosActiveZoneSetState_Type(Integer32):
    """Custom type fcEosActiveZoneSetState based on Integer32"""
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


_FcEosActiveZoneSetState_Type.__name__ = "Integer32"
_FcEosActiveZoneSetState_Object = MibScalar
fcEosActiveZoneSetState = _FcEosActiveZoneSetState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 4),
    _FcEosActiveZoneSetState_Type()
)
fcEosActiveZoneSetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosActiveZoneSetState.setStatus("mandatory")


class _FcEosHardwareEnforcedZoning_Type(Integer32):
    """Custom type fcEosHardwareEnforcedZoning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FcEosHardwareEnforcedZoning_Type.__name__ = "Integer32"
_FcEosHardwareEnforcedZoning_Object = MibScalar
fcEosHardwareEnforcedZoning = _FcEosHardwareEnforcedZoning_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 5),
    _FcEosHardwareEnforcedZoning_Type()
)
fcEosHardwareEnforcedZoning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosHardwareEnforcedZoning.setStatus("mandatory")
_FcEosActiveZoneTable_Object = MibTable
fcEosActiveZoneTable = _FcEosActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6)
)
if mibBuilder.loadTexts:
    fcEosActiveZoneTable.setStatus("mandatory")
_FcEosActiveZoneEntry_Object = MibTableRow
fcEosActiveZoneEntry = _FcEosActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1)
)
fcEosActiveZoneEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosZoneIndex"),
)
if mibBuilder.loadTexts:
    fcEosActiveZoneEntry.setStatus("mandatory")
_FcEosZoneIndex_Type = Integer32
_FcEosZoneIndex_Object = MibTableColumn
fcEosZoneIndex = _FcEosZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 1),
    _FcEosZoneIndex_Type()
)
fcEosZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosZoneIndex.setStatus("mandatory")
_FcEosZoneName_Type = DisplayString
_FcEosZoneName_Object = MibTableColumn
fcEosZoneName = _FcEosZoneName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 2),
    _FcEosZoneName_Type()
)
fcEosZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosZoneName.setStatus("mandatory")
_FcEosZoneMemberCount_Type = Integer32
_FcEosZoneMemberCount_Object = MibTableColumn
fcEosZoneMemberCount = _FcEosZoneMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 6, 1, 3),
    _FcEosZoneMemberCount_Type()
)
fcEosZoneMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosZoneMemberCount.setStatus("mandatory")
_FcEosActiveMemberTable_Object = MibTable
fcEosActiveMemberTable = _FcEosActiveMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    fcEosActiveMemberTable.setStatus("mandatory")
_FcEosActiveMemberEntry_Object = MibTableRow
fcEosActiveMemberEntry = _FcEosActiveMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1)
)
fcEosActiveMemberEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosMemberZoneIndex"),
    (0, "FCEOS-MIB", "fcEosMemberIndex"),
)
if mibBuilder.loadTexts:
    fcEosActiveMemberEntry.setStatus("mandatory")
_FcEosMemberZoneIndex_Type = Integer32
_FcEosMemberZoneIndex_Object = MibTableColumn
fcEosMemberZoneIndex = _FcEosMemberZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 1),
    _FcEosMemberZoneIndex_Type()
)
fcEosMemberZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberZoneIndex.setStatus("mandatory")
_FcEosMemberIndex_Type = Integer32
_FcEosMemberIndex_Object = MibTableColumn
fcEosMemberIndex = _FcEosMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 2),
    _FcEosMemberIndex_Type()
)
fcEosMemberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberIndex.setStatus("mandatory")


class _FcEosMemberType_Type(Integer32):
    """Custom type fcEosMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wwn", 1),
          ("portnumber", 2))
    )


_FcEosMemberType_Type.__name__ = "Integer32"
_FcEosMemberType_Object = MibTableColumn
fcEosMemberType = _FcEosMemberType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 3),
    _FcEosMemberType_Type()
)
fcEosMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberType.setStatus("mandatory")
_FcEosMemberWWN_Type = FcEosPortWWN
_FcEosMemberWWN_Object = MibTableColumn
fcEosMemberWWN = _FcEosMemberWWN_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 4),
    _FcEosMemberWWN_Type()
)
fcEosMemberWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberWWN.setStatus("mandatory")
_FcEosMemberDomainID_Type = Integer32
_FcEosMemberDomainID_Object = MibTableColumn
fcEosMemberDomainID = _FcEosMemberDomainID_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 5),
    _FcEosMemberDomainID_Type()
)
fcEosMemberDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberDomainID.setStatus("mandatory")
_FcEosMemberPortNumber_Type = Integer32
_FcEosMemberPortNumber_Object = MibTableColumn
fcEosMemberPortNumber = _FcEosMemberPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 5, 7, 1, 6),
    _FcEosMemberPortNumber_Type()
)
fcEosMemberPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosMemberPortNumber.setStatus("mandatory")
_FcEosTA_ObjectIdentity = ObjectIdentity
fcEosTA = _FcEosTA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6)
)
_FcEosTATable_Object = MibTable
fcEosTATable = _FcEosTATable_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    fcEosTATable.setStatus("mandatory")
_FcEosTAEntry_Object = MibTableRow
fcEosTAEntry = _FcEosTAEntry_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1)
)
fcEosTAEntry.setIndexNames(
    (0, "FCEOS-MIB", "fcEosTAIndex"),
)
if mibBuilder.loadTexts:
    fcEosTAEntry.setStatus("mandatory")
_FcEosTAIndex_Type = Integer32
_FcEosTAIndex_Object = MibTableColumn
fcEosTAIndex = _FcEosTAIndex_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 1),
    _FcEosTAIndex_Type()
)
fcEosTAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAIndex.setStatus("mandatory")


class _FcEosTAName_Type(DisplayString):
    """Custom type fcEosTAName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FcEosTAName_Type.__name__ = "DisplayString"
_FcEosTAName_Object = MibTableColumn
fcEosTAName = _FcEosTAName_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 2),
    _FcEosTAName_Type()
)
fcEosTAName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAName.setStatus("mandatory")


class _FcEosTAState_Type(Integer32):
    """Custom type fcEosTAState based on Integer32"""
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


_FcEosTAState_Type.__name__ = "Integer32"
_FcEosTAState_Object = MibTableColumn
fcEosTAState = _FcEosTAState_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 3),
    _FcEosTAState_Type()
)
fcEosTAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAState.setStatus("mandatory")


class _FcEosTAType_Type(Integer32):
    """Custom type fcEosTAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("throughput", 1),
          ("counter", 2))
    )


_FcEosTAType_Type.__name__ = "Integer32"
_FcEosTAType_Object = MibTableColumn
fcEosTAType = _FcEosTAType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 4),
    _FcEosTAType_Type()
)
fcEosTAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAType.setStatus("mandatory")


class _FcEosTAPortType_Type(Integer32):
    """Custom type fcEosTAPortType based on Integer32"""
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
        *(("list", 1),
          ("ePorts", 2),
          ("fPorts", 3),
          ("flPorts", 4))
    )


_FcEosTAPortType_Type.__name__ = "Integer32"
_FcEosTAPortType_Object = MibTableColumn
fcEosTAPortType = _FcEosTAPortType_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 5),
    _FcEosTAPortType_Type()
)
fcEosTAPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAPortType.setStatus("mandatory")
_FcEosTAPortList_Type = FcEosPortList
_FcEosTAPortList_Object = MibTableColumn
fcEosTAPortList = _FcEosTAPortList_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 6),
    _FcEosTAPortList_Type()
)
fcEosTAPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAPortList.setStatus("mandatory")
_FcEosTAInterval_Type = Integer32
_FcEosTAInterval_Object = MibTableColumn
fcEosTAInterval = _FcEosTAInterval_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 7),
    _FcEosTAInterval_Type()
)
fcEosTAInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTAInterval.setStatus("mandatory")
_FcEosTATriggerValue_Type = Integer32
_FcEosTATriggerValue_Object = MibTableColumn
fcEosTATriggerValue = _FcEosTATriggerValue_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 8),
    _FcEosTATriggerValue_Type()
)
fcEosTATriggerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTATriggerValue.setStatus("mandatory")


class _FcEosTTADirection_Type(Integer32):
    """Custom type fcEosTTADirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transmit", 1),
          ("receive", 2),
          ("either", 3))
    )


_FcEosTTADirection_Type.__name__ = "Integer32"
_FcEosTTADirection_Object = MibTableColumn
fcEosTTADirection = _FcEosTTADirection_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 9),
    _FcEosTTADirection_Type()
)
fcEosTTADirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTTADirection.setStatus("mandatory")
_FcEosTTATriggerDuration_Type = Integer32
_FcEosTTATriggerDuration_Object = MibTableColumn
fcEosTTATriggerDuration = _FcEosTTATriggerDuration_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 10),
    _FcEosTTATriggerDuration_Type()
)
fcEosTTATriggerDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosTTATriggerDuration.setStatus("mandatory")
_FcEosCTACounter_Type = Integer32
_FcEosCTACounter_Object = MibTableColumn
fcEosCTACounter = _FcEosCTACounter_Object(
    (1, 3, 6, 1, 4, 1, 289, 2, 1, 1, 2, 6, 1, 1, 11),
    _FcEosCTACounter_Type()
)
fcEosCTACounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcEosCTACounter.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fcEosPortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 1)
)
fcEosPortScn.setObjects(
    ("FCEOS-MIB", "fcEosPortOpStatus")
)
if mibBuilder.loadTexts:
    fcEosPortScn.setStatus(
        ""
    )

fcEosFruScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 2)
)
fcEosFruScn.setObjects(
    ("FCEOS-MIB", "fcEosFruStatus")
)
if mibBuilder.loadTexts:
    fcEosFruScn.setStatus(
        ""
    )

fcEosPortBindingViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 3)
)
fcEosPortBindingViolation.setObjects(
    ("FCEOS-MIB", "fcEosPortAttachedWWN")
)
if mibBuilder.loadTexts:
    fcEosPortBindingViolation.setStatus(
        ""
    )

fcEosThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 4)
)
fcEosThresholdAlert.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosTAIndex"))
)
if mibBuilder.loadTexts:
    fcEosThresholdAlert.setStatus(
        ""
    )

fcEosFruRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 5)
)
fcEosFruRemoved.setObjects(
      *(("FCEOS-MIB", "fcEosFruCode"),
        ("FCEOS-MIB", "fcEosFruPosition"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosFruRemoved.setStatus(
        ""
    )

fcEosFruActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 6)
)
fcEosFruActive.setObjects(
      *(("FCEOS-MIB", "fcEosFruCode"),
        ("FCEOS-MIB", "fcEosFruPosition"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosFruActive.setStatus(
        ""
    )

fcEosFruBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 7)
)
fcEosFruBackup.setObjects(
      *(("FCEOS-MIB", "fcEosFruCode"),
        ("FCEOS-MIB", "fcEosFruPosition"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosFruBackup.setStatus(
        ""
    )

fcEosFruUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 8)
)
fcEosFruUpdate.setObjects(
      *(("FCEOS-MIB", "fcEosFruCode"),
        ("FCEOS-MIB", "fcEosFruPosition"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosFruUpdate.setStatus(
        ""
    )

fcEosFruFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 9)
)
fcEosFruFailed.setObjects(
      *(("FCEOS-MIB", "fcEosFruCode"),
        ("FCEOS-MIB", "fcEosFruPosition"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosFruFailed.setStatus(
        ""
    )

fcEosLinkBitErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 10)
)
fcEosLinkBitErrorEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkBitErrorEvent.setStatus(
        ""
    )

fcEosLinkNoSignalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 11)
)
fcEosLinkNoSignalEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkNoSignalEvent.setStatus(
        ""
    )

fcEosLinkNOSEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 12)
)
fcEosLinkNOSEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkNOSEvent.setStatus(
        ""
    )

fcEosLinkFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 13)
)
fcEosLinkFailureEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkFailureEvent.setStatus(
        ""
    )

fcEosLinkInvalidEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 14)
)
fcEosLinkInvalidEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkInvalidEvent.setStatus(
        ""
    )

fcEosLinkAddedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 289, 0, 15)
)
fcEosLinkAddedEvent.setObjects(
      *(("FCEOS-MIB", "fcEosPortIndex"),
        ("FCEOS-MIB", "fcEosPortName"),
        ("FCEOS-MIB", "fcEosPortWWN"),
        ("FCEOS-MIB", "fcEosSysSwitchName"),
        ("FCEOS-MIB", "fcEosSysSwitchId"))
)
if mibBuilder.loadTexts:
    fcEosLinkAddedEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FCEOS-MIB",
    **{"DisplayString": DisplayString,
       "TruthValue": TruthValue,
       "FcEosSysOperStatus": FcEosSysOperStatus,
       "FcEosFruCode": FcEosFruCode,
       "FcEosFruPosition": FcEosFruPosition,
       "FcEosPortIndex": FcEosPortIndex,
       "FcEosPortPhyState": FcEosPortPhyState,
       "FcEosPortWWN": FcEosPortWWN,
       "FcEosPortList": FcEosPortList,
       "LoopPortALPA": LoopPortALPA,
       "VirtualPortNPIV": VirtualPortNPIV,
       "mcData": mcData,
       "fcEosPortScn": fcEosPortScn,
       "fcEosFruScn": fcEosFruScn,
       "fcEosPortBindingViolation": fcEosPortBindingViolation,
       "fcEosThresholdAlert": fcEosThresholdAlert,
       "fcEosFruRemoved": fcEosFruRemoved,
       "fcEosFruActive": fcEosFruActive,
       "fcEosFruBackup": fcEosFruBackup,
       "fcEosFruUpdate": fcEosFruUpdate,
       "fcEosFruFailed": fcEosFruFailed,
       "fcEosLinkBitErrorEvent": fcEosLinkBitErrorEvent,
       "fcEosLinkNoSignalEvent": fcEosLinkNoSignalEvent,
       "fcEosLinkNOSEvent": fcEosLinkNOSEvent,
       "fcEosLinkFailureEvent": fcEosLinkFailureEvent,
       "fcEosLinkInvalidEvent": fcEosLinkInvalidEvent,
       "fcEosLinkAddedEvent": fcEosLinkAddedEvent,
       "commDev": commDev,
       "fibreChannel": fibreChannel,
       "fcSwitch": fcSwitch,
       "fcEos": fcEos,
       "fcEosSys": fcEosSys,
       "fcEosSysCurrentDate": fcEosSysCurrentDate,
       "fcEosSysBootDate": fcEosSysBootDate,
       "fcEosSysFirmwareVersion": fcEosSysFirmwareVersion,
       "fcEosSysTypeNum": fcEosSysTypeNum,
       "fcEosSysModelNum": fcEosSysModelNum,
       "fcEosSysMfg": fcEosSysMfg,
       "fcEosSysPlantOfMfg": fcEosSysPlantOfMfg,
       "fcEosSysEcLevel": fcEosSysEcLevel,
       "fcEosSysSerialNum": fcEosSysSerialNum,
       "fcEosSysOperStatus": fcEosSysOperStatus,
       "fcEosSysState": fcEosSysState,
       "fcEosSysAdmStatus": fcEosSysAdmStatus,
       "fcEosSysConfigSpeed": fcEosSysConfigSpeed,
       "fcEosSysOpenTrunking": fcEosSysOpenTrunking,
       "fcEosSysSwitchName": fcEosSysSwitchName,
       "fcEosSysSwitchId": fcEosSysSwitchId,
       "fcEosSysNPIV": fcEosSysNPIV,
       "fcEosSysDomainIDOffset": fcEosSysDomainIDOffset,
       "fcEosFru": fcEosFru,
       "fcEosFruTable": fcEosFruTable,
       "fcEosFruEntry": fcEosFruEntry,
       "fcEosFruCode": fcEosFruCode,
       "fcEosFruPosition": fcEosFruPosition,
       "fcEosFruStatus": fcEosFruStatus,
       "fcEosFruPartNumber": fcEosFruPartNumber,
       "fcEosFruSerialNumber": fcEosFruSerialNumber,
       "fcEosFruPowerOnHours": fcEosFruPowerOnHours,
       "fcEosFruTestDate": fcEosFruTestDate,
       "fcEosPort": fcEosPort,
       "fcEosPortTable": fcEosPortTable,
       "fcEosPortEntry": fcEosPortEntry,
       "fcEosPortIndex": fcEosPortIndex,
       "fcEosPortPhyState": fcEosPortPhyState,
       "fcEosPortOpStatus": fcEosPortOpStatus,
       "fcEosPortAdmStatus": fcEosPortAdmStatus,
       "fcEosPortConnector": fcEosPortConnector,
       "fcEosPortDistance": fcEosPortDistance,
       "fcEosPortXceiverType": fcEosPortXceiverType,
       "fcEosPortMedia": fcEosPortMedia,
       "fcEosPortSpeedCap": fcEosPortSpeedCap,
       "fcEosPortConfigSpeed": fcEosPortConfigSpeed,
       "fcEosPortOpSpeed": fcEosPortOpSpeed,
       "fcEosPortConfigType": fcEosPortConfigType,
       "fcEosPortOpType": fcEosPortOpType,
       "fcEosPortALPAIndex": fcEosPortALPAIndex,
       "fcEosPortFAN": fcEosPortFAN,
       "fcEosPortTxWords32": fcEosPortTxWords32,
       "fcEosPortRxWords32": fcEosPortRxWords32,
       "fcEosPortTxFrames32": fcEosPortTxFrames32,
       "fcEosPortRxFrames32": fcEosPortRxFrames32,
       "fcEosPortTxThroughput": fcEosPortTxThroughput,
       "fcEosPortRxThroughput": fcEosPortRxThroughput,
       "fcEosPortTxC2Words32": fcEosPortTxC2Words32,
       "fcEosPortRxC2Words32": fcEosPortRxC2Words32,
       "fcEosPortTxC2Frames32": fcEosPortTxC2Frames32,
       "fcEosPortRxC2Frames32": fcEosPortRxC2Frames32,
       "fcEosPortTxC2Octets32": fcEosPortTxC2Octets32,
       "fcEosPortRxC2Octets32": fcEosPortRxC2Octets32,
       "fcEosPortRxC2FabricReject32": fcEosPortRxC2FabricReject32,
       "fcEosPortRxC2FabricBusy32": fcEosPortRxC2FabricBusy32,
       "fcEosPortTxC3Words32": fcEosPortTxC3Words32,
       "fcEosPortRxC3Words32": fcEosPortRxC3Words32,
       "fcEosPortTxC3Frames32": fcEosPortTxC3Frames32,
       "fcEosPortRxC3Frames32": fcEosPortRxC3Frames32,
       "fcEosPortTxC3Octets32": fcEosPortTxC3Octets32,
       "fcEosPortRxC3Octets32": fcEosPortRxC3Octets32,
       "fcEosPortC3Discards32": fcEosPortC3Discards32,
       "fcEosPortDiscardFrames": fcEosPortDiscardFrames,
       "fcEosPortTxLinkResets": fcEosPortTxLinkResets,
       "fcEosPortRxLinkResets": fcEosPortRxLinkResets,
       "fcEosPortTxOLSs": fcEosPortTxOLSs,
       "fcEosPortRxOLSs": fcEosPortRxOLSs,
       "fcEosPortLIPsGenerated": fcEosPortLIPsGenerated,
       "fcEosPortLIPsDetected": fcEosPortLIPsDetected,
       "fcEosPortAddrIDErrors": fcEosPortAddrIDErrors,
       "fcEosPortDelimiterErrors": fcEosPortDelimiterErrors,
       "fcEosPortSyncLosses": fcEosPortSyncLosses,
       "fcEosPortSigLosses": fcEosPortSigLosses,
       "fcEosPortProtocolErrors": fcEosPortProtocolErrors,
       "fcEosPortInvalidTxWords": fcEosPortInvalidTxWords,
       "fcEosPortLinkFailures": fcEosPortLinkFailures,
       "fcEosPortCrcs": fcEosPortCrcs,
       "fcEosPortTruncs": fcEosPortTruncs,
       "fcEosPortTxWords64": fcEosPortTxWords64,
       "fcEosPortRxWords64": fcEosPortRxWords64,
       "fcEosPortTxFrames64": fcEosPortTxFrames64,
       "fcEosPortRxFrames64": fcEosPortRxFrames64,
       "fcEosPortTxC2Words64": fcEosPortTxC2Words64,
       "fcEosPortRxC2Words64": fcEosPortRxC2Words64,
       "fcEosPortTxC2Frames64": fcEosPortTxC2Frames64,
       "fcEosPortRxC2Frames64": fcEosPortRxC2Frames64,
       "fcEosPortTxC2Octets64": fcEosPortTxC2Octets64,
       "fcEosPortRxC2Octets64": fcEosPortRxC2Octets64,
       "fcEosPortTxC3Words64": fcEosPortTxC3Words64,
       "fcEosPortRxC3Words64": fcEosPortRxC3Words64,
       "fcEosPortTxC3Frames64": fcEosPortTxC3Frames64,
       "fcEosPortRxC3Frames64": fcEosPortRxC3Frames64,
       "fcEosPortTxC3Octets64": fcEosPortTxC3Octets64,
       "fcEosPortRxC3Octets64": fcEosPortRxC3Octets64,
       "fcEosPortC3Discards64": fcEosPortC3Discards64,
       "fcEosPortTxFlows": fcEosPortTxFlows,
       "fcEosPortRxFlows": fcEosPortRxFlows,
       "fcEosPortLinkTrapEnable": fcEosPortLinkTrapEnable,
       "fcEosPortLinkEvent": fcEosPortLinkEvent,
       "fcEosPortLinkEventTime": fcEosPortLinkEventTime,
       "fcEosPortName": fcEosPortName,
       "fcEosPortWWN": fcEosPortWWN,
       "fcEosPortNPIVIndex": fcEosPortNPIVIndex,
       "fcEosPortNPIVMaxLogins": fcEosPortNPIVMaxLogins,
       "fcEosPortOpMode": fcEosPortOpMode,
       "fcEosPortSpeedMode": fcEosPortSpeedMode,
       "fcEosPortBinding": fcEosPortBinding,
       "fcEosPortBindingTable": fcEosPortBindingTable,
       "fcEosPortBindingEntry": fcEosPortBindingEntry,
       "fcEosPortBindingIndex": fcEosPortBindingIndex,
       "fcEosPortBindingFlag": fcEosPortBindingFlag,
       "fcEosPortConfiguredWWN": fcEosPortConfiguredWWN,
       "fcEosPortAttachedWWN": fcEosPortAttachedWWN,
       "fcEosZoning": fcEosZoning,
       "fcEosActiveZoneSetName": fcEosActiveZoneSetName,
       "fcEosActiveZoneCount": fcEosActiveZoneCount,
       "fcEosDefaultZoneSetState": fcEosDefaultZoneSetState,
       "fcEosActiveZoneSetState": fcEosActiveZoneSetState,
       "fcEosHardwareEnforcedZoning": fcEosHardwareEnforcedZoning,
       "fcEosActiveZoneTable": fcEosActiveZoneTable,
       "fcEosActiveZoneEntry": fcEosActiveZoneEntry,
       "fcEosZoneIndex": fcEosZoneIndex,
       "fcEosZoneName": fcEosZoneName,
       "fcEosZoneMemberCount": fcEosZoneMemberCount,
       "fcEosActiveMemberTable": fcEosActiveMemberTable,
       "fcEosActiveMemberEntry": fcEosActiveMemberEntry,
       "fcEosMemberZoneIndex": fcEosMemberZoneIndex,
       "fcEosMemberIndex": fcEosMemberIndex,
       "fcEosMemberType": fcEosMemberType,
       "fcEosMemberWWN": fcEosMemberWWN,
       "fcEosMemberDomainID": fcEosMemberDomainID,
       "fcEosMemberPortNumber": fcEosMemberPortNumber,
       "fcEosTA": fcEosTA,
       "fcEosTATable": fcEosTATable,
       "fcEosTAEntry": fcEosTAEntry,
       "fcEosTAIndex": fcEosTAIndex,
       "fcEosTAName": fcEosTAName,
       "fcEosTAState": fcEosTAState,
       "fcEosTAType": fcEosTAType,
       "fcEosTAPortType": fcEosTAPortType,
       "fcEosTAPortList": fcEosTAPortList,
       "fcEosTAInterval": fcEosTAInterval,
       "fcEosTATriggerValue": fcEosTATriggerValue,
       "fcEosTTADirection": fcEosTTADirection,
       "fcEosTTATriggerDuration": fcEosTTATriggerDuration,
       "fcEosCTACounter": fcEosCTACounter}
)
