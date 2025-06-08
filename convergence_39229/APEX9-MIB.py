# SNMP MIB module (APEX9-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/convergence_39229/APEX9-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:23 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apex9 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39229)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Brand_ObjectIdentity = ObjectIdentity
brand = _Brand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1)
)
_Ll1000_ObjectIdentity = ObjectIdentity
ll1000 = _Ll1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2)
)
_SysFce_ObjectIdentity = ObjectIdentity
sysFce = _SysFce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1)
)
_SysFceBas_ObjectIdentity = ObjectIdentity
sysFceBas = _SysFceBas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1)
)
_SysFceBasDev_ObjectIdentity = ObjectIdentity
sysFceBasDev = _SysFceBasDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1)
)


class _SysFceBasDevName_Type(DisplayString):
    """Custom type sysFceBasDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 24),
    )


_SysFceBasDevName_Type.__name__ = "DisplayString"
_SysFceBasDevName_Object = MibScalar
sysFceBasDevName = _SysFceBasDevName_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 1),
    _SysFceBasDevName_Type()
)
sysFceBasDevName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevName.setStatus("current")


class _SysFceBasDevAddDesc1_Type(DisplayString):
    """Custom type sysFceBasDevAddDesc1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SysFceBasDevAddDesc1_Type.__name__ = "DisplayString"
_SysFceBasDevAddDesc1_Object = MibScalar
sysFceBasDevAddDesc1 = _SysFceBasDevAddDesc1_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 2),
    _SysFceBasDevAddDesc1_Type()
)
sysFceBasDevAddDesc1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevAddDesc1.setStatus("current")


class _SysFceBasDevAddDesc2_Type(DisplayString):
    """Custom type sysFceBasDevAddDesc2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SysFceBasDevAddDesc2_Type.__name__ = "DisplayString"
_SysFceBasDevAddDesc2_Object = MibScalar
sysFceBasDevAddDesc2 = _SysFceBasDevAddDesc2_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 3),
    _SysFceBasDevAddDesc2_Type()
)
sysFceBasDevAddDesc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevAddDesc2.setStatus("current")


class _SysFceBasDevAddDesc3_Type(DisplayString):
    """Custom type sysFceBasDevAddDesc3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SysFceBasDevAddDesc3_Type.__name__ = "DisplayString"
_SysFceBasDevAddDesc3_Object = MibScalar
sysFceBasDevAddDesc3 = _SysFceBasDevAddDesc3_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 4),
    _SysFceBasDevAddDesc3_Type()
)
sysFceBasDevAddDesc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevAddDesc3.setStatus("current")


class _SysFceBasDevAddDesc4_Type(DisplayString):
    """Custom type sysFceBasDevAddDesc4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SysFceBasDevAddDesc4_Type.__name__ = "DisplayString"
_SysFceBasDevAddDesc4_Object = MibScalar
sysFceBasDevAddDesc4 = _SysFceBasDevAddDesc4_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 5),
    _SysFceBasDevAddDesc4_Type()
)
sysFceBasDevAddDesc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevAddDesc4.setStatus("current")


class _SysFceBasDevAddDesc5_Type(DisplayString):
    """Custom type sysFceBasDevAddDesc5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SysFceBasDevAddDesc5_Type.__name__ = "DisplayString"
_SysFceBasDevAddDesc5_Object = MibScalar
sysFceBasDevAddDesc5 = _SysFceBasDevAddDesc5_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 6),
    _SysFceBasDevAddDesc5_Type()
)
sysFceBasDevAddDesc5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevAddDesc5.setStatus("current")


class _SysFceBasDevDate_Type(DisplayString):
    """Custom type sysFceBasDevDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_SysFceBasDevDate_Type.__name__ = "DisplayString"
_SysFceBasDevDate_Object = MibScalar
sysFceBasDevDate = _SysFceBasDevDate_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 7),
    _SysFceBasDevDate_Type()
)
sysFceBasDevDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevDate.setStatus("current")


class _SysFceBasDevTime_Type(DisplayString):
    """Custom type sysFceBasDevTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SysFceBasDevTime_Type.__name__ = "DisplayString"
_SysFceBasDevTime_Object = MibScalar
sysFceBasDevTime = _SysFceBasDevTime_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 8),
    _SysFceBasDevTime_Type()
)
sysFceBasDevTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasDevTime.setStatus("current")


class _SysFceBasDevIduProNum_Type(DisplayString):
    """Custom type sysFceBasDevIduProNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduProNum_Type.__name__ = "DisplayString"
_SysFceBasDevIduProNum_Object = MibScalar
sysFceBasDevIduProNum = _SysFceBasDevIduProNum_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 9),
    _SysFceBasDevIduProNum_Type()
)
sysFceBasDevIduProNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduProNum.setStatus("current")


class _SysFceBasDevIduSerNum_Type(DisplayString):
    """Custom type sysFceBasDevIduSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduSerNum_Type.__name__ = "DisplayString"
_SysFceBasDevIduSerNum_Object = MibScalar
sysFceBasDevIduSerNum = _SysFceBasDevIduSerNum_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 10),
    _SysFceBasDevIduSerNum_Type()
)
sysFceBasDevIduSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduSerNum.setStatus("current")


class _SysFceBasDevOduProNum_Type(DisplayString):
    """Custom type sysFceBasDevOduProNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevOduProNum_Type.__name__ = "DisplayString"
_SysFceBasDevOduProNum_Object = MibScalar
sysFceBasDevOduProNum = _SysFceBasDevOduProNum_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 11),
    _SysFceBasDevOduProNum_Type()
)
sysFceBasDevOduProNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevOduProNum.setStatus("current")


class _SysFceBasDevOduSerNum_Type(DisplayString):
    """Custom type sysFceBasDevOduSerNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevOduSerNum_Type.__name__ = "DisplayString"
_SysFceBasDevOduSerNum_Object = MibScalar
sysFceBasDevOduSerNum = _SysFceBasDevOduSerNum_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 12),
    _SysFceBasDevOduSerNum_Type()
)
sysFceBasDevOduSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevOduSerNum.setStatus("current")


class _SysFceBasDevIduHwBase_Type(DisplayString):
    """Custom type sysFceBasDevIduHwBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduHwBase_Type.__name__ = "DisplayString"
_SysFceBasDevIduHwBase_Object = MibScalar
sysFceBasDevIduHwBase = _SysFceBasDevIduHwBase_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 13),
    _SysFceBasDevIduHwBase_Type()
)
sysFceBasDevIduHwBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduHwBase.setStatus("current")


class _SysFceBasDevIduFwBase_Type(DisplayString):
    """Custom type sysFceBasDevIduFwBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduFwBase_Type.__name__ = "DisplayString"
_SysFceBasDevIduFwBase_Object = MibScalar
sysFceBasDevIduFwBase = _SysFceBasDevIduFwBase_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 14),
    _SysFceBasDevIduFwBase_Type()
)
sysFceBasDevIduFwBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduFwBase.setStatus("current")


class _SysFceBasDevIduOsKern_Type(DisplayString):
    """Custom type sysFceBasDevIduOsKern based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduOsKern_Type.__name__ = "DisplayString"
_SysFceBasDevIduOsKern_Object = MibScalar
sysFceBasDevIduOsKern = _SysFceBasDevIduOsKern_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 15),
    _SysFceBasDevIduOsKern_Type()
)
sysFceBasDevIduOsKern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduOsKern.setStatus("current")


class _SysFceBasDevIduOsDev_Type(DisplayString):
    """Custom type sysFceBasDevIduOsDev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevIduOsDev_Type.__name__ = "DisplayString"
_SysFceBasDevIduOsDev_Object = MibScalar
sysFceBasDevIduOsDev = _SysFceBasDevIduOsDev_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 16),
    _SysFceBasDevIduOsDev_Type()
)
sysFceBasDevIduOsDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevIduOsDev.setStatus("current")


class _SysFceBasDevOduSwVer_Type(DisplayString):
    """Custom type sysFceBasDevOduSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevOduSwVer_Type.__name__ = "DisplayString"
_SysFceBasDevOduSwVer_Object = MibScalar
sysFceBasDevOduSwVer = _SysFceBasDevOduSwVer_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 17),
    _SysFceBasDevOduSwVer_Type()
)
sysFceBasDevOduSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevOduSwVer.setStatus("current")


class _SysFceBasDevCpuMac_Type(DisplayString):
    """Custom type sysFceBasDevCpuMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevCpuMac_Type.__name__ = "DisplayString"
_SysFceBasDevCpuMac_Object = MibScalar
sysFceBasDevCpuMac = _SysFceBasDevCpuMac_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 18),
    _SysFceBasDevCpuMac_Type()
)
sysFceBasDevCpuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevCpuMac.setStatus("current")


class _SysFceBasDevSysStat_Type(Integer32):
    """Custom type sysFceBasDevSysStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("warning", 1),
          ("error", 2))
    )


_SysFceBasDevSysStat_Type.__name__ = "Integer32"
_SysFceBasDevSysStat_Object = MibScalar
sysFceBasDevSysStat = _SysFceBasDevSysStat_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 19),
    _SysFceBasDevSysStat_Type()
)
sysFceBasDevSysStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevSysStat.setStatus("current")


class _SysFceBasDevDesc1_Type(DisplayString):
    """Custom type sysFceBasDevDesc1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevDesc1_Type.__name__ = "DisplayString"
_SysFceBasDevDesc1_Object = MibScalar
sysFceBasDevDesc1 = _SysFceBasDevDesc1_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 20),
    _SysFceBasDevDesc1_Type()
)
sysFceBasDevDesc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevDesc1.setStatus("current")


class _SysFceBasDevDesc2_Type(DisplayString):
    """Custom type sysFceBasDevDesc2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevDesc2_Type.__name__ = "DisplayString"
_SysFceBasDevDesc2_Object = MibScalar
sysFceBasDevDesc2 = _SysFceBasDevDesc2_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 21),
    _SysFceBasDevDesc2_Type()
)
sysFceBasDevDesc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevDesc2.setStatus("current")


class _SysFceBasDevAddInfo_Type(DisplayString):
    """Custom type sysFceBasDevAddInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysFceBasDevAddInfo_Type.__name__ = "DisplayString"
_SysFceBasDevAddInfo_Object = MibScalar
sysFceBasDevAddInfo = _SysFceBasDevAddInfo_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 1, 22),
    _SysFceBasDevAddInfo_Type()
)
sysFceBasDevAddInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFceBasDevAddInfo.setStatus("current")
_SysFceBasCmd_ObjectIdentity = ObjectIdentity
sysFceBasCmd = _SysFceBasCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2)
)


class _SysFceBasCmdEn_Type(Integer32):
    """Custom type sysFceBasCmdEn based on Integer32"""
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
        *(("readonly", 0),
          ("writeAccessSNMP", 1),
          ("writeAccessCMD", 2),
          ("writeAccessWEB", 3))
    )


_SysFceBasCmdEn_Type.__name__ = "Integer32"
_SysFceBasCmdEn_Object = MibScalar
sysFceBasCmdEn = _SysFceBasCmdEn_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 1),
    _SysFceBasCmdEn_Type()
)
sysFceBasCmdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdEn.setStatus("current")


class _SysFceBasCmdWr_Type(Integer32):
    """Custom type sysFceBasCmdWr based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("w1", 1),
          ("w2", 2),
          ("w3", 3),
          ("startup", 4))
    )


_SysFceBasCmdWr_Type.__name__ = "Integer32"
_SysFceBasCmdWr_Object = MibScalar
sysFceBasCmdWr = _SysFceBasCmdWr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 2),
    _SysFceBasCmdWr_Type()
)
sysFceBasCmdWr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdWr.setStatus("current")


class _SysFceBasCmdRn_Type(Integer32):
    """Custom type sysFceBasCmdRn based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("r1", 1),
          ("r2", 2),
          ("r3", 3),
          ("startup", 4))
    )


_SysFceBasCmdRn_Type.__name__ = "Integer32"
_SysFceBasCmdRn_Object = MibScalar
sysFceBasCmdRn = _SysFceBasCmdRn_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 3),
    _SysFceBasCmdRn_Type()
)
sysFceBasCmdRn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdRn.setStatus("current")


class _SysFceBasCmdDsg_Type(Integer32):
    """Custom type sysFceBasCmdDsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 0),
          ("wide", 1))
    )


_SysFceBasCmdDsg_Type.__name__ = "Integer32"
_SysFceBasCmdDsg_Object = MibScalar
sysFceBasCmdDsg = _SysFceBasCmdDsg_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 4),
    _SysFceBasCmdDsg_Type()
)
sysFceBasCmdDsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdDsg.setStatus("current")


class _SysFceBasCmdRem_Type(Integer32):
    """Custom type sysFceBasCmdRem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("localANDremote", 1))
    )


_SysFceBasCmdRem_Type.__name__ = "Integer32"
_SysFceBasCmdRem_Object = MibScalar
sysFceBasCmdRem = _SysFceBasCmdRem_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 5),
    _SysFceBasCmdRem_Type()
)
sysFceBasCmdRem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdRem.setStatus("current")


class _SysFceBasCmdAuto_Type(Integer32):
    """Custom type sysFceBasCmdAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SysFceBasCmdAuto_Type.__name__ = "Integer32"
_SysFceBasCmdAuto_Object = MibScalar
sysFceBasCmdAuto = _SysFceBasCmdAuto_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 6),
    _SysFceBasCmdAuto_Type()
)
sysFceBasCmdAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdAuto.setStatus("current")


class _SysFceBasCmdAlm_Type(Integer32):
    """Custom type sysFceBasCmdAlm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("validate", 1),
          ("clear", 2))
    )


_SysFceBasCmdAlm_Type.__name__ = "Integer32"
_SysFceBasCmdAlm_Object = MibScalar
sysFceBasCmdAlm = _SysFceBasCmdAlm_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 7),
    _SysFceBasCmdAlm_Type()
)
sysFceBasCmdAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdAlm.setStatus("current")


class _SysFceBasCmdClr_Type(Integer32):
    """Custom type sysFceBasCmdClr based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("all", 1),
          ("rfi", 2),
          ("lan", 3),
          ("ber", 4))
    )


_SysFceBasCmdClr_Type.__name__ = "Integer32"
_SysFceBasCmdClr_Object = MibScalar
sysFceBasCmdClr = _SysFceBasCmdClr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 8),
    _SysFceBasCmdClr_Type()
)
sysFceBasCmdClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdClr.setStatus("current")


class _SysFceBasCmdRst_Type(Integer32):
    """Custom type sysFceBasCmdRst based on Integer32"""
    defaultValue = 0

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
          ("reboot", 1),
          ("ip", 2),
          ("odu", 3))
    )


_SysFceBasCmdRst_Type.__name__ = "Integer32"
_SysFceBasCmdRst_Object = MibScalar
sysFceBasCmdRst = _SysFceBasCmdRst_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 1, 1, 2, 9),
    _SysFceBasCmdRst_Type()
)
sysFceBasCmdRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFceBasCmdRst.setStatus("current")
_CnfFce_ObjectIdentity = ObjectIdentity
cnfFce = _CnfFce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2)
)
_CnfFceMng_ObjectIdentity = ObjectIdentity
cnfFceMng = _CnfFceMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1)
)
_CnfFceMngIp_ObjectIdentity = ObjectIdentity
cnfFceMngIp = _CnfFceMngIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1)
)


class _CnfFceMngIpEthAddr_Type(IpAddress):
    """Custom type cnfFceMngIpEthAddr based on IpAddress"""
    defaultHexValue = "c0a8025a"


_CnfFceMngIpEthAddr_Type.__name__ = "IpAddress"
_CnfFceMngIpEthAddr_Object = MibScalar
cnfFceMngIpEthAddr = _CnfFceMngIpEthAddr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 1),
    _CnfFceMngIpEthAddr_Type()
)
cnfFceMngIpEthAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpEthAddr.setStatus("current")


class _CnfFceMngIpEthMask_Type(IpAddress):
    """Custom type cnfFceMngIpEthMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_CnfFceMngIpEthMask_Type.__name__ = "IpAddress"
_CnfFceMngIpEthMask_Object = MibScalar
cnfFceMngIpEthMask = _CnfFceMngIpEthMask_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 2),
    _CnfFceMngIpEthMask_Type()
)
cnfFceMngIpEthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpEthMask.setStatus("current")


class _CnfFceMngIpRemote_Type(IpAddress):
    """Custom type cnfFceMngIpRemote based on IpAddress"""
    defaultHexValue = "c0a8025b"


_CnfFceMngIpRemote_Type.__name__ = "IpAddress"
_CnfFceMngIpRemote_Object = MibScalar
cnfFceMngIpRemote = _CnfFceMngIpRemote_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 3),
    _CnfFceMngIpRemote_Type()
)
cnfFceMngIpRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpRemote.setStatus("current")


class _CnfFceMngIpGtwAddr_Type(IpAddress):
    """Custom type cnfFceMngIpGtwAddr based on IpAddress"""
    defaultHexValue = "c0a80201"


_CnfFceMngIpGtwAddr_Type.__name__ = "IpAddress"
_CnfFceMngIpGtwAddr_Object = MibScalar
cnfFceMngIpGtwAddr = _CnfFceMngIpGtwAddr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 4),
    _CnfFceMngIpGtwAddr_Type()
)
cnfFceMngIpGtwAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpGtwAddr.setStatus("current")


class _CnfFceMngIpFtpUsb_Type(DisplayString):
    """Custom type cnfFceMngIpFtpUsb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_CnfFceMngIpFtpUsb_Type.__name__ = "DisplayString"
_CnfFceMngIpFtpUsb_Object = MibScalar
cnfFceMngIpFtpUsb = _CnfFceMngIpFtpUsb_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 5),
    _CnfFceMngIpFtpUsb_Type()
)
cnfFceMngIpFtpUsb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpFtpUsb.setStatus("current")


class _CnfFceMngIpSecEthaddr_Type(IpAddress):
    """Custom type cnfFceMngIpSecEthaddr based on IpAddress"""
    defaultHexValue = "0a0a0a0a"


_CnfFceMngIpSecEthaddr_Type.__name__ = "IpAddress"
_CnfFceMngIpSecEthaddr_Object = MibScalar
cnfFceMngIpSecEthaddr = _CnfFceMngIpSecEthaddr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 6),
    _CnfFceMngIpSecEthaddr_Type()
)
cnfFceMngIpSecEthaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpSecEthaddr.setStatus("current")


class _CnfFceMngIpSecEthMask_Type(IpAddress):
    """Custom type cnfFceMngIpSecEthMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_CnfFceMngIpSecEthMask_Type.__name__ = "IpAddress"
_CnfFceMngIpSecEthMask_Object = MibScalar
cnfFceMngIpSecEthMask = _CnfFceMngIpSecEthMask_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 7),
    _CnfFceMngIpSecEthMask_Type()
)
cnfFceMngIpSecEthMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpSecEthMask.setStatus("current")


class _CnfFceMngIpSecProxyArp_Type(Integer32):
    """Custom type cnfFceMngIpSecProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceMngIpSecProxyArp_Type.__name__ = "Integer32"
_CnfFceMngIpSecProxyArp_Object = MibScalar
cnfFceMngIpSecProxyArp = _CnfFceMngIpSecProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 1, 8),
    _CnfFceMngIpSecProxyArp_Type()
)
cnfFceMngIpSecProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngIpSecProxyArp.setStatus("current")
_CnfFceMngSnmp_ObjectIdentity = ObjectIdentity
cnfFceMngSnmp = _CnfFceMngSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2)
)


class _CnfFceMngSnmpRstring_Type(DisplayString):
    """Custom type cnfFceMngSnmpRstring based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceMngSnmpRstring_Type.__name__ = "DisplayString"
_CnfFceMngSnmpRstring_Object = MibScalar
cnfFceMngSnmpRstring = _CnfFceMngSnmpRstring_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 1),
    _CnfFceMngSnmpRstring_Type()
)
cnfFceMngSnmpRstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpRstring.setStatus("current")


class _CnfFceMngSnmpWstring_Type(DisplayString):
    """Custom type cnfFceMngSnmpWstring based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceMngSnmpWstring_Type.__name__ = "DisplayString"
_CnfFceMngSnmpWstring_Object = MibScalar
cnfFceMngSnmpWstring = _CnfFceMngSnmpWstring_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 2),
    _CnfFceMngSnmpWstring_Type()
)
cnfFceMngSnmpWstring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpWstring.setStatus("current")


class _CnfFceMngSnmpDport_Type(Unsigned32):
    """Custom type cnfFceMngSnmpDport based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnfFceMngSnmpDport_Type.__name__ = "Unsigned32"
_CnfFceMngSnmpDport_Object = MibScalar
cnfFceMngSnmpDport = _CnfFceMngSnmpDport_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 3),
    _CnfFceMngSnmpDport_Type()
)
cnfFceMngSnmpDport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpDport.setStatus("current")


class _CnfFceMngSnmpTport_Type(Unsigned32):
    """Custom type cnfFceMngSnmpTport based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnfFceMngSnmpTport_Type.__name__ = "Unsigned32"
_CnfFceMngSnmpTport_Object = MibScalar
cnfFceMngSnmpTport = _CnfFceMngSnmpTport_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 4),
    _CnfFceMngSnmpTport_Type()
)
cnfFceMngSnmpTport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpTport.setStatus("current")
_CnfFceMngSnmpTrap1Ip_Type = IpAddress
_CnfFceMngSnmpTrap1Ip_Object = MibScalar
cnfFceMngSnmpTrap1Ip = _CnfFceMngSnmpTrap1Ip_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 5),
    _CnfFceMngSnmpTrap1Ip_Type()
)
cnfFceMngSnmpTrap1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpTrap1Ip.setStatus("current")
_CnfFceMngSnmpTrap2Ip_Type = IpAddress
_CnfFceMngSnmpTrap2Ip_Object = MibScalar
cnfFceMngSnmpTrap2Ip = _CnfFceMngSnmpTrap2Ip_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 6),
    _CnfFceMngSnmpTrap2Ip_Type()
)
cnfFceMngSnmpTrap2Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpTrap2Ip.setStatus("current")
_CnfFceMngSnmpTrap3Ip_Type = IpAddress
_CnfFceMngSnmpTrap3Ip_Object = MibScalar
cnfFceMngSnmpTrap3Ip = _CnfFceMngSnmpTrap3Ip_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 1, 2, 7),
    _CnfFceMngSnmpTrap3Ip_Type()
)
cnfFceMngSnmpTrap3Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceMngSnmpTrap3Ip.setStatus("current")
_CnfFceDat_ObjectIdentity = ObjectIdentity
cnfFceDat = _CnfFceDat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2)
)
_CnfFceDatTdm_ObjectIdentity = ObjectIdentity
cnfFceDatTdm = _CnfFceDatTdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1)
)


class _CnfFceDatTdmE3Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE3Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE3Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE3Ena_Object = MibScalar
cnfFceDatTdmE3Ena = _CnfFceDatTdmE3Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 1),
    _CnfFceDatTdmE3Ena_Type()
)
cnfFceDatTdmE3Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE3Ena.setStatus("current")


class _CnfFceDatTdmE3Frm_Type(Integer32):
    """Custom type cnfFceDatTdmE3Frm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE3Frm_Type.__name__ = "Integer32"
_CnfFceDatTdmE3Frm_Object = MibScalar
cnfFceDatTdmE3Frm = _CnfFceDatTdmE3Frm_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 2),
    _CnfFceDatTdmE3Frm_Type()
)
cnfFceDatTdmE3Frm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE3Frm.setStatus("current")


class _CnfFceDatTdmE3Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE3Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE3Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE3Loop_Object = MibScalar
cnfFceDatTdmE3Loop = _CnfFceDatTdmE3Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 3),
    _CnfFceDatTdmE3Loop_Type()
)
cnfFceDatTdmE3Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE3Loop.setStatus("current")


class _CnfFceDatTdmE21Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE21Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("through", 0),
          ("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE21Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE21Mod_Object = MibScalar
cnfFceDatTdmE21Mod = _CnfFceDatTdmE21Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 4),
    _CnfFceDatTdmE21Mod_Type()
)
cnfFceDatTdmE21Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE21Mod.setStatus("current")


class _CnfFceDatTdmE22Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE22Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE22Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE22Ena_Object = MibScalar
cnfFceDatTdmE22Ena = _CnfFceDatTdmE22Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 5),
    _CnfFceDatTdmE22Ena_Type()
)
cnfFceDatTdmE22Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE22Ena.setStatus("current")


class _CnfFceDatTdmE22Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE22Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE22Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE22Loop_Object = MibScalar
cnfFceDatTdmE22Loop = _CnfFceDatTdmE22Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 6),
    _CnfFceDatTdmE22Loop_Type()
)
cnfFceDatTdmE22Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE22Loop.setStatus("current")


class _CnfFceDatTdmE22Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE22Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("through", 0),
          ("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE22Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE22Mod_Object = MibScalar
cnfFceDatTdmE22Mod = _CnfFceDatTdmE22Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 7),
    _CnfFceDatTdmE22Mod_Type()
)
cnfFceDatTdmE22Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE22Mod.setStatus("current")


class _CnfFceDatTdmE23Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE23Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE23Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE23Ena_Object = MibScalar
cnfFceDatTdmE23Ena = _CnfFceDatTdmE23Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 8),
    _CnfFceDatTdmE23Ena_Type()
)
cnfFceDatTdmE23Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE23Ena.setStatus("current")


class _CnfFceDatTdmE23Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE23Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE23Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE23Loop_Object = MibScalar
cnfFceDatTdmE23Loop = _CnfFceDatTdmE23Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 9),
    _CnfFceDatTdmE23Loop_Type()
)
cnfFceDatTdmE23Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE23Loop.setStatus("current")


class _CnfFceDatTdmE23Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE23Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("through", 0),
          ("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE23Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE23Mod_Object = MibScalar
cnfFceDatTdmE23Mod = _CnfFceDatTdmE23Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 10),
    _CnfFceDatTdmE23Mod_Type()
)
cnfFceDatTdmE23Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE23Mod.setStatus("current")


class _CnfFceDatTdmE24Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE24Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE24Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE24Ena_Object = MibScalar
cnfFceDatTdmE24Ena = _CnfFceDatTdmE24Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 11),
    _CnfFceDatTdmE24Ena_Type()
)
cnfFceDatTdmE24Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE24Ena.setStatus("current")


class _CnfFceDatTdmE24Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE24Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE24Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE24Loop_Object = MibScalar
cnfFceDatTdmE24Loop = _CnfFceDatTdmE24Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 12),
    _CnfFceDatTdmE24Loop_Type()
)
cnfFceDatTdmE24Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE24Loop.setStatus("current")


class _CnfFceDatTdmE24Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE24Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("through", 0),
          ("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE24Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE24Mod_Object = MibScalar
cnfFceDatTdmE24Mod = _CnfFceDatTdmE24Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 13),
    _CnfFceDatTdmE24Mod_Type()
)
cnfFceDatTdmE24Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE24Mod.setStatus("current")


class _CnfFceDatTdmE11Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE11Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE11Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE11Ena_Object = MibScalar
cnfFceDatTdmE11Ena = _CnfFceDatTdmE11Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 14),
    _CnfFceDatTdmE11Ena_Type()
)
cnfFceDatTdmE11Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE11Ena.setStatus("current")


class _CnfFceDatTdmE11Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE11Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE11Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE11Loop_Object = MibScalar
cnfFceDatTdmE11Loop = _CnfFceDatTdmE11Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 15),
    _CnfFceDatTdmE11Loop_Type()
)
cnfFceDatTdmE11Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE11Loop.setStatus("current")


class _CnfFceDatTdmE11Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE11Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE11Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE11Mod_Object = MibScalar
cnfFceDatTdmE11Mod = _CnfFceDatTdmE11Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 16),
    _CnfFceDatTdmE11Mod_Type()
)
cnfFceDatTdmE11Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE11Mod.setStatus("current")


class _CnfFceDatTdmE12Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE12Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE12Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE12Ena_Object = MibScalar
cnfFceDatTdmE12Ena = _CnfFceDatTdmE12Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 17),
    _CnfFceDatTdmE12Ena_Type()
)
cnfFceDatTdmE12Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE12Ena.setStatus("current")


class _CnfFceDatTdmE12Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE12Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE12Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE12Loop_Object = MibScalar
cnfFceDatTdmE12Loop = _CnfFceDatTdmE12Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 18),
    _CnfFceDatTdmE12Loop_Type()
)
cnfFceDatTdmE12Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE12Loop.setStatus("current")


class _CnfFceDatTdmE12Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE12Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE12Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE12Mod_Object = MibScalar
cnfFceDatTdmE12Mod = _CnfFceDatTdmE12Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 19),
    _CnfFceDatTdmE12Mod_Type()
)
cnfFceDatTdmE12Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE12Mod.setStatus("current")


class _CnfFceDatTdmE13Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE13Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE13Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE13Ena_Object = MibScalar
cnfFceDatTdmE13Ena = _CnfFceDatTdmE13Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 20),
    _CnfFceDatTdmE13Ena_Type()
)
cnfFceDatTdmE13Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE13Ena.setStatus("current")


class _CnfFceDatTdmE13Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE13Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE13Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE13Loop_Object = MibScalar
cnfFceDatTdmE13Loop = _CnfFceDatTdmE13Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 21),
    _CnfFceDatTdmE13Loop_Type()
)
cnfFceDatTdmE13Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE13Loop.setStatus("current")


class _CnfFceDatTdmE13Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE13Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE13Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE13Mod_Object = MibScalar
cnfFceDatTdmE13Mod = _CnfFceDatTdmE13Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 22),
    _CnfFceDatTdmE13Mod_Type()
)
cnfFceDatTdmE13Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE13Mod.setStatus("current")


class _CnfFceDatTdmE14Ena_Type(Integer32):
    """Custom type cnfFceDatTdmE14Ena based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE14Ena_Type.__name__ = "Integer32"
_CnfFceDatTdmE14Ena_Object = MibScalar
cnfFceDatTdmE14Ena = _CnfFceDatTdmE14Ena_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 23),
    _CnfFceDatTdmE14Ena_Type()
)
cnfFceDatTdmE14Ena.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE14Ena.setStatus("current")


class _CnfFceDatTdmE14Loop_Type(Integer32):
    """Custom type cnfFceDatTdmE14Loop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatTdmE14Loop_Type.__name__ = "Integer32"
_CnfFceDatTdmE14Loop_Object = MibScalar
cnfFceDatTdmE14Loop = _CnfFceDatTdmE14Loop_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 24),
    _CnfFceDatTdmE14Loop_Type()
)
cnfFceDatTdmE14Loop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE14Loop.setStatus("current")


class _CnfFceDatTdmE14Mod_Type(Integer32):
    """Custom type cnfFceDatTdmE14Mod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfi", 1),
          ("ber", 2))
    )


_CnfFceDatTdmE14Mod_Type.__name__ = "Integer32"
_CnfFceDatTdmE14Mod_Object = MibScalar
cnfFceDatTdmE14Mod = _CnfFceDatTdmE14Mod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 1, 25),
    _CnfFceDatTdmE14Mod_Type()
)
cnfFceDatTdmE14Mod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatTdmE14Mod.setStatus("current")
_CnfFceDatEth_ObjectIdentity = ObjectIdentity
cnfFceDatEth = _CnfFceDatEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2)
)


class _CnfFceDatEthLanAb_Type(Integer32):
    """Custom type cnfFceDatEthLanAb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatEthLanAb_Type.__name__ = "Integer32"
_CnfFceDatEthLanAb_Object = MibScalar
cnfFceDatEthLanAb = _CnfFceDatEthLanAb_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 1),
    _CnfFceDatEthLanAb_Type()
)
cnfFceDatEthLanAb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthLanAb.setStatus("current")


class _CnfFceDatEthSpeed_Type(Unsigned32):
    """Custom type cnfFceDatEthSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_CnfFceDatEthSpeed_Type.__name__ = "Unsigned32"
_CnfFceDatEthSpeed_Object = MibScalar
cnfFceDatEthSpeed = _CnfFceDatEthSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 2),
    _CnfFceDatEthSpeed_Type()
)
cnfFceDatEthSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthSpeed.setStatus("current")


class _CnfFceDatEthA1Aneg_Type(Integer32):
    """Custom type cnfFceDatEthA1Aneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatEthA1Aneg_Type.__name__ = "Integer32"
_CnfFceDatEthA1Aneg_Object = MibScalar
cnfFceDatEthA1Aneg = _CnfFceDatEthA1Aneg_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 3),
    _CnfFceDatEthA1Aneg_Type()
)
cnfFceDatEthA1Aneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthA1Aneg.setStatus("current")


class _CnfFceDatEthA1Dupl_Type(Integer32):
    """Custom type cnfFceDatEthA1Dupl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_CnfFceDatEthA1Dupl_Type.__name__ = "Integer32"
_CnfFceDatEthA1Dupl_Object = MibScalar
cnfFceDatEthA1Dupl = _CnfFceDatEthA1Dupl_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 4),
    _CnfFceDatEthA1Dupl_Type()
)
cnfFceDatEthA1Dupl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthA1Dupl.setStatus("current")


class _CnfFceDatEthA1Speed_Type(Integer32):
    """Custom type cnfFceDatEthA1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("fasteth", 1),
          ("gbiteth", 2))
    )


_CnfFceDatEthA1Speed_Type.__name__ = "Integer32"
_CnfFceDatEthA1Speed_Object = MibScalar
cnfFceDatEthA1Speed = _CnfFceDatEthA1Speed_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 5),
    _CnfFceDatEthA1Speed_Type()
)
cnfFceDatEthA1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthA1Speed.setStatus("current")


class _CnfFceDatEthA1Mdix_Type(Integer32):
    """Custom type cnfFceDatEthA1Mdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mdi", 1),
          ("mdx", 2))
    )


_CnfFceDatEthA1Mdix_Type.__name__ = "Integer32"
_CnfFceDatEthA1Mdix_Object = MibScalar
cnfFceDatEthA1Mdix = _CnfFceDatEthA1Mdix_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 6),
    _CnfFceDatEthA1Mdix_Type()
)
cnfFceDatEthA1Mdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthA1Mdix.setStatus("current")


class _CnfFceDatEthB1Aneg_Type(Integer32):
    """Custom type cnfFceDatEthB1Aneg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceDatEthB1Aneg_Type.__name__ = "Integer32"
_CnfFceDatEthB1Aneg_Object = MibScalar
cnfFceDatEthB1Aneg = _CnfFceDatEthB1Aneg_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 7),
    _CnfFceDatEthB1Aneg_Type()
)
cnfFceDatEthB1Aneg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthB1Aneg.setStatus("current")


class _CnfFceDatEthB1Dupl_Type(Integer32):
    """Custom type cnfFceDatEthB1Dupl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("half", 0),
          ("full", 1))
    )


_CnfFceDatEthB1Dupl_Type.__name__ = "Integer32"
_CnfFceDatEthB1Dupl_Object = MibScalar
cnfFceDatEthB1Dupl = _CnfFceDatEthB1Dupl_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 8),
    _CnfFceDatEthB1Dupl_Type()
)
cnfFceDatEthB1Dupl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthB1Dupl.setStatus("current")


class _CnfFceDatEthB1Speed_Type(Integer32):
    """Custom type cnfFceDatEthB1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("eth", 0),
          ("fastEth", 1))
    )


_CnfFceDatEthB1Speed_Type.__name__ = "Integer32"
_CnfFceDatEthB1Speed_Object = MibScalar
cnfFceDatEthB1Speed = _CnfFceDatEthB1Speed_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 9),
    _CnfFceDatEthB1Speed_Type()
)
cnfFceDatEthB1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthB1Speed.setStatus("current")


class _CnfFceDatEthB1Mdix_Type(Integer32):
    """Custom type cnfFceDatEthB1Mdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mdi", 1),
          ("mdx", 2))
    )


_CnfFceDatEthB1Mdix_Type.__name__ = "Integer32"
_CnfFceDatEthB1Mdix_Object = MibScalar
cnfFceDatEthB1Mdix = _CnfFceDatEthB1Mdix_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 2, 10),
    _CnfFceDatEthB1Mdix_Type()
)
cnfFceDatEthB1Mdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatEthB1Mdix.setStatus("current")
_CnfFceDatBer_ObjectIdentity = ObjectIdentity
cnfFceDatBer = _CnfFceDatBer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 3)
)


class _CnfFceDatBerSpeed_Type(Unsigned32):
    """Custom type cnfFceDatBerSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnfFceDatBerSpeed_Type.__name__ = "Unsigned32"
_CnfFceDatBerSpeed_Object = MibScalar
cnfFceDatBerSpeed = _CnfFceDatBerSpeed_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 3, 1),
    _CnfFceDatBerSpeed_Type()
)
cnfFceDatBerSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatBerSpeed.setStatus("current")


class _CnfFceDatBerInerr_Type(Integer32):
    """Custom type cnfFceDatBerInerr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("insert", 1))
    )


_CnfFceDatBerInerr_Type.__name__ = "Integer32"
_CnfFceDatBerInerr_Object = MibScalar
cnfFceDatBerInerr = _CnfFceDatBerInerr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 2, 3, 2),
    _CnfFceDatBerInerr_Type()
)
cnfFceDatBerInerr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceDatBerInerr.setStatus("current")
_CnfFceRad_ObjectIdentity = ObjectIdentity
cnfFceRad = _CnfFceRad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3)
)
_CnfFceRadRf_ObjectIdentity = ObjectIdentity
cnfFceRadRf = _CnfFceRadRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1)
)


class _CnfFceRadRfTxPwr_Type(Integer32):
    """Custom type cnfFceRadRfTxPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 40),
    )


_CnfFceRadRfTxPwr_Type.__name__ = "Integer32"
_CnfFceRadRfTxPwr_Object = MibScalar
cnfFceRadRfTxPwr = _CnfFceRadRfTxPwr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1, 1),
    _CnfFceRadRfTxPwr_Type()
)
cnfFceRadRfTxPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadRfTxPwr.setStatus("current")
_CnfFceRadRfTxFreq_Type = Unsigned32
_CnfFceRadRfTxFreq_Object = MibScalar
cnfFceRadRfTxFreq = _CnfFceRadRfTxFreq_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1, 2),
    _CnfFceRadRfTxFreq_Type()
)
cnfFceRadRfTxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadRfTxFreq.setStatus("current")
_CnfFceRadRfRxFreq_Type = Unsigned32
_CnfFceRadRfRxFreq_Object = MibScalar
cnfFceRadRfRxFreq = _CnfFceRadRfRxFreq_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1, 3),
    _CnfFceRadRfRxFreq_Type()
)
cnfFceRadRfRxFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadRfRxFreq.setStatus("current")


class _CnfFceRadRfAtpcEna_Type(Integer32):
    """Custom type cnfFceRadRfAtpcEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CnfFceRadRfAtpcEna_Type.__name__ = "Integer32"
_CnfFceRadRfAtpcEna_Object = MibScalar
cnfFceRadRfAtpcEna = _CnfFceRadRfAtpcEna_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1, 4),
    _CnfFceRadRfAtpcEna_Type()
)
cnfFceRadRfAtpcEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadRfAtpcEna.setStatus("current")


class _CnfFceRadRfAtpcRxl_Type(Integer32):
    """Custom type cnfFceRadRfAtpcRxl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_CnfFceRadRfAtpcRxl_Type.__name__ = "Integer32"
_CnfFceRadRfAtpcRxl_Object = MibScalar
cnfFceRadRfAtpcRxl = _CnfFceRadRfAtpcRxl_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 1, 5),
    _CnfFceRadRfAtpcRxl_Type()
)
cnfFceRadRfAtpcRxl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadRfAtpcRxl.setStatus("current")
_CnfFceRadMod_ObjectIdentity = ObjectIdentity
cnfFceRadMod = _CnfFceRadMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2)
)


class _CnfFceRadModActMod_Type(DisplayString):
    """Custom type cnfFceRadModActMod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceRadModActMod_Type.__name__ = "DisplayString"
_CnfFceRadModActMod_Object = MibScalar
cnfFceRadModActMod = _CnfFceRadModActMod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 1),
    _CnfFceRadModActMod_Type()
)
cnfFceRadModActMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadModActMod.setStatus("current")


class _CnfFceRadModAcmEna_Type(Integer32):
    """Custom type cnfFceRadModAcmEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CnfFceRadModAcmEna_Type.__name__ = "Integer32"
_CnfFceRadModAcmEna_Object = MibScalar
cnfFceRadModAcmEna = _CnfFceRadModAcmEna_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 2),
    _CnfFceRadModAcmEna_Type()
)
cnfFceRadModAcmEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadModAcmEna.setStatus("current")


class _CnfFceRadModAcmMod0_Type(DisplayString):
    """Custom type cnfFceRadModAcmMod0 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceRadModAcmMod0_Type.__name__ = "DisplayString"
_CnfFceRadModAcmMod0_Object = MibScalar
cnfFceRadModAcmMod0 = _CnfFceRadModAcmMod0_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 3),
    _CnfFceRadModAcmMod0_Type()
)
cnfFceRadModAcmMod0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadModAcmMod0.setStatus("current")


class _CnfFceRadModAcmMod1_Type(DisplayString):
    """Custom type cnfFceRadModAcmMod1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceRadModAcmMod1_Type.__name__ = "DisplayString"
_CnfFceRadModAcmMod1_Object = MibScalar
cnfFceRadModAcmMod1 = _CnfFceRadModAcmMod1_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 4),
    _CnfFceRadModAcmMod1_Type()
)
cnfFceRadModAcmMod1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadModAcmMod1.setStatus("current")


class _CnfFceRadModAcmMod2_Type(DisplayString):
    """Custom type cnfFceRadModAcmMod2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceRadModAcmMod2_Type.__name__ = "DisplayString"
_CnfFceRadModAcmMod2_Object = MibScalar
cnfFceRadModAcmMod2 = _CnfFceRadModAcmMod2_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 5),
    _CnfFceRadModAcmMod2_Type()
)
cnfFceRadModAcmMod2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadModAcmMod2.setStatus("current")
_CnfFceRadModTable_Object = MibTable
cnfFceRadModTable = _CnfFceRadModTable_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    cnfFceRadModTable.setStatus("current")
_CnfFceRadModEntry_Object = MibTableRow
cnfFceRadModEntry = _CnfFceRadModEntry_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 6, 1)
)
cnfFceRadModEntry.setIndexNames(
    (0, "APEX9-MIB", "cnfFceRadModTableIndex"),
)
if mibBuilder.loadTexts:
    cnfFceRadModEntry.setStatus("current")


class _CnfFceRadModTableIndex_Type(Unsigned32):
    """Custom type cnfFceRadModTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnfFceRadModTableIndex_Type.__name__ = "Unsigned32"
_CnfFceRadModTableIndex_Object = MibTableColumn
cnfFceRadModTableIndex = _CnfFceRadModTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 6, 1, 1),
    _CnfFceRadModTableIndex_Type()
)
cnfFceRadModTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceRadModTableIndex.setStatus("current")


class _CnfFceRadModTableMod_Type(DisplayString):
    """Custom type cnfFceRadModTableMod based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceRadModTableMod_Type.__name__ = "DisplayString"
_CnfFceRadModTableMod_Object = MibTableColumn
cnfFceRadModTableMod = _CnfFceRadModTableMod_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 2, 6, 1, 2),
    _CnfFceRadModTableMod_Type()
)
cnfFceRadModTableMod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceRadModTableMod.setStatus("current")
_CnfFceRadOpt_ObjectIdentity = ObjectIdentity
cnfFceRadOpt = _CnfFceRadOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3)
)


class _CnfFceRadOptOduMute_Type(Integer32):
    """Custom type cnfFceRadOptOduMute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("mute", 1))
    )


_CnfFceRadOptOduMute_Type.__name__ = "Integer32"
_CnfFceRadOptOduMute_Object = MibScalar
cnfFceRadOptOduMute = _CnfFceRadOptOduMute_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 1),
    _CnfFceRadOptOduMute_Type()
)
cnfFceRadOptOduMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptOduMute.setStatus("current")


class _CnfFceRadOptOduMuteStat_Type(Integer32):
    """Custom type cnfFceRadOptOduMuteStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unmuted", 0),
          ("muted", 1))
    )


_CnfFceRadOptOduMuteStat_Type.__name__ = "Integer32"
_CnfFceRadOptOduMuteStat_Object = MibScalar
cnfFceRadOptOduMuteStat = _CnfFceRadOptOduMuteStat_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 2),
    _CnfFceRadOptOduMuteStat_Type()
)
cnfFceRadOptOduMuteStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceRadOptOduMuteStat.setStatus("current")


class _CnfFceRadOptPwrDown_Type(Integer32):
    """Custom type cnfFceRadOptPwrDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oduPWRup", 0),
          ("oduPWRdown", 1))
    )


_CnfFceRadOptPwrDown_Type.__name__ = "Integer32"
_CnfFceRadOptPwrDown_Object = MibScalar
cnfFceRadOptPwrDown = _CnfFceRadOptPwrDown_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 3),
    _CnfFceRadOptPwrDown_Type()
)
cnfFceRadOptPwrDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptPwrDown.setStatus("current")


class _CnfFceRadOptOduFlt_Type(Integer32):
    """Custom type cnfFceRadOptOduFlt based on Integer32"""
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
        *(("auto", 0),
          ("narrow", 1),
          ("wide", 2),
          ("notAvailable", 3))
    )


_CnfFceRadOptOduFlt_Type.__name__ = "Integer32"
_CnfFceRadOptOduFlt_Object = MibScalar
cnfFceRadOptOduFlt = _CnfFceRadOptOduFlt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 4),
    _CnfFceRadOptOduFlt_Type()
)
cnfFceRadOptOduFlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptOduFlt.setStatus("current")
_CnfFceRadOptOduFltStat_Type = DisplayString
_CnfFceRadOptOduFltStat_Object = MibScalar
cnfFceRadOptOduFltStat = _CnfFceRadOptOduFltStat_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 5),
    _CnfFceRadOptOduFltStat_Type()
)
cnfFceRadOptOduFltStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceRadOptOduFltStat.setStatus("current")


class _CnfFceRadOptOduSp_Type(Integer32):
    """Custom type cnfFceRadOptOduSp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("noinversion", 1),
          ("inversion", 2))
    )


_CnfFceRadOptOduSp_Type.__name__ = "Integer32"
_CnfFceRadOptOduSp_Object = MibScalar
cnfFceRadOptOduSp = _CnfFceRadOptOduSp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 6),
    _CnfFceRadOptOduSp_Type()
)
cnfFceRadOptOduSp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptOduSp.setStatus("current")


class _CnfFceRadOptSpStat_Type(Integer32):
    """Custom type cnfFceRadOptSpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noinversion", 0),
          ("inversion", 1))
    )


_CnfFceRadOptSpStat_Type.__name__ = "Integer32"
_CnfFceRadOptSpStat_Object = MibScalar
cnfFceRadOptSpStat = _CnfFceRadOptSpStat_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 7),
    _CnfFceRadOptSpStat_Type()
)
cnfFceRadOptSpStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceRadOptSpStat.setStatus("current")


class _CnfFceRadOptLat_Type(Integer32):
    """Custom type cnfFceRadOptLat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("low", 1))
    )


_CnfFceRadOptLat_Type.__name__ = "Integer32"
_CnfFceRadOptLat_Object = MibScalar
cnfFceRadOptLat = _CnfFceRadOptLat_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 8),
    _CnfFceRadOptLat_Type()
)
cnfFceRadOptLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptLat.setStatus("current")


class _CnfFceRadOptCw_Type(Integer32):
    """Custom type cnfFceRadOptCw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CnfFceRadOptCw_Type.__name__ = "Integer32"
_CnfFceRadOptCw_Object = MibScalar
cnfFceRadOptCw = _CnfFceRadOptCw_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 9),
    _CnfFceRadOptCw_Type()
)
cnfFceRadOptCw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptCw.setStatus("current")


class _CnfFceRadOptAgc_Type(Integer32):
    """Custom type cnfFceRadOptAgc based on Integer32"""
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
        *(("auto", 0),
          ("slow", 1),
          ("fast", 2),
          ("freeze", 3))
    )


_CnfFceRadOptAgc_Type.__name__ = "Integer32"
_CnfFceRadOptAgc_Object = MibScalar
cnfFceRadOptAgc = _CnfFceRadOptAgc_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 3, 3, 10),
    _CnfFceRadOptAgc_Type()
)
cnfFceRadOptAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceRadOptAgc.setStatus("current")
_CnfFceAlm_ObjectIdentity = ObjectIdentity
cnfFceAlm = _CnfFceAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4)
)
_CnfFceAlmPort_ObjectIdentity = ObjectIdentity
cnfFceAlmPort = _CnfFceAlmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1)
)


class _CnfFceAlmPortE11Link_Type(Integer32):
    """Custom type cnfFceAlmPortE11Link based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE11Link_Type.__name__ = "Integer32"
_CnfFceAlmPortE11Link_Object = MibScalar
cnfFceAlmPortE11Link = _CnfFceAlmPortE11Link_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 1),
    _CnfFceAlmPortE11Link_Type()
)
cnfFceAlmPortE11Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE11Link.setStatus("current")


class _CnfFceAlmPortE11Ais_Type(Integer32):
    """Custom type cnfFceAlmPortE11Ais based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE11Ais_Type.__name__ = "Integer32"
_CnfFceAlmPortE11Ais_Object = MibScalar
cnfFceAlmPortE11Ais = _CnfFceAlmPortE11Ais_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 2),
    _CnfFceAlmPortE11Ais_Type()
)
cnfFceAlmPortE11Ais.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE11Ais.setStatus("current")


class _CnfFceAlmPortE12Link_Type(Integer32):
    """Custom type cnfFceAlmPortE12Link based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE12Link_Type.__name__ = "Integer32"
_CnfFceAlmPortE12Link_Object = MibScalar
cnfFceAlmPortE12Link = _CnfFceAlmPortE12Link_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 3),
    _CnfFceAlmPortE12Link_Type()
)
cnfFceAlmPortE12Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE12Link.setStatus("current")


class _CnfFceAlmPortE12Ais_Type(Integer32):
    """Custom type cnfFceAlmPortE12Ais based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE12Ais_Type.__name__ = "Integer32"
_CnfFceAlmPortE12Ais_Object = MibScalar
cnfFceAlmPortE12Ais = _CnfFceAlmPortE12Ais_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 4),
    _CnfFceAlmPortE12Ais_Type()
)
cnfFceAlmPortE12Ais.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE12Ais.setStatus("current")


class _CnfFceAlmPortLanA1Link_Type(Integer32):
    """Custom type cnfFceAlmPortLanA1Link based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortLanA1Link_Type.__name__ = "Integer32"
_CnfFceAlmPortLanA1Link_Object = MibScalar
cnfFceAlmPortLanA1Link = _CnfFceAlmPortLanA1Link_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 5),
    _CnfFceAlmPortLanA1Link_Type()
)
cnfFceAlmPortLanA1Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortLanA1Link.setStatus("current")


class _CnfFceAlmPortLanB1Link_Type(Integer32):
    """Custom type cnfFceAlmPortLanB1Link based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortLanB1Link_Type.__name__ = "Integer32"
_CnfFceAlmPortLanB1Link_Object = MibScalar
cnfFceAlmPortLanB1Link = _CnfFceAlmPortLanB1Link_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 6),
    _CnfFceAlmPortLanB1Link_Type()
)
cnfFceAlmPortLanB1Link.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortLanB1Link.setStatus("current")


class _CnfFceAlmPortE3Los_Type(Integer32):
    """Custom type cnfFceAlmPortE3Los based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE3Los_Type.__name__ = "Integer32"
_CnfFceAlmPortE3Los_Object = MibScalar
cnfFceAlmPortE3Los = _CnfFceAlmPortE3Los_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 7),
    _CnfFceAlmPortE3Los_Type()
)
cnfFceAlmPortE3Los.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE3Los.setStatus("current")


class _CnfFceAlmPortE3Fer_Type(Integer32):
    """Custom type cnfFceAlmPortE3Fer based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmPortE3Fer_Type.__name__ = "Integer32"
_CnfFceAlmPortE3Fer_Object = MibScalar
cnfFceAlmPortE3Fer = _CnfFceAlmPortE3Fer_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 1, 8),
    _CnfFceAlmPortE3Fer_Type()
)
cnfFceAlmPortE3Fer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmPortE3Fer.setStatus("current")
_CnfFceAlmMux_ObjectIdentity = ObjectIdentity
cnfFceAlmMux = _CnfFceAlmMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 2)
)


class _CnfFceAlmMuxRfiLos_Type(Integer32):
    """Custom type cnfFceAlmMuxRfiLos based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmMuxRfiLos_Type.__name__ = "Integer32"
_CnfFceAlmMuxRfiLos_Object = MibScalar
cnfFceAlmMuxRfiLos = _CnfFceAlmMuxRfiLos_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 2, 1),
    _CnfFceAlmMuxRfiLos_Type()
)
cnfFceAlmMuxRfiLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmMuxRfiLos.setStatus("current")


class _CnfFceAlmMuxRfiFer_Type(Integer32):
    """Custom type cnfFceAlmMuxRfiFer based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmMuxRfiFer_Type.__name__ = "Integer32"
_CnfFceAlmMuxRfiFer_Object = MibScalar
cnfFceAlmMuxRfiFer = _CnfFceAlmMuxRfiFer_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 2, 2),
    _CnfFceAlmMuxRfiFer_Type()
)
cnfFceAlmMuxRfiFer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmMuxRfiFer.setStatus("current")


class _CnfFceAlmMuxRfiFerThr_Type(Unsigned32):
    """Custom type cnfFceAlmMuxRfiFerThr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_CnfFceAlmMuxRfiFerThr_Type.__name__ = "Unsigned32"
_CnfFceAlmMuxRfiFerThr_Object = MibScalar
cnfFceAlmMuxRfiFerThr = _CnfFceAlmMuxRfiFerThr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 2, 3),
    _CnfFceAlmMuxRfiFerThr_Type()
)
cnfFceAlmMuxRfiFerThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmMuxRfiFerThr.setStatus("current")
_CnfFceAlmMod_ObjectIdentity = ObjectIdentity
cnfFceAlmMod = _CnfFceAlmMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 3)
)


class _CnfFceAlmModLos_Type(Integer32):
    """Custom type cnfFceAlmModLos based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmModLos_Type.__name__ = "Integer32"
_CnfFceAlmModLos_Object = MibScalar
cnfFceAlmModLos = _CnfFceAlmModLos_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 3, 1),
    _CnfFceAlmModLos_Type()
)
cnfFceAlmModLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmModLos.setStatus("current")


class _CnfFceAlmModMse_Type(Integer32):
    """Custom type cnfFceAlmModMse based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmModMse_Type.__name__ = "Integer32"
_CnfFceAlmModMse_Object = MibScalar
cnfFceAlmModMse = _CnfFceAlmModMse_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 3, 2),
    _CnfFceAlmModMse_Type()
)
cnfFceAlmModMse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmModMse.setStatus("current")


class _CnfFceAlmModMseThr_Type(Integer32):
    """Custom type cnfFceAlmModMseThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_CnfFceAlmModMseThr_Type.__name__ = "Integer32"
_CnfFceAlmModMseThr_Object = MibScalar
cnfFceAlmModMseThr = _CnfFceAlmModMseThr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 3, 3),
    _CnfFceAlmModMseThr_Type()
)
cnfFceAlmModMseThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmModMseThr.setStatus("current")
_CnfFceAlmIdu_ObjectIdentity = ObjectIdentity
cnfFceAlmIdu = _CnfFceAlmIdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 4)
)


class _CnfFceAlmIduLic_Type(Integer32):
    """Custom type cnfFceAlmIduLic based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmIduLic_Type.__name__ = "Integer32"
_CnfFceAlmIduLic_Object = MibScalar
cnfFceAlmIduLic = _CnfFceAlmIduLic_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 4, 1),
    _CnfFceAlmIduLic_Type()
)
cnfFceAlmIduLic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmIduLic.setStatus("current")


class _CnfFceAlmIduTemp_Type(Integer32):
    """Custom type cnfFceAlmIduTemp based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmIduTemp_Type.__name__ = "Integer32"
_CnfFceAlmIduTemp_Object = MibScalar
cnfFceAlmIduTemp = _CnfFceAlmIduTemp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 4, 2),
    _CnfFceAlmIduTemp_Type()
)
cnfFceAlmIduTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmIduTemp.setStatus("current")


class _CnfFceAlmIduHw_Type(Integer32):
    """Custom type cnfFceAlmIduHw based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmIduHw_Type.__name__ = "Integer32"
_CnfFceAlmIduHw_Object = MibScalar
cnfFceAlmIduHw = _CnfFceAlmIduHw_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 4, 3),
    _CnfFceAlmIduHw_Type()
)
cnfFceAlmIduHw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmIduHw.setStatus("current")


class _CnfFceAlmIduSw_Type(Integer32):
    """Custom type cnfFceAlmIduSw based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmIduSw_Type.__name__ = "Integer32"
_CnfFceAlmIduSw_Object = MibScalar
cnfFceAlmIduSw = _CnfFceAlmIduSw_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 4, 4),
    _CnfFceAlmIduSw_Type()
)
cnfFceAlmIduSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmIduSw.setStatus("current")
_CnfFceAlmOdu_ObjectIdentity = ObjectIdentity
cnfFceAlmOdu = _CnfFceAlmOdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5)
)


class _CnfFceAlmOduTemp_Type(Integer32):
    """Custom type cnfFceAlmOduTemp based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmOduTemp_Type.__name__ = "Integer32"
_CnfFceAlmOduTemp_Object = MibScalar
cnfFceAlmOduTemp = _CnfFceAlmOduTemp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 1),
    _CnfFceAlmOduTemp_Type()
)
cnfFceAlmOduTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmOduTemp.setStatus("current")


class _CnfFceAlmOduComm_Type(Integer32):
    """Custom type cnfFceAlmOduComm based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmOduComm_Type.__name__ = "Integer32"
_CnfFceAlmOduComm_Object = MibScalar
cnfFceAlmOduComm = _CnfFceAlmOduComm_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 2),
    _CnfFceAlmOduComm_Type()
)
cnfFceAlmOduComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmOduComm.setStatus("current")


class _CnfFceAlmOduAlm_Type(Integer32):
    """Custom type cnfFceAlmOduAlm based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmOduAlm_Type.__name__ = "Integer32"
_CnfFceAlmOduAlm_Object = MibScalar
cnfFceAlmOduAlm = _CnfFceAlmOduAlm_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 3),
    _CnfFceAlmOduAlm_Type()
)
cnfFceAlmOduAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmOduAlm.setStatus("current")


class _CnfFceAlmOduRxl_Type(Integer32):
    """Custom type cnfFceAlmOduRxl based on Integer32"""
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
        *(("inactiveANDnoalarm", 0),
          ("activeANDnoalarm", 1),
          ("inactiveANDalarm", 2),
          ("activeANDalarm", 3))
    )


_CnfFceAlmOduRxl_Type.__name__ = "Integer32"
_CnfFceAlmOduRxl_Object = MibScalar
cnfFceAlmOduRxl = _CnfFceAlmOduRxl_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 4),
    _CnfFceAlmOduRxl_Type()
)
cnfFceAlmOduRxl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmOduRxl.setStatus("current")


class _CnfFceAlmOduRxlThr_Type(Integer32):
    """Custom type cnfFceAlmOduRxlThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 0),
    )


_CnfFceAlmOduRxlThr_Type.__name__ = "Integer32"
_CnfFceAlmOduRxlThr_Object = MibScalar
cnfFceAlmOduRxlThr = _CnfFceAlmOduRxlThr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 5),
    _CnfFceAlmOduRxlThr_Type()
)
cnfFceAlmOduRxlThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnfFceAlmOduRxlThr.setStatus("current")


class _CnfFceAlmOduAlmByte_Type(DisplayString):
    """Custom type cnfFceAlmOduAlmByte based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnfFceAlmOduAlmByte_Type.__name__ = "DisplayString"
_CnfFceAlmOduAlmByte_Object = MibScalar
cnfFceAlmOduAlmByte = _CnfFceAlmOduAlmByte_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 2, 4, 5, 6),
    _CnfFceAlmOduAlmByte_Type()
)
cnfFceAlmOduAlmByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnfFceAlmOduAlmByte.setStatus("current")
_InfoFce_ObjectIdentity = ObjectIdentity
infoFce = _InfoFce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3)
)
_InfoFceMng_ObjectIdentity = ObjectIdentity
infoFceMng = _InfoFceMng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 1)
)
_InfoFceMngSnmp_ObjectIdentity = ObjectIdentity
infoFceMngSnmp = _InfoFceMngSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 1, 2)
)


class _InfoFceMngSnmpVer_Type(Integer32):
    """Custom type infoFceMngSnmpVer based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v1ANDv2", 3),
          ("v3", 4),
          ("v1ANDv2ANDv3", 5))
    )


_InfoFceMngSnmpVer_Type.__name__ = "Integer32"
_InfoFceMngSnmpVer_Object = MibScalar
infoFceMngSnmpVer = _InfoFceMngSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 1, 2, 1),
    _InfoFceMngSnmpVer_Type()
)
infoFceMngSnmpVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceMngSnmpVer.setStatus("current")


class _InfoFceMngSnmpAnt_Type(DisplayString):
    """Custom type infoFceMngSnmpAnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InfoFceMngSnmpAnt_Type.__name__ = "DisplayString"
_InfoFceMngSnmpAnt_Object = MibScalar
infoFceMngSnmpAnt = _InfoFceMngSnmpAnt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 1, 2, 2),
    _InfoFceMngSnmpAnt_Type()
)
infoFceMngSnmpAnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceMngSnmpAnt.setStatus("current")
_InfoFceDat_ObjectIdentity = ObjectIdentity
infoFceDat = _InfoFceDat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2)
)
_InfoFceDatTdm_ObjectIdentity = ObjectIdentity
infoFceDatTdm = _InfoFceDatTdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 1)
)


class _InfoFceDatTdmE11port_Type(Integer32):
    """Custom type infoFceDatTdmE11port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 0),
          ("link", 1),
          ("ais", 2))
    )


_InfoFceDatTdmE11port_Type.__name__ = "Integer32"
_InfoFceDatTdmE11port_Object = MibScalar
infoFceDatTdmE11port = _InfoFceDatTdmE11port_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 1, 1),
    _InfoFceDatTdmE11port_Type()
)
infoFceDatTdmE11port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceDatTdmE11port.setStatus("current")


class _InfoFceDatTdmE12port_Type(Integer32):
    """Custom type infoFceDatTdmE12port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loss", 0),
          ("link", 1),
          ("ais", 2))
    )


_InfoFceDatTdmE12port_Type.__name__ = "Integer32"
_InfoFceDatTdmE12port_Object = MibScalar
infoFceDatTdmE12port = _InfoFceDatTdmE12port_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 1, 2),
    _InfoFceDatTdmE12port_Type()
)
infoFceDatTdmE12port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceDatTdmE12port.setStatus("current")


class _InfoFceDatTdmE3port_Type(Integer32):
    """Custom type infoFceDatTdmE3port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loss", 0),
          ("sync", 1))
    )


_InfoFceDatTdmE3port_Type.__name__ = "Integer32"
_InfoFceDatTdmE3port_Object = MibScalar
infoFceDatTdmE3port = _InfoFceDatTdmE3port_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 1, 3),
    _InfoFceDatTdmE3port_Type()
)
infoFceDatTdmE3port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceDatTdmE3port.setStatus("current")
_InfoFceDatEth_ObjectIdentity = ObjectIdentity
infoFceDatEth = _InfoFceDatEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 2)
)


class _InfoFceDatEthA1_Type(Integer32):
    """Custom type infoFceDatEthA1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nolink", 0),
          ("halfEth", 1),
          ("fullEth", 2),
          ("halfFast", 3),
          ("fullFast", 4),
          ("fullGiga", 5))
    )


_InfoFceDatEthA1_Type.__name__ = "Integer32"
_InfoFceDatEthA1_Object = MibScalar
infoFceDatEthA1 = _InfoFceDatEthA1_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 2, 1),
    _InfoFceDatEthA1_Type()
)
infoFceDatEthA1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceDatEthA1.setStatus("current")


class _InfoFceDatEthB1_Type(Integer32):
    """Custom type infoFceDatEthB1 based on Integer32"""
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
        *(("nolink", 0),
          ("halfEth", 1),
          ("fullEth", 2),
          ("halfFast", 3),
          ("fullFast", 4))
    )


_InfoFceDatEthB1_Type.__name__ = "Integer32"
_InfoFceDatEthB1_Object = MibScalar
infoFceDatEthB1 = _InfoFceDatEthB1_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 2, 2, 2),
    _InfoFceDatEthB1_Type()
)
infoFceDatEthB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceDatEthB1.setStatus("current")
_InfoFceRad_ObjectIdentity = ObjectIdentity
infoFceRad = _InfoFceRad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3)
)
_InfoFceRadRf_ObjectIdentity = ObjectIdentity
infoFceRadRf = _InfoFceRadRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 1)
)


class _InfoFceRadRfRSSI_Type(Integer32):
    """Custom type infoFceRadRfRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_InfoFceRadRfRSSI_Type.__name__ = "Integer32"
_InfoFceRadRfRSSI_Object = MibScalar
infoFceRadRfRSSI = _InfoFceRadRfRSSI_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 1, 1),
    _InfoFceRadRfRSSI_Type()
)
infoFceRadRfRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadRfRSSI.setStatus("current")
_InfoFceRadMod_ObjectIdentity = ObjectIdentity
infoFceRadMod = _InfoFceRadMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 2)
)


class _InfoFceRadModSync_Type(Integer32):
    """Custom type infoFceRadModSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nosync", 0),
          ("sync", 1))
    )


_InfoFceRadModSync_Type.__name__ = "Integer32"
_InfoFceRadModSync_Object = MibScalar
infoFceRadModSync = _InfoFceRadModSync_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 2, 1),
    _InfoFceRadModSync_Type()
)
infoFceRadModSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadModSync.setStatus("current")


class _InfoFceRadModMSE_Type(Integer32):
    """Custom type infoFceRadModMSE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 0),
    )


_InfoFceRadModMSE_Type.__name__ = "Integer32"
_InfoFceRadModMSE_Object = MibScalar
infoFceRadModMSE = _InfoFceRadModMSE_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 2, 2),
    _InfoFceRadModMSE_Type()
)
infoFceRadModMSE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadModMSE.setStatus("current")
_InfoFceRadOpt_ObjectIdentity = ObjectIdentity
infoFceRadOpt = _InfoFceRadOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3)
)


class _InfoFceRadOptIduTemp_Type(Integer32):
    """Custom type infoFceRadOptIduTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_InfoFceRadOptIduTemp_Type.__name__ = "Integer32"
_InfoFceRadOptIduTemp_Object = MibScalar
infoFceRadOptIduTemp = _InfoFceRadOptIduTemp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3, 1),
    _InfoFceRadOptIduTemp_Type()
)
infoFceRadOptIduTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadOptIduTemp.setStatus("current")


class _InfoFceRadOptOduTemp_Type(Integer32):
    """Custom type infoFceRadOptOduTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_InfoFceRadOptOduTemp_Type.__name__ = "Integer32"
_InfoFceRadOptOduTemp_Object = MibScalar
infoFceRadOptOduTemp = _InfoFceRadOptOduTemp_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3, 2),
    _InfoFceRadOptOduTemp_Type()
)
infoFceRadOptOduTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadOptOduTemp.setStatus("current")
_InfoFceRadOptIduExtAGC_Type = Integer32
_InfoFceRadOptIduExtAGC_Object = MibScalar
infoFceRadOptIduExtAGC = _InfoFceRadOptIduExtAGC_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3, 3),
    _InfoFceRadOptIduExtAGC_Type()
)
infoFceRadOptIduExtAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadOptIduExtAGC.setStatus("current")
_InfoFceRadOptIduIntAGC_Type = Integer32
_InfoFceRadOptIduIntAGC_Object = MibScalar
infoFceRadOptIduIntAGC = _InfoFceRadOptIduIntAGC_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3, 4),
    _InfoFceRadOptIduIntAGC_Type()
)
infoFceRadOptIduIntAGC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadOptIduIntAGC.setStatus("current")
_InfoFceRadOptIduBitrate_Type = Integer32
_InfoFceRadOptIduBitrate_Object = MibScalar
infoFceRadOptIduBitrate = _InfoFceRadOptIduBitrate_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 3, 3, 3, 5),
    _InfoFceRadOptIduBitrate_Type()
)
infoFceRadOptIduBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoFceRadOptIduBitrate.setStatus("current")
_StatFce_ObjectIdentity = ObjectIdentity
statFce = _StatFce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4)
)
_StatFceBas_ObjectIdentity = ObjectIdentity
statFceBas = _StatFceBas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1)
)
_StatFceBasRfi_ObjectIdentity = ObjectIdentity
statFceBasRfi = _StatFceBasRfi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1)
)
_StatFceBasRfiRxC_Type = Counter64
_StatFceBasRfiRxC_Object = MibScalar
statFceBasRfiRxC = _StatFceBasRfiRxC_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 1),
    _StatFceBasRfiRxC_Type()
)
statFceBasRfiRxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiRxC.setStatus("current")
_StatFceBasRfiRxErr_Type = Counter32
_StatFceBasRfiRxErr_Object = MibScalar
statFceBasRfiRxErr = _StatFceBasRfiRxErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 2),
    _StatFceBasRfiRxErr_Type()
)
statFceBasRfiRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiRxErr.setStatus("current")
_StatFceBasRfiRxSync_Type = Counter32
_StatFceBasRfiRxSync_Object = MibScalar
statFceBasRfiRxSync = _StatFceBasRfiRxSync_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 3),
    _StatFceBasRfiRxSync_Type()
)
statFceBasRfiRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiRxSync.setStatus("current")
_StatFceBasRfiEfs_Type = Counter32
_StatFceBasRfiEfs_Object = MibScalar
statFceBasRfiEfs = _StatFceBasRfiEfs_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 4),
    _StatFceBasRfiEfs_Type()
)
statFceBasRfiEfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiEfs.setStatus("current")
_StatFceBasRfiErs_Type = Counter32
_StatFceBasRfiErs_Object = MibScalar
statFceBasRfiErs = _StatFceBasRfiErs_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 5),
    _StatFceBasRfiErs_Type()
)
statFceBasRfiErs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiErs.setStatus("current")
_StatFceBasRfiTle_Type = Counter32
_StatFceBasRfiTle_Object = MibScalar
statFceBasRfiTle = _StatFceBasRfiTle_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 1, 1, 6),
    _StatFceBasRfiTle_Type()
)
statFceBasRfiTle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBasRfiTle.setStatus("current")
_StatFceDat_ObjectIdentity = ObjectIdentity
statFceDat = _StatFceDat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2)
)
_EtherIfBas_ObjectIdentity = ObjectIdentity
etherIfBas = _EtherIfBas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1)
)
_EtherIfBasLanA1Disc_Type = Counter32
_EtherIfBasLanA1Disc_Object = MibScalar
etherIfBasLanA1Disc = _EtherIfBasLanA1Disc_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 1),
    _EtherIfBasLanA1Disc_Type()
)
etherIfBasLanA1Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA1Disc.setStatus("current")
_EtherIfBasLanA1Filt_Type = Counter32
_EtherIfBasLanA1Filt_Object = MibScalar
etherIfBasLanA1Filt = _EtherIfBasLanA1Filt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 2),
    _EtherIfBasLanA1Filt_Type()
)
etherIfBasLanA1Filt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA1Filt.setStatus("current")
_EtherIfBasLanA1Err_Type = Counter32
_EtherIfBasLanA1Err_Object = MibScalar
etherIfBasLanA1Err = _EtherIfBasLanA1Err_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 3),
    _EtherIfBasLanA1Err_Type()
)
etherIfBasLanA1Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA1Err.setStatus("current")
_EtherIfBasWanADisc_Type = Counter32
_EtherIfBasWanADisc_Object = MibScalar
etherIfBasWanADisc = _EtherIfBasWanADisc_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 4),
    _EtherIfBasWanADisc_Type()
)
etherIfBasWanADisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasWanADisc.setStatus("current")
_EtherIfBasWanAFilt_Type = Counter32
_EtherIfBasWanAFilt_Object = MibScalar
etherIfBasWanAFilt = _EtherIfBasWanAFilt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 5),
    _EtherIfBasWanAFilt_Type()
)
etherIfBasWanAFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasWanAFilt.setStatus("current")
_EtherIfBasWanARx_Type = Counter32
_EtherIfBasWanARx_Object = MibScalar
etherIfBasWanARx = _EtherIfBasWanARx_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 6),
    _EtherIfBasWanARx_Type()
)
etherIfBasWanARx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasWanARx.setStatus("current")
_EtherIfBasLanB1Tx_Type = Counter32
_EtherIfBasLanB1Tx_Object = MibScalar
etherIfBasLanB1Tx = _EtherIfBasLanB1Tx_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 7),
    _EtherIfBasLanB1Tx_Type()
)
etherIfBasLanB1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB1Tx.setStatus("current")
_EtherIfBasLanB1Rx_Type = Counter32
_EtherIfBasLanB1Rx_Object = MibScalar
etherIfBasLanB1Rx = _EtherIfBasLanB1Rx_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 8),
    _EtherIfBasLanB1Rx_Type()
)
etherIfBasLanB1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB1Rx.setStatus("current")
_EtherIfBasLanB1Err_Type = Counter32
_EtherIfBasLanB1Err_Object = MibScalar
etherIfBasLanB1Err = _EtherIfBasLanB1Err_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 9),
    _EtherIfBasLanB1Err_Type()
)
etherIfBasLanB1Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB1Err.setStatus("current")
_EtherIfBasCpuTx_Type = Counter32
_EtherIfBasCpuTx_Object = MibScalar
etherIfBasCpuTx = _EtherIfBasCpuTx_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 10),
    _EtherIfBasCpuTx_Type()
)
etherIfBasCpuTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasCpuTx.setStatus("current")
_EtherIfBasCpuRx_Type = Counter32
_EtherIfBasCpuRx_Object = MibScalar
etherIfBasCpuRx = _EtherIfBasCpuRx_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 11),
    _EtherIfBasCpuRx_Type()
)
etherIfBasCpuRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasCpuRx.setStatus("current")
_EtherIfBasCpuErr_Type = Counter32
_EtherIfBasCpuErr_Object = MibScalar
etherIfBasCpuErr = _EtherIfBasCpuErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 12),
    _EtherIfBasCpuErr_Type()
)
etherIfBasCpuErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasCpuErr.setStatus("current")
_EtherIfBasWanATxUtil_Type = Unsigned32
_EtherIfBasWanATxUtil_Object = MibScalar
etherIfBasWanATxUtil = _EtherIfBasWanATxUtil_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 13),
    _EtherIfBasWanATxUtil_Type()
)
etherIfBasWanATxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasWanATxUtil.setStatus("current")
_EtherIfBasWanARxUtil_Type = Unsigned32
_EtherIfBasWanARxUtil_Object = MibScalar
etherIfBasWanARxUtil = _EtherIfBasWanARxUtil_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 14),
    _EtherIfBasWanARxUtil_Type()
)
etherIfBasWanARxUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasWanARxUtil.setStatus("current")
_EtherIfBasLanA2Disc_Type = Counter32
_EtherIfBasLanA2Disc_Object = MibScalar
etherIfBasLanA2Disc = _EtherIfBasLanA2Disc_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 15),
    _EtherIfBasLanA2Disc_Type()
)
etherIfBasLanA2Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA2Disc.setStatus("current")
_EtherIfBasLanA2Filt_Type = Counter32
_EtherIfBasLanA2Filt_Object = MibScalar
etherIfBasLanA2Filt = _EtherIfBasLanA2Filt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 16),
    _EtherIfBasLanA2Filt_Type()
)
etherIfBasLanA2Filt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA2Filt.setStatus("current")
_EtherIfBasLanA2Err_Type = Counter32
_EtherIfBasLanA2Err_Object = MibScalar
etherIfBasLanA2Err = _EtherIfBasLanA2Err_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 17),
    _EtherIfBasLanA2Err_Type()
)
etherIfBasLanA2Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanA2Err.setStatus("current")
_EtherIfBasLanB2Disc_Type = Counter32
_EtherIfBasLanB2Disc_Object = MibScalar
etherIfBasLanB2Disc = _EtherIfBasLanB2Disc_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 18),
    _EtherIfBasLanB2Disc_Type()
)
etherIfBasLanB2Disc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB2Disc.setStatus("current")
_EtherIfBasLanB2Filt_Type = Counter32
_EtherIfBasLanB2Filt_Object = MibScalar
etherIfBasLanB2Filt = _EtherIfBasLanB2Filt_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 19),
    _EtherIfBasLanB2Filt_Type()
)
etherIfBasLanB2Filt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB2Filt.setStatus("current")
_EtherIfBasLanB2Err_Type = Counter32
_EtherIfBasLanB2Err_Object = MibScalar
etherIfBasLanB2Err = _EtherIfBasLanB2Err_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 1, 20),
    _EtherIfBasLanB2Err_Type()
)
etherIfBasLanB2Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfBasLanB2Err.setStatus("current")
_EtherIfStats_ObjectIdentity = ObjectIdentity
etherIfStats = _EtherIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2)
)
_EtherIfStatsTable_Object = MibTable
etherIfStatsTable = _EtherIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etherIfStatsTable.setStatus("current")
_EtherIfStatsEntry_Object = MibTableRow
etherIfStatsEntry = _EtherIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1)
)
etherIfStatsEntry.setIndexNames(
    (0, "APEX9-MIB", "etherIfStatsIndex"),
)
if mibBuilder.loadTexts:
    etherIfStatsEntry.setStatus("current")


class _EtherIfStatsIndex_Type(Integer32):
    """Custom type etherIfStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EtherIfStatsIndex_Type.__name__ = "Integer32"
_EtherIfStatsIndex_Object = MibTableColumn
etherIfStatsIndex = _EtherIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 1),
    _EtherIfStatsIndex_Type()
)
etherIfStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIndex.setStatus("current")
_EtherIfStatsInGoodOctetsLo_Type = Counter32
_EtherIfStatsInGoodOctetsLo_Object = MibTableColumn
etherIfStatsInGoodOctetsLo = _EtherIfStatsInGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 2),
    _EtherIfStatsInGoodOctetsLo_Type()
)
etherIfStatsInGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInGoodOctetsLo.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInGoodOctetsLo.setUnits("Octets")
_EtherIfStatsInGoodOctetsHi_Type = Counter32
_EtherIfStatsInGoodOctetsHi_Object = MibTableColumn
etherIfStatsInGoodOctetsHi = _EtherIfStatsInGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 3),
    _EtherIfStatsInGoodOctetsHi_Type()
)
etherIfStatsInGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInGoodOctetsHi.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInGoodOctetsHi.setUnits("Octets")
_EtherIfStatsInBadOctets_Type = Counter32
_EtherIfStatsInBadOctets_Object = MibTableColumn
etherIfStatsInBadOctets = _EtherIfStatsInBadOctets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 4),
    _EtherIfStatsInBadOctets_Type()
)
etherIfStatsInBadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInBadOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInBadOctets.setUnits("Octets")
_EtherIfStatsInUnicastPkts_Type = Counter32
_EtherIfStatsInUnicastPkts_Object = MibTableColumn
etherIfStatsInUnicastPkts = _EtherIfStatsInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 5),
    _EtherIfStatsInUnicastPkts_Type()
)
etherIfStatsInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInUnicastPkts.setUnits("Packets")
_EtherIfStatsInBroadcastPkts_Type = Counter32
_EtherIfStatsInBroadcastPkts_Object = MibTableColumn
etherIfStatsInBroadcastPkts = _EtherIfStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 6),
    _EtherIfStatsInBroadcastPkts_Type()
)
etherIfStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInBroadcastPkts.setUnits("Packets")
_EtherIfStatsInMulticastPkts_Type = Counter32
_EtherIfStatsInMulticastPkts_Object = MibTableColumn
etherIfStatsInMulticastPkts = _EtherIfStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 7),
    _EtherIfStatsInMulticastPkts_Type()
)
etherIfStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInMulticastPkts.setUnits("Packets")
_EtherIfStatsInPausePkts_Type = Counter32
_EtherIfStatsInPausePkts_Object = MibTableColumn
etherIfStatsInPausePkts = _EtherIfStatsInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 8),
    _EtherIfStatsInPausePkts_Type()
)
etherIfStatsInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInPausePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInPausePkts.setUnits("Packets")
_EtherIfStatsInUndersizePkts_Type = Counter32
_EtherIfStatsInUndersizePkts_Object = MibTableColumn
etherIfStatsInUndersizePkts = _EtherIfStatsInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 9),
    _EtherIfStatsInUndersizePkts_Type()
)
etherIfStatsInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInUndersizePkts.setUnits("Packets")
_EtherIfStatsInFragments_Type = Counter32
_EtherIfStatsInFragments_Object = MibTableColumn
etherIfStatsInFragments = _EtherIfStatsInFragments_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 10),
    _EtherIfStatsInFragments_Type()
)
etherIfStatsInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInFragments.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInFragments.setUnits("Packets")
_EtherIfStatsInOversizePkts_Type = Counter32
_EtherIfStatsInOversizePkts_Object = MibTableColumn
etherIfStatsInOversizePkts = _EtherIfStatsInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 11),
    _EtherIfStatsInOversizePkts_Type()
)
etherIfStatsInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInOversizePkts.setUnits("Packets")
_EtherIfStatsInJabbers_Type = Counter32
_EtherIfStatsInJabbers_Object = MibTableColumn
etherIfStatsInJabbers = _EtherIfStatsInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 12),
    _EtherIfStatsInJabbers_Type()
)
etherIfStatsInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInJabbers.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInJabbers.setUnits("Packets")
_EtherIfStatsInRxErr_Type = Counter32
_EtherIfStatsInRxErr_Object = MibTableColumn
etherIfStatsInRxErr = _EtherIfStatsInRxErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 13),
    _EtherIfStatsInRxErr_Type()
)
etherIfStatsInRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInRxErr.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInRxErr.setUnits("Packets")
_EtherIfStatsInFCSErr_Type = Counter32
_EtherIfStatsInFCSErr_Object = MibTableColumn
etherIfStatsInFCSErr = _EtherIfStatsInFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 14),
    _EtherIfStatsInFCSErr_Type()
)
etherIfStatsInFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsInFCSErr.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsInFCSErr.setUnits("Packets")
_EtherIfStatsOutGoodOctetsLo_Type = Counter32
_EtherIfStatsOutGoodOctetsLo_Object = MibTableColumn
etherIfStatsOutGoodOctetsLo = _EtherIfStatsOutGoodOctetsLo_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 15),
    _EtherIfStatsOutGoodOctetsLo_Type()
)
etherIfStatsOutGoodOctetsLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutGoodOctetsLo.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutGoodOctetsLo.setUnits("Octets")
_EtherIfStatsOutGoodOctetsHi_Type = Counter32
_EtherIfStatsOutGoodOctetsHi_Object = MibTableColumn
etherIfStatsOutGoodOctetsHi = _EtherIfStatsOutGoodOctetsHi_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 16),
    _EtherIfStatsOutGoodOctetsHi_Type()
)
etherIfStatsOutGoodOctetsHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutGoodOctetsHi.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutGoodOctetsHi.setUnits("Octets")
_EtherIfStatsOutUnicastPkts_Type = Counter32
_EtherIfStatsOutUnicastPkts_Object = MibTableColumn
etherIfStatsOutUnicastPkts = _EtherIfStatsOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 17),
    _EtherIfStatsOutUnicastPkts_Type()
)
etherIfStatsOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutUnicastPkts.setUnits("Packets")
_EtherIfStatsOutBroadcastPkts_Type = Counter32
_EtherIfStatsOutBroadcastPkts_Object = MibTableColumn
etherIfStatsOutBroadcastPkts = _EtherIfStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 18),
    _EtherIfStatsOutBroadcastPkts_Type()
)
etherIfStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutBroadcastPkts.setUnits("Packets")
_EtherIfStatsOutMulticastPkts_Type = Counter32
_EtherIfStatsOutMulticastPkts_Object = MibTableColumn
etherIfStatsOutMulticastPkts = _EtherIfStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 19),
    _EtherIfStatsOutMulticastPkts_Type()
)
etherIfStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutMulticastPkts.setUnits("Packets")
_EtherIfStatsOutPausePkts_Type = Counter32
_EtherIfStatsOutPausePkts_Object = MibTableColumn
etherIfStatsOutPausePkts = _EtherIfStatsOutPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 20),
    _EtherIfStatsOutPausePkts_Type()
)
etherIfStatsOutPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutPausePkts.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutPausePkts.setUnits("Packets")
_EtherIfStatsOutFCSErr_Type = Counter32
_EtherIfStatsOutFCSErr_Object = MibTableColumn
etherIfStatsOutFCSErr = _EtherIfStatsOutFCSErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 21),
    _EtherIfStatsOutFCSErr_Type()
)
etherIfStatsOutFCSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsOutFCSErr.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsOutFCSErr.setUnits("Packets")
_EtherIfStatsIOPkts64Octets_Type = Counter32
_EtherIfStatsIOPkts64Octets_Object = MibTableColumn
etherIfStatsIOPkts64Octets = _EtherIfStatsIOPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 22),
    _EtherIfStatsIOPkts64Octets_Type()
)
etherIfStatsIOPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts64Octets.setUnits("Packets")
_EtherIfStatsIOPkts65to127Octets_Type = Counter32
_EtherIfStatsIOPkts65to127Octets_Object = MibTableColumn
etherIfStatsIOPkts65to127Octets = _EtherIfStatsIOPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 23),
    _EtherIfStatsIOPkts65to127Octets_Type()
)
etherIfStatsIOPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts65to127Octets.setUnits("Packets")
_EtherIfStatsIOPkts128to255Octets_Type = Counter32
_EtherIfStatsIOPkts128to255Octets_Object = MibTableColumn
etherIfStatsIOPkts128to255Octets = _EtherIfStatsIOPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 24),
    _EtherIfStatsIOPkts128to255Octets_Type()
)
etherIfStatsIOPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts128to255Octets.setUnits("Packets")
_EtherIfStatsIOPkts256to511Octets_Type = Counter32
_EtherIfStatsIOPkts256to511Octets_Object = MibTableColumn
etherIfStatsIOPkts256to511Octets = _EtherIfStatsIOPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 25),
    _EtherIfStatsIOPkts256to511Octets_Type()
)
etherIfStatsIOPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts256to511Octets.setUnits("Packets")
_EtherIfStatsIOPkts512to1023Octets_Type = Counter32
_EtherIfStatsIOPkts512to1023Octets_Object = MibTableColumn
etherIfStatsIOPkts512to1023Octets = _EtherIfStatsIOPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 26),
    _EtherIfStatsIOPkts512to1023Octets_Type()
)
etherIfStatsIOPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts512to1023Octets.setUnits("Packets")
_EtherIfStatsIOPkts1024toMaxOctets_Type = Counter32
_EtherIfStatsIOPkts1024toMaxOctets_Object = MibTableColumn
etherIfStatsIOPkts1024toMaxOctets = _EtherIfStatsIOPkts1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 2, 2, 1, 1, 27),
    _EtherIfStatsIOPkts1024toMaxOctets_Type()
)
etherIfStatsIOPkts1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts1024toMaxOctets.setStatus("current")
if mibBuilder.loadTexts:
    etherIfStatsIOPkts1024toMaxOctets.setUnits("Packets")
_StatFceHsi_ObjectIdentity = ObjectIdentity
statFceHsi = _StatFceHsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 3)
)
_StatFceHsiCnt_ObjectIdentity = ObjectIdentity
statFceHsiCnt = _StatFceHsiCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 3, 1)
)
_StatFceHsiCntRxC_Type = Counter64
_StatFceHsiCntRxC_Object = MibScalar
statFceHsiCntRxC = _StatFceHsiCntRxC_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 3, 1, 1),
    _StatFceHsiCntRxC_Type()
)
statFceHsiCntRxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceHsiCntRxC.setStatus("current")
_StatFceHsiCntRxErr_Type = Counter32
_StatFceHsiCntRxErr_Object = MibScalar
statFceHsiCntRxErr = _StatFceHsiCntRxErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 3, 1, 2),
    _StatFceHsiCntRxErr_Type()
)
statFceHsiCntRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceHsiCntRxErr.setStatus("current")
_StatFceHsiCntRxSync_Type = Counter32
_StatFceHsiCntRxSync_Object = MibScalar
statFceHsiCntRxSync = _StatFceHsiCntRxSync_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 3, 1, 3),
    _StatFceHsiCntRxSync_Type()
)
statFceHsiCntRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceHsiCntRxSync.setStatus("current")
_StatFceBer_ObjectIdentity = ObjectIdentity
statFceBer = _StatFceBer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4)
)
_StatFceBerCnt_ObjectIdentity = ObjectIdentity
statFceBerCnt = _StatFceBerCnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1)
)
_StatFceBerCntRxC_Type = Counter64
_StatFceBerCntRxC_Object = MibScalar
statFceBerCntRxC = _StatFceBerCntRxC_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 1),
    _StatFceBerCntRxC_Type()
)
statFceBerCntRxC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntRxC.setStatus("current")
_StatFceBerCntRxErr_Type = Counter32
_StatFceBerCntRxErr_Object = MibScalar
statFceBerCntRxErr = _StatFceBerCntRxErr_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 2),
    _StatFceBerCntRxErr_Type()
)
statFceBerCntRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntRxErr.setStatus("current")
_StatFceBerCntRxSync_Type = Counter32
_StatFceBerCntRxSync_Object = MibScalar
statFceBerCntRxSync = _StatFceBerCntRxSync_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 3),
    _StatFceBerCntRxSync_Type()
)
statFceBerCntRxSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntRxSync.setStatus("current")
_StatFceBerCntEfs_Type = Counter32
_StatFceBerCntEfs_Object = MibScalar
statFceBerCntEfs = _StatFceBerCntEfs_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 4),
    _StatFceBerCntEfs_Type()
)
statFceBerCntEfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntEfs.setStatus("current")
_StatFceBerCntErs_Type = Counter32
_StatFceBerCntErs_Object = MibScalar
statFceBerCntErs = _StatFceBerCntErs_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 5),
    _StatFceBerCntErs_Type()
)
statFceBerCntErs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntErs.setStatus("current")
_StatFceBerCntTle_Type = Counter32
_StatFceBerCntTle_Object = MibScalar
statFceBerCntTle = _StatFceBerCntTle_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 6),
    _StatFceBerCntTle_Type()
)
statFceBerCntTle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntTle.setStatus("current")
_StatFceBerCntTbe_Type = Counter32
_StatFceBerCntTbe_Object = MibScalar
statFceBerCntTbe = _StatFceBerCntTbe_Object(
    (1, 3, 6, 1, 4, 1, 39229, 1, 1, 2, 4, 4, 1, 7),
    _StatFceBerCntTbe_Type()
)
statFceBerCntTbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFceBerCntTbe.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39229, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APEX9-MIB",
    **{"apex9": apex9,
       "brand": brand,
       "products": products,
       "ll1000": ll1000,
       "sysFce": sysFce,
       "sysFceBas": sysFceBas,
       "sysFceBasDev": sysFceBasDev,
       "sysFceBasDevName": sysFceBasDevName,
       "sysFceBasDevAddDesc1": sysFceBasDevAddDesc1,
       "sysFceBasDevAddDesc2": sysFceBasDevAddDesc2,
       "sysFceBasDevAddDesc3": sysFceBasDevAddDesc3,
       "sysFceBasDevAddDesc4": sysFceBasDevAddDesc4,
       "sysFceBasDevAddDesc5": sysFceBasDevAddDesc5,
       "sysFceBasDevDate": sysFceBasDevDate,
       "sysFceBasDevTime": sysFceBasDevTime,
       "sysFceBasDevIduProNum": sysFceBasDevIduProNum,
       "sysFceBasDevIduSerNum": sysFceBasDevIduSerNum,
       "sysFceBasDevOduProNum": sysFceBasDevOduProNum,
       "sysFceBasDevOduSerNum": sysFceBasDevOduSerNum,
       "sysFceBasDevIduHwBase": sysFceBasDevIduHwBase,
       "sysFceBasDevIduFwBase": sysFceBasDevIduFwBase,
       "sysFceBasDevIduOsKern": sysFceBasDevIduOsKern,
       "sysFceBasDevIduOsDev": sysFceBasDevIduOsDev,
       "sysFceBasDevOduSwVer": sysFceBasDevOduSwVer,
       "sysFceBasDevCpuMac": sysFceBasDevCpuMac,
       "sysFceBasDevSysStat": sysFceBasDevSysStat,
       "sysFceBasDevDesc1": sysFceBasDevDesc1,
       "sysFceBasDevDesc2": sysFceBasDevDesc2,
       "sysFceBasDevAddInfo": sysFceBasDevAddInfo,
       "sysFceBasCmd": sysFceBasCmd,
       "sysFceBasCmdEn": sysFceBasCmdEn,
       "sysFceBasCmdWr": sysFceBasCmdWr,
       "sysFceBasCmdRn": sysFceBasCmdRn,
       "sysFceBasCmdDsg": sysFceBasCmdDsg,
       "sysFceBasCmdRem": sysFceBasCmdRem,
       "sysFceBasCmdAuto": sysFceBasCmdAuto,
       "sysFceBasCmdAlm": sysFceBasCmdAlm,
       "sysFceBasCmdClr": sysFceBasCmdClr,
       "sysFceBasCmdRst": sysFceBasCmdRst,
       "cnfFce": cnfFce,
       "cnfFceMng": cnfFceMng,
       "cnfFceMngIp": cnfFceMngIp,
       "cnfFceMngIpEthAddr": cnfFceMngIpEthAddr,
       "cnfFceMngIpEthMask": cnfFceMngIpEthMask,
       "cnfFceMngIpRemote": cnfFceMngIpRemote,
       "cnfFceMngIpGtwAddr": cnfFceMngIpGtwAddr,
       "cnfFceMngIpFtpUsb": cnfFceMngIpFtpUsb,
       "cnfFceMngIpSecEthaddr": cnfFceMngIpSecEthaddr,
       "cnfFceMngIpSecEthMask": cnfFceMngIpSecEthMask,
       "cnfFceMngIpSecProxyArp": cnfFceMngIpSecProxyArp,
       "cnfFceMngSnmp": cnfFceMngSnmp,
       "cnfFceMngSnmpRstring": cnfFceMngSnmpRstring,
       "cnfFceMngSnmpWstring": cnfFceMngSnmpWstring,
       "cnfFceMngSnmpDport": cnfFceMngSnmpDport,
       "cnfFceMngSnmpTport": cnfFceMngSnmpTport,
       "cnfFceMngSnmpTrap1Ip": cnfFceMngSnmpTrap1Ip,
       "cnfFceMngSnmpTrap2Ip": cnfFceMngSnmpTrap2Ip,
       "cnfFceMngSnmpTrap3Ip": cnfFceMngSnmpTrap3Ip,
       "cnfFceDat": cnfFceDat,
       "cnfFceDatTdm": cnfFceDatTdm,
       "cnfFceDatTdmE3Ena": cnfFceDatTdmE3Ena,
       "cnfFceDatTdmE3Frm": cnfFceDatTdmE3Frm,
       "cnfFceDatTdmE3Loop": cnfFceDatTdmE3Loop,
       "cnfFceDatTdmE21Mod": cnfFceDatTdmE21Mod,
       "cnfFceDatTdmE22Ena": cnfFceDatTdmE22Ena,
       "cnfFceDatTdmE22Loop": cnfFceDatTdmE22Loop,
       "cnfFceDatTdmE22Mod": cnfFceDatTdmE22Mod,
       "cnfFceDatTdmE23Ena": cnfFceDatTdmE23Ena,
       "cnfFceDatTdmE23Loop": cnfFceDatTdmE23Loop,
       "cnfFceDatTdmE23Mod": cnfFceDatTdmE23Mod,
       "cnfFceDatTdmE24Ena": cnfFceDatTdmE24Ena,
       "cnfFceDatTdmE24Loop": cnfFceDatTdmE24Loop,
       "cnfFceDatTdmE24Mod": cnfFceDatTdmE24Mod,
       "cnfFceDatTdmE11Ena": cnfFceDatTdmE11Ena,
       "cnfFceDatTdmE11Loop": cnfFceDatTdmE11Loop,
       "cnfFceDatTdmE11Mod": cnfFceDatTdmE11Mod,
       "cnfFceDatTdmE12Ena": cnfFceDatTdmE12Ena,
       "cnfFceDatTdmE12Loop": cnfFceDatTdmE12Loop,
       "cnfFceDatTdmE12Mod": cnfFceDatTdmE12Mod,
       "cnfFceDatTdmE13Ena": cnfFceDatTdmE13Ena,
       "cnfFceDatTdmE13Loop": cnfFceDatTdmE13Loop,
       "cnfFceDatTdmE13Mod": cnfFceDatTdmE13Mod,
       "cnfFceDatTdmE14Ena": cnfFceDatTdmE14Ena,
       "cnfFceDatTdmE14Loop": cnfFceDatTdmE14Loop,
       "cnfFceDatTdmE14Mod": cnfFceDatTdmE14Mod,
       "cnfFceDatEth": cnfFceDatEth,
       "cnfFceDatEthLanAb": cnfFceDatEthLanAb,
       "cnfFceDatEthSpeed": cnfFceDatEthSpeed,
       "cnfFceDatEthA1Aneg": cnfFceDatEthA1Aneg,
       "cnfFceDatEthA1Dupl": cnfFceDatEthA1Dupl,
       "cnfFceDatEthA1Speed": cnfFceDatEthA1Speed,
       "cnfFceDatEthA1Mdix": cnfFceDatEthA1Mdix,
       "cnfFceDatEthB1Aneg": cnfFceDatEthB1Aneg,
       "cnfFceDatEthB1Dupl": cnfFceDatEthB1Dupl,
       "cnfFceDatEthB1Speed": cnfFceDatEthB1Speed,
       "cnfFceDatEthB1Mdix": cnfFceDatEthB1Mdix,
       "cnfFceDatBer": cnfFceDatBer,
       "cnfFceDatBerSpeed": cnfFceDatBerSpeed,
       "cnfFceDatBerInerr": cnfFceDatBerInerr,
       "cnfFceRad": cnfFceRad,
       "cnfFceRadRf": cnfFceRadRf,
       "cnfFceRadRfTxPwr": cnfFceRadRfTxPwr,
       "cnfFceRadRfTxFreq": cnfFceRadRfTxFreq,
       "cnfFceRadRfRxFreq": cnfFceRadRfRxFreq,
       "cnfFceRadRfAtpcEna": cnfFceRadRfAtpcEna,
       "cnfFceRadRfAtpcRxl": cnfFceRadRfAtpcRxl,
       "cnfFceRadMod": cnfFceRadMod,
       "cnfFceRadModActMod": cnfFceRadModActMod,
       "cnfFceRadModAcmEna": cnfFceRadModAcmEna,
       "cnfFceRadModAcmMod0": cnfFceRadModAcmMod0,
       "cnfFceRadModAcmMod1": cnfFceRadModAcmMod1,
       "cnfFceRadModAcmMod2": cnfFceRadModAcmMod2,
       "cnfFceRadModTable": cnfFceRadModTable,
       "cnfFceRadModEntry": cnfFceRadModEntry,
       "cnfFceRadModTableIndex": cnfFceRadModTableIndex,
       "cnfFceRadModTableMod": cnfFceRadModTableMod,
       "cnfFceRadOpt": cnfFceRadOpt,
       "cnfFceRadOptOduMute": cnfFceRadOptOduMute,
       "cnfFceRadOptOduMuteStat": cnfFceRadOptOduMuteStat,
       "cnfFceRadOptPwrDown": cnfFceRadOptPwrDown,
       "cnfFceRadOptOduFlt": cnfFceRadOptOduFlt,
       "cnfFceRadOptOduFltStat": cnfFceRadOptOduFltStat,
       "cnfFceRadOptOduSp": cnfFceRadOptOduSp,
       "cnfFceRadOptSpStat": cnfFceRadOptSpStat,
       "cnfFceRadOptLat": cnfFceRadOptLat,
       "cnfFceRadOptCw": cnfFceRadOptCw,
       "cnfFceRadOptAgc": cnfFceRadOptAgc,
       "cnfFceAlm": cnfFceAlm,
       "cnfFceAlmPort": cnfFceAlmPort,
       "cnfFceAlmPortE11Link": cnfFceAlmPortE11Link,
       "cnfFceAlmPortE11Ais": cnfFceAlmPortE11Ais,
       "cnfFceAlmPortE12Link": cnfFceAlmPortE12Link,
       "cnfFceAlmPortE12Ais": cnfFceAlmPortE12Ais,
       "cnfFceAlmPortLanA1Link": cnfFceAlmPortLanA1Link,
       "cnfFceAlmPortLanB1Link": cnfFceAlmPortLanB1Link,
       "cnfFceAlmPortE3Los": cnfFceAlmPortE3Los,
       "cnfFceAlmPortE3Fer": cnfFceAlmPortE3Fer,
       "cnfFceAlmMux": cnfFceAlmMux,
       "cnfFceAlmMuxRfiLos": cnfFceAlmMuxRfiLos,
       "cnfFceAlmMuxRfiFer": cnfFceAlmMuxRfiFer,
       "cnfFceAlmMuxRfiFerThr": cnfFceAlmMuxRfiFerThr,
       "cnfFceAlmMod": cnfFceAlmMod,
       "cnfFceAlmModLos": cnfFceAlmModLos,
       "cnfFceAlmModMse": cnfFceAlmModMse,
       "cnfFceAlmModMseThr": cnfFceAlmModMseThr,
       "cnfFceAlmIdu": cnfFceAlmIdu,
       "cnfFceAlmIduLic": cnfFceAlmIduLic,
       "cnfFceAlmIduTemp": cnfFceAlmIduTemp,
       "cnfFceAlmIduHw": cnfFceAlmIduHw,
       "cnfFceAlmIduSw": cnfFceAlmIduSw,
       "cnfFceAlmOdu": cnfFceAlmOdu,
       "cnfFceAlmOduTemp": cnfFceAlmOduTemp,
       "cnfFceAlmOduComm": cnfFceAlmOduComm,
       "cnfFceAlmOduAlm": cnfFceAlmOduAlm,
       "cnfFceAlmOduRxl": cnfFceAlmOduRxl,
       "cnfFceAlmOduRxlThr": cnfFceAlmOduRxlThr,
       "cnfFceAlmOduAlmByte": cnfFceAlmOduAlmByte,
       "infoFce": infoFce,
       "infoFceMng": infoFceMng,
       "infoFceMngSnmp": infoFceMngSnmp,
       "infoFceMngSnmpVer": infoFceMngSnmpVer,
       "infoFceMngSnmpAnt": infoFceMngSnmpAnt,
       "infoFceDat": infoFceDat,
       "infoFceDatTdm": infoFceDatTdm,
       "infoFceDatTdmE11port": infoFceDatTdmE11port,
       "infoFceDatTdmE12port": infoFceDatTdmE12port,
       "infoFceDatTdmE3port": infoFceDatTdmE3port,
       "infoFceDatEth": infoFceDatEth,
       "infoFceDatEthA1": infoFceDatEthA1,
       "infoFceDatEthB1": infoFceDatEthB1,
       "infoFceRad": infoFceRad,
       "infoFceRadRf": infoFceRadRf,
       "infoFceRadRfRSSI": infoFceRadRfRSSI,
       "infoFceRadMod": infoFceRadMod,
       "infoFceRadModSync": infoFceRadModSync,
       "infoFceRadModMSE": infoFceRadModMSE,
       "infoFceRadOpt": infoFceRadOpt,
       "infoFceRadOptIduTemp": infoFceRadOptIduTemp,
       "infoFceRadOptOduTemp": infoFceRadOptOduTemp,
       "infoFceRadOptIduExtAGC": infoFceRadOptIduExtAGC,
       "infoFceRadOptIduIntAGC": infoFceRadOptIduIntAGC,
       "infoFceRadOptIduBitrate": infoFceRadOptIduBitrate,
       "statFce": statFce,
       "statFceBas": statFceBas,
       "statFceBasRfi": statFceBasRfi,
       "statFceBasRfiRxC": statFceBasRfiRxC,
       "statFceBasRfiRxErr": statFceBasRfiRxErr,
       "statFceBasRfiRxSync": statFceBasRfiRxSync,
       "statFceBasRfiEfs": statFceBasRfiEfs,
       "statFceBasRfiErs": statFceBasRfiErs,
       "statFceBasRfiTle": statFceBasRfiTle,
       "statFceDat": statFceDat,
       "etherIfBas": etherIfBas,
       "etherIfBasLanA1Disc": etherIfBasLanA1Disc,
       "etherIfBasLanA1Filt": etherIfBasLanA1Filt,
       "etherIfBasLanA1Err": etherIfBasLanA1Err,
       "etherIfBasWanADisc": etherIfBasWanADisc,
       "etherIfBasWanAFilt": etherIfBasWanAFilt,
       "etherIfBasWanARx": etherIfBasWanARx,
       "etherIfBasLanB1Tx": etherIfBasLanB1Tx,
       "etherIfBasLanB1Rx": etherIfBasLanB1Rx,
       "etherIfBasLanB1Err": etherIfBasLanB1Err,
       "etherIfBasCpuTx": etherIfBasCpuTx,
       "etherIfBasCpuRx": etherIfBasCpuRx,
       "etherIfBasCpuErr": etherIfBasCpuErr,
       "etherIfBasWanATxUtil": etherIfBasWanATxUtil,
       "etherIfBasWanARxUtil": etherIfBasWanARxUtil,
       "etherIfBasLanA2Disc": etherIfBasLanA2Disc,
       "etherIfBasLanA2Filt": etherIfBasLanA2Filt,
       "etherIfBasLanA2Err": etherIfBasLanA2Err,
       "etherIfBasLanB2Disc": etherIfBasLanB2Disc,
       "etherIfBasLanB2Filt": etherIfBasLanB2Filt,
       "etherIfBasLanB2Err": etherIfBasLanB2Err,
       "etherIfStats": etherIfStats,
       "etherIfStatsTable": etherIfStatsTable,
       "etherIfStatsEntry": etherIfStatsEntry,
       "etherIfStatsIndex": etherIfStatsIndex,
       "etherIfStatsInGoodOctetsLo": etherIfStatsInGoodOctetsLo,
       "etherIfStatsInGoodOctetsHi": etherIfStatsInGoodOctetsHi,
       "etherIfStatsInBadOctets": etherIfStatsInBadOctets,
       "etherIfStatsInUnicastPkts": etherIfStatsInUnicastPkts,
       "etherIfStatsInBroadcastPkts": etherIfStatsInBroadcastPkts,
       "etherIfStatsInMulticastPkts": etherIfStatsInMulticastPkts,
       "etherIfStatsInPausePkts": etherIfStatsInPausePkts,
       "etherIfStatsInUndersizePkts": etherIfStatsInUndersizePkts,
       "etherIfStatsInFragments": etherIfStatsInFragments,
       "etherIfStatsInOversizePkts": etherIfStatsInOversizePkts,
       "etherIfStatsInJabbers": etherIfStatsInJabbers,
       "etherIfStatsInRxErr": etherIfStatsInRxErr,
       "etherIfStatsInFCSErr": etherIfStatsInFCSErr,
       "etherIfStatsOutGoodOctetsLo": etherIfStatsOutGoodOctetsLo,
       "etherIfStatsOutGoodOctetsHi": etherIfStatsOutGoodOctetsHi,
       "etherIfStatsOutUnicastPkts": etherIfStatsOutUnicastPkts,
       "etherIfStatsOutBroadcastPkts": etherIfStatsOutBroadcastPkts,
       "etherIfStatsOutMulticastPkts": etherIfStatsOutMulticastPkts,
       "etherIfStatsOutPausePkts": etherIfStatsOutPausePkts,
       "etherIfStatsOutFCSErr": etherIfStatsOutFCSErr,
       "etherIfStatsIOPkts64Octets": etherIfStatsIOPkts64Octets,
       "etherIfStatsIOPkts65to127Octets": etherIfStatsIOPkts65to127Octets,
       "etherIfStatsIOPkts128to255Octets": etherIfStatsIOPkts128to255Octets,
       "etherIfStatsIOPkts256to511Octets": etherIfStatsIOPkts256to511Octets,
       "etherIfStatsIOPkts512to1023Octets": etherIfStatsIOPkts512to1023Octets,
       "etherIfStatsIOPkts1024toMaxOctets": etherIfStatsIOPkts1024toMaxOctets,
       "statFceHsi": statFceHsi,
       "statFceHsiCnt": statFceHsiCnt,
       "statFceHsiCntRxC": statFceHsiCntRxC,
       "statFceHsiCntRxErr": statFceHsiCntRxErr,
       "statFceHsiCntRxSync": statFceHsiCntRxSync,
       "statFceBer": statFceBer,
       "statFceBerCnt": statFceBerCnt,
       "statFceBerCntRxC": statFceBerCntRxC,
       "statFceBerCntRxErr": statFceBerCntRxErr,
       "statFceBerCntRxSync": statFceBerCntRxSync,
       "statFceBerCntEfs": statFceBerCntEfs,
       "statFceBerCntErs": statFceBerCntErs,
       "statFceBerCntTle": statFceBerCntTle,
       "statFceBerCntTbe": statFceBerCntTbe,
       "traps": traps}
)
