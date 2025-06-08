# SNMP MIB module (SW57-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1588/SW57-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:12:33 2025
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

(bcsiModules,
 fcSwitch) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsiModules",
    "fcSwitch")

(FcWwn,
 SwDomainIndex,
 SwNbIndex,
 SwPortIndex,
 SwSensorIndex,
 SwTrunkMaster) = mibBuilder.importSymbols(
    "Brocade-TC",
    "FcWwn",
    "SwDomainIndex",
    "SwNbIndex",
    "SwPortIndex",
    "SwSensorIndex",
    "SwTrunkMaster")

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

swMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 3, 1, 3)
)
if mibBuilder.loadTexts:
    swMibModule.setRevisions(
        ("1903-01-13 14:30",
         "1903-07-20 14:30",
         "1904-04-15 10:30",
         "1904-08-06 18:30",
         "1905-04-29 20:16",
         "1906-01-09 09:00",
         "1906-05-17 09:00",
         "1907-01-23 09:00",
         "1907-06-08 12:00",
         "1907-06-27 10:30",
         "1907-08-01 12:20",
         "1907-08-29 04:42")
    )


# Types definitions



class SwFwActs(Integer32):
    """Custom type SwFwActs based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("swFwNoAction", 0),
          ("swFwErrlog", 1),
          ("swFwSnmptrap", 2),
          ("swFwErrlogSnmptrap", 3),
          ("swFwPortloglock", 4),
          ("swFwErrlogPortloglock", 5),
          ("swFwSnmptrapPortloglock", 6),
          ("swFwErrlogSnmptrapPortloglock", 7),
          ("swFwRn", 8),
          ("swFwElRn", 9),
          ("swFwStRn", 10),
          ("swFwElStRn", 11),
          ("swFwPlRn", 12),
          ("swFwElPlRn", 13),
          ("swFwStPlRn", 14),
          ("swFwElStPlRn", 15),
          ("swFwMailAlert", 16),
          ("swFwMailAlertErrlog", 17),
          ("swFwMailAlertSnmptrap", 18),
          ("swFwMailAlertErrlogSnmptrap", 19),
          ("swFwMailAlertPortloglock", 20),
          ("swFwMailAlertErrlogPortloglock", 21),
          ("swFwMailAlertSnmptrapPortloglock", 22),
          ("swFwMailAlertErrlogSnmptrapPortloglock", 23),
          ("swFwMailAlertRn", 24),
          ("swFwElMailAlertRn", 25),
          ("swFwMailAlertStRn", 26),
          ("swFwMailAlertElStRn", 27),
          ("swFwMailAlertPlRn", 28),
          ("swFwMailAlertElPlRn", 29),
          ("swFwMailAlertStPlRn", 30),
          ("swFwMailAlertElStPlRn", 31))
    )





class SwFwLevels(Integer32):
    """Custom type SwFwLevels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swFwReserved", 1),
          ("swFwDefault", 2),
          ("swFwCustom", 3))
    )





class SwFwClassesAreas(Integer32):
    """Custom type SwFwClassesAreas based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85)
        )
    )
    namedValues = NamedValues(
        *(("swFwEnvTemp", 1),
          ("swFwEnvFan", 2),
          ("swFwEnvPs", 3),
          ("swFwTransceiverTemp", 4),
          ("swFwTransceiverRxp", 5),
          ("swFwTransceiverTxp", 6),
          ("swFwTransceiverCurrent", 7),
          ("swFwPortLink", 8),
          ("swFwPortSync", 9),
          ("swFwPortSignal", 10),
          ("swFwPortPe", 11),
          ("swFwPortWords", 12),
          ("swFwPortCrcs", 13),
          ("swFwPortRXPerf", 14),
          ("swFwPortTXPerf", 15),
          ("swFwPortState", 16),
          ("swFwFabricEd", 17),
          ("swFwFabricFr", 18),
          ("swFwFabricDi", 19),
          ("swFwFabricSc", 20),
          ("swFwFabricZc", 21),
          ("swFwFabricFq", 22),
          ("swFwFabricFl", 23),
          ("swFwFabricGs", 24),
          ("swFwEPortLink", 25),
          ("swFwEPortSync", 26),
          ("swFwEPortSignal", 27),
          ("swFwEPortPe", 28),
          ("swFwEPortWords", 29),
          ("swFwEPortCrcs", 30),
          ("swFwEPortRXPerf", 31),
          ("swFwEPortTXPerf", 32),
          ("swFwEPortState", 33),
          ("swFwFCUPortLink", 34),
          ("swFwFCUPortSync", 35),
          ("swFwFCUPortSignal", 36),
          ("swFwFCUPortPe", 37),
          ("swFwFCUPortWords", 38),
          ("swFwFCUPortCrcs", 39),
          ("swFwFCUPortRXPerf", 40),
          ("swFwFCUPortTXPerf", 41),
          ("swFwFCUPortState", 42),
          ("swFwFOPPortLink", 43),
          ("swFwFOPPortSync", 44),
          ("swFwFOPPortSignal", 45),
          ("swFwFOPPortPe", 46),
          ("swFwFOPPortWords", 47),
          ("swFwFOPPortCrcs", 48),
          ("swFwFOPPortRXPerf", 49),
          ("swFwFOPPortTXPerf", 50),
          ("swFwFOPPortState", 51),
          ("swFwPerfALPACRC", 52),
          ("swFwPerfEToECRC", 53),
          ("swFwPerfEToERxCnt", 54),
          ("swFwPerfEToETxCnt", 55),
          ("swFwPerffltCusDef", 56),
          ("swFwTransceiverVoltage", 57),
          ("swFwSecTelnetViolations", 58),
          ("swFwSecHTTPViolations", 59),
          ("swFwSecAPIViolations", 60),
          ("swFwSecRSNMPViolations", 61),
          ("swFwSecWSNMPViolations", 62),
          ("swFwSecSESViolations", 63),
          ("swFwSecMSViolations", 64),
          ("swFwSecSerialViolations", 65),
          ("swFwSecFPViolations", 66),
          ("swFwSecSCCViolations", 67),
          ("swFwSecDCCViolations", 68),
          ("swFwSecLoginViolations", 69),
          ("swFwSecInvaledTS", 70),
          ("swFwSecInvalidSign", 71),
          ("swFwSecInvalidCert", 72),
          ("swFwSecSlapFail", 73),
          ("swFwSecSlapBadPkt", 74),
          ("swFwSecTSOutSync", 75),
          ("swFwSecNoFcs", 76),
          ("swFwSecIncompDB", 77),
          ("swFwSecIllegalCmd", 78),
          ("swFwSAMTotalDownTime", 79),
          ("swFwSAMTotalUpTime", 80),
          ("swFwSAMDurationOfOccur", 81),
          ("swFwSAMFreqOfOccur", 82),
          ("swFwResourceFlash", 83),
          ("swFwEPortUtil", 84),
          ("swFwEPortPktl", 85))
    )





class SwFwWriteVals(Integer32):
    """Custom type SwFwWriteVals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swFwCancelWrite", 1),
          ("swFwApplyWrite", 2))
    )





class SwFwTimebase(Integer32):
    """Custom type SwFwTimebase based on Integer32"""
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
        *(("swFwTbNone", 1),
          ("swFwTbSec", 2),
          ("swFwTbMin", 3),
          ("swFwTbHour", 4),
          ("swFwTbDay", 5))
    )





class SwFwStatus(Integer32):
    """Custom type SwFwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class SwFwEvent(Integer32):
    """Custom type SwFwEvent based on Integer32"""
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
        *(("started", 1),
          ("changed", 2),
          ("exceeded", 3),
          ("below", 4),
          ("above", 5),
          ("inBetween", 6))
    )





class SwFwBehavior(Integer32):
    """Custom type SwFwBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("triggered", 1),
          ("continuous", 2))
    )





class SwFwState(Integer32):
    """Custom type SwFwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swFwInformative", 1),
          ("swFwNormal", 2),
          ("swFwFaulty", 3))
    )





class SwFwLicense(Integer32):
    """Custom type SwFwLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swFwLicensed", 1),
          ("swFwNotLicensed", 2))
    )




# TEXTUAL-CONVENTIONS



class SwSevType(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )



class FcPortFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("virtual", 0)
    )


# MIB Managed Objects in the order of their OIDs

_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sw.setStatus("current")
_SwTrapsV2_ObjectIdentity = ObjectIdentity
swTrapsV2 = _SwTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    swTrapsV2.setStatus("current")
_SwSystem_ObjectIdentity = ObjectIdentity
swSystem = _SwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    swSystem.setStatus("current")


class _SwCurrentDate_Type(DisplayString):
    """Custom type swCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwCurrentDate_Type.__name__ = "DisplayString"
_SwCurrentDate_Object = MibScalar
swCurrentDate = _SwCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 1),
    _SwCurrentDate_Type()
)
swCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentDate.setStatus("current")


class _SwBootDate_Type(DisplayString):
    """Custom type swBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootDate_Type.__name__ = "DisplayString"
_SwBootDate_Object = MibScalar
swBootDate = _SwBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 2),
    _SwBootDate_Type()
)
swBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootDate.setStatus("current")


class _SwFWLastUpdated_Type(DisplayString):
    """Custom type swFWLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFWLastUpdated_Type.__name__ = "DisplayString"
_SwFWLastUpdated_Object = MibScalar
swFWLastUpdated = _SwFWLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 3),
    _SwFWLastUpdated_Type()
)
swFWLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFWLastUpdated.setStatus("current")


class _SwFlashLastUpdated_Type(DisplayString):
    """Custom type swFlashLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashLastUpdated_Type.__name__ = "DisplayString"
_SwFlashLastUpdated_Object = MibScalar
swFlashLastUpdated = _SwFlashLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 4),
    _SwFlashLastUpdated_Type()
)
swFlashLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashLastUpdated.setStatus("current")


class _SwBootPromLastUpdated_Type(DisplayString):
    """Custom type swBootPromLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwBootPromLastUpdated_Type.__name__ = "DisplayString"
_SwBootPromLastUpdated_Object = MibScalar
swBootPromLastUpdated = _SwBootPromLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 5),
    _SwBootPromLastUpdated_Type()
)
swBootPromLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootPromLastUpdated.setStatus("current")


class _SwFirmwareVersion_Type(DisplayString):
    """Custom type swFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFirmwareVersion_Type.__name__ = "DisplayString"
_SwFirmwareVersion_Object = MibScalar
swFirmwareVersion = _SwFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 6),
    _SwFirmwareVersion_Type()
)
swFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVersion.setStatus("current")


class _SwOperStatus_Type(Integer32):
    """Custom type swOperStatus based on Integer32"""
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


_SwOperStatus_Type.__name__ = "Integer32"
_SwOperStatus_Object = MibScalar
swOperStatus = _SwOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 7),
    _SwOperStatus_Type()
)
swOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOperStatus.setStatus("current")


class _SwAdmStatus_Type(Integer32):
    """Custom type swAdmStatus based on Integer32"""
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
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4),
          ("reboot", 5),
          ("fastboot", 6),
          ("switchReboot", 7))
    )


_SwAdmStatus_Type.__name__ = "Integer32"
_SwAdmStatus_Object = MibScalar
swAdmStatus = _SwAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 8),
    _SwAdmStatus_Type()
)
swAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAdmStatus.setStatus("current")


class _SwTelnetShellAdmStatus_Type(Integer32):
    """Custom type swTelnetShellAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("terminated", 1))
    )


_SwTelnetShellAdmStatus_Type.__name__ = "Integer32"
_SwTelnetShellAdmStatus_Object = MibScalar
swTelnetShellAdmStatus = _SwTelnetShellAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 9),
    _SwTelnetShellAdmStatus_Type()
)
swTelnetShellAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swTelnetShellAdmStatus.setStatus("current")


class _SwSsn_Type(DisplayString):
    """Custom type swSsn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwSsn_Type.__name__ = "DisplayString"
_SwSsn_Object = MibScalar
swSsn = _SwSsn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 10),
    _SwSsn_Type()
)
swSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSsn.setStatus("current")


class _SwFlashDLOperStatus_Type(Integer32):
    """Custom type swFlashDLOperStatus based on Integer32"""
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
        *(("unknown", 0),
          ("swCurrent", 1),
          ("swFwUpgraded", 2),
          ("swCfUploaded", 3),
          ("swCfDownloaded", 4),
          ("swFwCorrupted", 5))
    )


_SwFlashDLOperStatus_Type.__name__ = "Integer32"
_SwFlashDLOperStatus_Object = MibScalar
swFlashDLOperStatus = _SwFlashDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 11),
    _SwFlashDLOperStatus_Type()
)
swFlashDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashDLOperStatus.setStatus("current")


class _SwFlashDLAdmStatus_Type(Integer32):
    """Custom type swFlashDLAdmStatus based on Integer32"""
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
        *(("swCurrent", 1),
          ("swFwUpgrade", 2),
          ("swCfUpload", 3),
          ("swCfDownload", 4),
          ("swFwCorrupted", 5))
    )


_SwFlashDLAdmStatus_Type.__name__ = "Integer32"
_SwFlashDLAdmStatus_Object = MibScalar
swFlashDLAdmStatus = _SwFlashDLAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 12),
    _SwFlashDLAdmStatus_Type()
)
swFlashDLAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLAdmStatus.setStatus("current")


class _SwFlashDLHost_Type(DisplayString):
    """Custom type swFlashDLHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashDLHost_Type.__name__ = "DisplayString"
_SwFlashDLHost_Object = MibScalar
swFlashDLHost = _SwFlashDLHost_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 13),
    _SwFlashDLHost_Type()
)
swFlashDLHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLHost.setStatus("current")


class _SwFlashDLUser_Type(DisplayString):
    """Custom type swFlashDLUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwFlashDLUser_Type.__name__ = "DisplayString"
_SwFlashDLUser_Object = MibScalar
swFlashDLUser = _SwFlashDLUser_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 14),
    _SwFlashDLUser_Type()
)
swFlashDLUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLUser.setStatus("current")
_SwFlashDLFile_Type = DisplayString
_SwFlashDLFile_Object = MibScalar
swFlashDLFile = _SwFlashDLFile_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 15),
    _SwFlashDLFile_Type()
)
swFlashDLFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLFile.setStatus("current")


class _SwFlashDLPassword_Type(DisplayString):
    """Custom type swFlashDLPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwFlashDLPassword_Type.__name__ = "DisplayString"
_SwFlashDLPassword_Object = MibScalar
swFlashDLPassword = _SwFlashDLPassword_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 16),
    _SwFlashDLPassword_Type()
)
swFlashDLPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLPassword.setStatus("current")


class _SwBeaconOperStatus_Type(Integer32):
    """Custom type swBeaconOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconOperStatus_Type.__name__ = "Integer32"
_SwBeaconOperStatus_Object = MibScalar
swBeaconOperStatus = _SwBeaconOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 18),
    _SwBeaconOperStatus_Type()
)
swBeaconOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBeaconOperStatus.setStatus("current")


class _SwBeaconAdmStatus_Type(Integer32):
    """Custom type swBeaconAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_SwBeaconAdmStatus_Type.__name__ = "Integer32"
_SwBeaconAdmStatus_Object = MibScalar
swBeaconAdmStatus = _SwBeaconAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 19),
    _SwBeaconAdmStatus_Type()
)
swBeaconAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBeaconAdmStatus.setStatus("current")


class _SwDiagResult_Type(Integer32):
    """Custom type swDiagResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sw-ok", 1),
          ("sw-faulty", 2),
          ("sw-embedded-port-fault", 3))
    )


_SwDiagResult_Type.__name__ = "Integer32"
_SwDiagResult_Object = MibScalar
swDiagResult = _SwDiagResult_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 20),
    _SwDiagResult_Type()
)
swDiagResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDiagResult.setStatus("current")


class _SwNumSensors_Type(Integer32):
    """Custom type swNumSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumSensors_Type.__name__ = "Integer32"
_SwNumSensors_Object = MibScalar
swNumSensors = _SwNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 21),
    _SwNumSensors_Type()
)
swNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumSensors.setStatus("current")
_SwSensorTable_Object = MibTable
swSensorTable = _SwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swSensorTable.setStatus("current")
_SwSensorEntry_Object = MibTableRow
swSensorEntry = _SwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1)
)
swSensorEntry.setIndexNames(
    (0, "SW57-MIB", "swSensorIndex"),
)
if mibBuilder.loadTexts:
    swSensorEntry.setStatus("current")
_SwSensorIndex_Type = SwSensorIndex
_SwSensorIndex_Object = MibTableColumn
swSensorIndex = _SwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 1),
    _SwSensorIndex_Type()
)
swSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorIndex.setStatus("current")


class _SwSensorType_Type(Integer32):
    """Custom type swSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("temperature", 1),
          ("fan", 2),
          ("power-supply", 3))
    )


_SwSensorType_Type.__name__ = "Integer32"
_SwSensorType_Object = MibTableColumn
swSensorType = _SwSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 2),
    _SwSensorType_Type()
)
swSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorType.setStatus("current")


class _SwSensorStatus_Type(Integer32):
    """Custom type swSensorStatus based on Integer32"""
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
          ("faulty", 2),
          ("below-min", 3),
          ("nominal", 4),
          ("above-max", 5),
          ("absent", 6))
    )


_SwSensorStatus_Type.__name__ = "Integer32"
_SwSensorStatus_Object = MibTableColumn
swSensorStatus = _SwSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 3),
    _SwSensorStatus_Type()
)
swSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorStatus.setStatus("current")
_SwSensorValue_Type = Integer32
_SwSensorValue_Object = MibTableColumn
swSensorValue = _SwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 4),
    _SwSensorValue_Type()
)
swSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorValue.setStatus("current")


class _SwSensorInfo_Type(DisplayString):
    """Custom type swSensorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwSensorInfo_Type.__name__ = "DisplayString"
_SwSensorInfo_Object = MibTableColumn
swSensorInfo = _SwSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 5),
    _SwSensorInfo_Type()
)
swSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorInfo.setStatus("current")
_SwTrackChangesInfo_Type = DisplayString
_SwTrackChangesInfo_Object = MibScalar
swTrackChangesInfo = _SwTrackChangesInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 23),
    _SwTrackChangesInfo_Type()
)
swTrackChangesInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrackChangesInfo.setStatus("current")
_SwID_Type = Integer32
_SwID_Object = MibScalar
swID = _SwID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 24),
    _SwID_Type()
)
swID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swID.setStatus("current")
_SwEtherIPAddress_Type = IpAddress
_SwEtherIPAddress_Object = MibScalar
swEtherIPAddress = _SwEtherIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 25),
    _SwEtherIPAddress_Type()
)
swEtherIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPAddress.setStatus("current")
_SwEtherIPMask_Type = IpAddress
_SwEtherIPMask_Object = MibScalar
swEtherIPMask = _SwEtherIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 26),
    _SwEtherIPMask_Type()
)
swEtherIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEtherIPMask.setStatus("current")
_SwFCIPAddress_Type = IpAddress
_SwFCIPAddress_Object = MibScalar
swFCIPAddress = _SwFCIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 27),
    _SwFCIPAddress_Type()
)
swFCIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCIPAddress.setStatus("current")
_SwFCIPMask_Type = IpAddress
_SwFCIPMask_Object = MibScalar
swFCIPMask = _SwFCIPMask_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 28),
    _SwFCIPMask_Type()
)
swFCIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCIPMask.setStatus("current")
_SwFabric_ObjectIdentity = ObjectIdentity
swFabric = _SwFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    swFabric.setStatus("current")
_SwDomainID_Type = SwDomainIndex
_SwDomainID_Object = MibScalar
swDomainID = _SwDomainID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 1),
    _SwDomainID_Type()
)
swDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDomainID.setStatus("current")


class _SwPrincipalSwitch_Type(Integer32):
    """Custom type swPrincipalSwitch based on Integer32"""
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


_SwPrincipalSwitch_Type.__name__ = "Integer32"
_SwPrincipalSwitch_Object = MibScalar
swPrincipalSwitch = _SwPrincipalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 2),
    _SwPrincipalSwitch_Type()
)
swPrincipalSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPrincipalSwitch.setStatus("current")


class _SwNumNbs_Type(Integer32):
    """Custom type swNumNbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNumNbs_Type.__name__ = "Integer32"
_SwNumNbs_Object = MibScalar
swNumNbs = _SwNumNbs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 8),
    _SwNumNbs_Type()
)
swNumNbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumNbs.setStatus("current")
_SwNbTable_Object = MibTable
swNbTable = _SwNbTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    swNbTable.setStatus("current")
_SwNbEntry_Object = MibTableRow
swNbEntry = _SwNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1)
)
swNbEntry.setIndexNames(
    (0, "SW57-MIB", "swNbIndex"),
)
if mibBuilder.loadTexts:
    swNbEntry.setStatus("current")
_SwNbIndex_Type = SwNbIndex
_SwNbIndex_Object = MibTableColumn
swNbIndex = _SwNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 1),
    _SwNbIndex_Type()
)
swNbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbIndex.setStatus("current")
_SwNbMyPort_Type = SwPortIndex
_SwNbMyPort_Object = MibTableColumn
swNbMyPort = _SwNbMyPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 2),
    _SwNbMyPort_Type()
)
swNbMyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbMyPort.setStatus("current")
_SwNbRemDomain_Type = SwDomainIndex
_SwNbRemDomain_Object = MibTableColumn
swNbRemDomain = _SwNbRemDomain_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 3),
    _SwNbRemDomain_Type()
)
swNbRemDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemDomain.setStatus("current")
_SwNbRemPort_Type = SwPortIndex
_SwNbRemPort_Object = MibTableColumn
swNbRemPort = _SwNbRemPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 4),
    _SwNbRemPort_Type()
)
swNbRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemPort.setStatus("current")


class _SwNbBaudRate_Type(Integer32):
    """Custom type swNbBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("oneEighth", 2),
          ("quarter", 4),
          ("half", 8),
          ("full", 16),
          ("double", 32),
          ("quadruple", 64),
          ("octuple", 128),
          ("decuple", 256))
    )


_SwNbBaudRate_Type.__name__ = "Integer32"
_SwNbBaudRate_Object = MibTableColumn
swNbBaudRate = _SwNbBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 5),
    _SwNbBaudRate_Type()
)
swNbBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbBaudRate.setStatus("current")


class _SwNbIslState_Type(Integer32):
    """Custom type swNbIslState based on Integer32"""
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
        *(("sw-init", 1),
          ("sw-internal2", 2),
          ("sw-internal3", 3),
          ("sw-internal4", 4),
          ("sw-active", 5))
    )


_SwNbIslState_Type.__name__ = "Integer32"
_SwNbIslState_Object = MibTableColumn
swNbIslState = _SwNbIslState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 6),
    _SwNbIslState_Type()
)
swNbIslState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbIslState.setStatus("current")


class _SwNbIslCost_Type(Integer32):
    """Custom type swNbIslCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNbIslCost_Type.__name__ = "Integer32"
_SwNbIslCost_Object = MibTableColumn
swNbIslCost = _SwNbIslCost_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 7),
    _SwNbIslCost_Type()
)
swNbIslCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swNbIslCost.setStatus("current")


class _SwNbRemPortName_Type(OctetString):
    """Custom type swNbRemPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwNbRemPortName_Type.__name__ = "OctetString"
_SwNbRemPortName_Object = MibTableColumn
swNbRemPortName = _SwNbRemPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 8),
    _SwNbRemPortName_Type()
)
swNbRemPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemPortName.setStatus("current")
_SwFabricMemTable_Object = MibTable
swFabricMemTable = _SwFabricMemTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    swFabricMemTable.setStatus("current")
_SwFabricMemEntry_Object = MibTableRow
swFabricMemEntry = _SwFabricMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1)
)
swFabricMemEntry.setIndexNames(
    (0, "SW57-MIB", "swFabricMemWwn"),
)
if mibBuilder.loadTexts:
    swFabricMemEntry.setStatus("current")
_SwFabricMemWwn_Type = FcWwn
_SwFabricMemWwn_Object = MibTableColumn
swFabricMemWwn = _SwFabricMemWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 1),
    _SwFabricMemWwn_Type()
)
swFabricMemWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemWwn.setStatus("current")
_SwFabricMemDid_Type = SwDomainIndex
_SwFabricMemDid_Object = MibTableColumn
swFabricMemDid = _SwFabricMemDid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 2),
    _SwFabricMemDid_Type()
)
swFabricMemDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemDid.setStatus("current")


class _SwFabricMemName_Type(DisplayString):
    """Custom type swFabricMemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwFabricMemName_Type.__name__ = "DisplayString"
_SwFabricMemName_Object = MibTableColumn
swFabricMemName = _SwFabricMemName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 3),
    _SwFabricMemName_Type()
)
swFabricMemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemName.setStatus("current")
_SwFabricMemEIP_Type = IpAddress
_SwFabricMemEIP_Object = MibTableColumn
swFabricMemEIP = _SwFabricMemEIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 4),
    _SwFabricMemEIP_Type()
)
swFabricMemEIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemEIP.setStatus("current")
_SwFabricMemFCIP_Type = IpAddress
_SwFabricMemFCIP_Object = MibTableColumn
swFabricMemFCIP = _SwFabricMemFCIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 5),
    _SwFabricMemFCIP_Type()
)
swFabricMemFCIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemFCIP.setStatus("current")
_SwFabricMemGWIP_Type = IpAddress
_SwFabricMemGWIP_Object = MibTableColumn
swFabricMemGWIP = _SwFabricMemGWIP_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 6),
    _SwFabricMemGWIP_Type()
)
swFabricMemGWIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemGWIP.setStatus("current")


class _SwFabricMemType_Type(Integer32):
    """Custom type swFabricMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFabricMemType_Type.__name__ = "Integer32"
_SwFabricMemType_Object = MibTableColumn
swFabricMemType = _SwFabricMemType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 7),
    _SwFabricMemType_Type()
)
swFabricMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemType.setStatus("current")


class _SwFabricMemShortVersion_Type(OctetString):
    """Custom type swFabricMemShortVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SwFabricMemShortVersion_Type.__name__ = "OctetString"
_SwFabricMemShortVersion_Object = MibTableColumn
swFabricMemShortVersion = _SwFabricMemShortVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 10, 1, 8),
    _SwFabricMemShortVersion_Type()
)
swFabricMemShortVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFabricMemShortVersion.setStatus("current")


class _SwIDIDMode_Type(Integer32):
    """Custom type swIDIDMode based on Integer32"""
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


_SwIDIDMode_Type.__name__ = "Integer32"
_SwIDIDMode_Object = MibScalar
swIDIDMode = _SwIDIDMode_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 11),
    _SwIDIDMode_Type()
)
swIDIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIDIDMode.setStatus("current")
_SwModule_ObjectIdentity = ObjectIdentity
swModule = _SwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    swModule.setStatus("current")
_SwAgtCfg_ObjectIdentity = ObjectIdentity
swAgtCfg = _SwAgtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    swAgtCfg.setStatus("current")
_SwAgtCmtyTable_Object = MibTable
swAgtCmtyTable = _SwAgtCmtyTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    swAgtCmtyTable.setStatus("current")
_SwAgtCmtyEntry_Object = MibTableRow
swAgtCmtyEntry = _SwAgtCmtyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1)
)
swAgtCmtyEntry.setIndexNames(
    (0, "SW57-MIB", "swAgtCmtyIdx"),
)
if mibBuilder.loadTexts:
    swAgtCmtyEntry.setStatus("current")


class _SwAgtCmtyIdx_Type(Integer32):
    """Custom type swAgtCmtyIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SwAgtCmtyIdx_Type.__name__ = "Integer32"
_SwAgtCmtyIdx_Object = MibTableColumn
swAgtCmtyIdx = _SwAgtCmtyIdx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 1),
    _SwAgtCmtyIdx_Type()
)
swAgtCmtyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAgtCmtyIdx.setStatus("current")


class _SwAgtCmtyStr_Type(DisplayString):
    """Custom type swAgtCmtyStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_SwAgtCmtyStr_Type.__name__ = "DisplayString"
_SwAgtCmtyStr_Object = MibTableColumn
swAgtCmtyStr = _SwAgtCmtyStr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 2),
    _SwAgtCmtyStr_Type()
)
swAgtCmtyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtCmtyStr.setStatus("current")
_SwAgtTrapRcp_Type = IpAddress
_SwAgtTrapRcp_Object = MibTableColumn
swAgtTrapRcp = _SwAgtTrapRcp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 3),
    _SwAgtTrapRcp_Type()
)
swAgtTrapRcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtTrapRcp.setStatus("current")
_SwAgtTrapSeverityLevel_Type = SwSevType
_SwAgtTrapSeverityLevel_Object = MibTableColumn
swAgtTrapSeverityLevel = _SwAgtTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 4),
    _SwAgtTrapSeverityLevel_Type()
)
swAgtTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtTrapSeverityLevel.setStatus("current")
_SwFCport_ObjectIdentity = ObjectIdentity
swFCport = _SwFCport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    swFCport.setStatus("current")


class _SwFCPortCapacity_Type(Integer32):
    """Custom type swFCPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFCPortCapacity_Type.__name__ = "Integer32"
_SwFCPortCapacity_Object = MibScalar
swFCPortCapacity = _SwFCPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 1),
    _SwFCPortCapacity_Type()
)
swFCPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortCapacity.setStatus("current")
_SwFCPortTable_Object = MibTable
swFCPortTable = _SwFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    swFCPortTable.setStatus("current")
_SwFCPortEntry_Object = MibTableRow
swFCPortEntry = _SwFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1)
)
swFCPortEntry.setIndexNames(
    (0, "SW57-MIB", "swFCPortIndex"),
)
if mibBuilder.loadTexts:
    swFCPortEntry.setStatus("current")
_SwFCPortIndex_Type = SwPortIndex
_SwFCPortIndex_Object = MibTableColumn
swFCPortIndex = _SwFCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 1),
    _SwFCPortIndex_Type()
)
swFCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortIndex.setStatus("current")


class _SwFCPortType_Type(Integer32):
    """Custom type swFCPortType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("stitch", 1),
          ("flannel", 2),
          ("loom", 3),
          ("bloom", 4),
          ("rdbloom", 5),
          ("wormhole", 6),
          ("other", 7),
          ("unknown", 8))
    )


_SwFCPortType_Type.__name__ = "Integer32"
_SwFCPortType_Object = MibTableColumn
swFCPortType = _SwFCPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 2),
    _SwFCPortType_Type()
)
swFCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortType.setStatus("current")


class _SwFCPortPhyState_Type(Integer32):
    """Custom type swFCPortPhyState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noCard", 1),
          ("noTransceiver", 2),
          ("laserFault", 3),
          ("noLight", 4),
          ("noSync", 5),
          ("inSync", 6),
          ("portFault", 7),
          ("diagFault", 8),
          ("lockRef", 9))
    )


_SwFCPortPhyState_Type.__name__ = "Integer32"
_SwFCPortPhyState_Object = MibTableColumn
swFCPortPhyState = _SwFCPortPhyState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 3),
    _SwFCPortPhyState_Type()
)
swFCPortPhyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortPhyState.setStatus("current")


class _SwFCPortOpStatus_Type(Integer32):
    """Custom type swFCPortOpStatus based on Integer32"""
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
          ("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4))
    )


_SwFCPortOpStatus_Type.__name__ = "Integer32"
_SwFCPortOpStatus_Object = MibTableColumn
swFCPortOpStatus = _SwFCPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 4),
    _SwFCPortOpStatus_Type()
)
swFCPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortOpStatus.setStatus("current")


class _SwFCPortAdmStatus_Type(Integer32):
    """Custom type swFCPortAdmStatus based on Integer32"""
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


_SwFCPortAdmStatus_Type.__name__ = "Integer32"
_SwFCPortAdmStatus_Object = MibTableColumn
swFCPortAdmStatus = _SwFCPortAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 5),
    _SwFCPortAdmStatus_Type()
)
swFCPortAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortAdmStatus.setStatus("current")


class _SwFCPortLinkState_Type(Integer32):
    """Custom type swFCPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("loopback", 3))
    )


_SwFCPortLinkState_Type.__name__ = "Integer32"
_SwFCPortLinkState_Object = MibTableColumn
swFCPortLinkState = _SwFCPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 6),
    _SwFCPortLinkState_Type()
)
swFCPortLinkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortLinkState.setStatus("current")


class _SwFCPortTxType_Type(Integer32):
    """Custom type swFCPortTxType based on Integer32"""
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
          ("lw", 2),
          ("sw", 3),
          ("ld", 4),
          ("cu", 5))
    )


_SwFCPortTxType_Type.__name__ = "Integer32"
_SwFCPortTxType_Object = MibTableColumn
swFCPortTxType = _SwFCPortTxType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 7),
    _SwFCPortTxType_Type()
)
swFCPortTxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxType.setStatus("current")
_SwFCPortTxWords_Type = Counter32
_SwFCPortTxWords_Object = MibTableColumn
swFCPortTxWords = _SwFCPortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 11),
    _SwFCPortTxWords_Type()
)
swFCPortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxWords.setStatus("current")
_SwFCPortRxWords_Type = Counter32
_SwFCPortRxWords_Object = MibTableColumn
swFCPortRxWords = _SwFCPortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 12),
    _SwFCPortRxWords_Type()
)
swFCPortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxWords.setStatus("current")
_SwFCPortTxFrames_Type = Counter32
_SwFCPortTxFrames_Object = MibTableColumn
swFCPortTxFrames = _SwFCPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 13),
    _SwFCPortTxFrames_Type()
)
swFCPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxFrames.setStatus("current")
_SwFCPortRxFrames_Type = Counter32
_SwFCPortRxFrames_Object = MibTableColumn
swFCPortRxFrames = _SwFCPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 14),
    _SwFCPortRxFrames_Type()
)
swFCPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxFrames.setStatus("current")
_SwFCPortRxC2Frames_Type = Counter32
_SwFCPortRxC2Frames_Object = MibTableColumn
swFCPortRxC2Frames = _SwFCPortRxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 15),
    _SwFCPortRxC2Frames_Type()
)
swFCPortRxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC2Frames.setStatus("current")
_SwFCPortRxC3Frames_Type = Counter32
_SwFCPortRxC3Frames_Object = MibTableColumn
swFCPortRxC3Frames = _SwFCPortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 16),
    _SwFCPortRxC3Frames_Type()
)
swFCPortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC3Frames.setStatus("current")
_SwFCPortRxLCs_Type = Counter32
_SwFCPortRxLCs_Object = MibTableColumn
swFCPortRxLCs = _SwFCPortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 17),
    _SwFCPortRxLCs_Type()
)
swFCPortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxLCs.setStatus("current")
_SwFCPortRxMcasts_Type = Counter32
_SwFCPortRxMcasts_Object = MibTableColumn
swFCPortRxMcasts = _SwFCPortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 18),
    _SwFCPortRxMcasts_Type()
)
swFCPortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxMcasts.setStatus("current")
_SwFCPortTooManyRdys_Type = Counter32
_SwFCPortTooManyRdys_Object = MibTableColumn
swFCPortTooManyRdys = _SwFCPortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 19),
    _SwFCPortTooManyRdys_Type()
)
swFCPortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTooManyRdys.setStatus("current")
_SwFCPortNoTxCredits_Type = Counter32
_SwFCPortNoTxCredits_Object = MibTableColumn
swFCPortNoTxCredits = _SwFCPortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 20),
    _SwFCPortNoTxCredits_Type()
)
swFCPortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortNoTxCredits.setStatus("current")
_SwFCPortRxEncInFrs_Type = Counter32
_SwFCPortRxEncInFrs_Object = MibTableColumn
swFCPortRxEncInFrs = _SwFCPortRxEncInFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 21),
    _SwFCPortRxEncInFrs_Type()
)
swFCPortRxEncInFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncInFrs.setStatus("current")
_SwFCPortRxCrcs_Type = Counter32
_SwFCPortRxCrcs_Object = MibTableColumn
swFCPortRxCrcs = _SwFCPortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 22),
    _SwFCPortRxCrcs_Type()
)
swFCPortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxCrcs.setStatus("current")
_SwFCPortRxTruncs_Type = Counter32
_SwFCPortRxTruncs_Object = MibTableColumn
swFCPortRxTruncs = _SwFCPortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 23),
    _SwFCPortRxTruncs_Type()
)
swFCPortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTruncs.setStatus("current")
_SwFCPortRxTooLongs_Type = Counter32
_SwFCPortRxTooLongs_Object = MibTableColumn
swFCPortRxTooLongs = _SwFCPortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 24),
    _SwFCPortRxTooLongs_Type()
)
swFCPortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTooLongs.setStatus("current")
_SwFCPortRxBadEofs_Type = Counter32
_SwFCPortRxBadEofs_Object = MibTableColumn
swFCPortRxBadEofs = _SwFCPortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 25),
    _SwFCPortRxBadEofs_Type()
)
swFCPortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadEofs.setStatus("current")
_SwFCPortRxEncOutFrs_Type = Counter32
_SwFCPortRxEncOutFrs_Object = MibTableColumn
swFCPortRxEncOutFrs = _SwFCPortRxEncOutFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 26),
    _SwFCPortRxEncOutFrs_Type()
)
swFCPortRxEncOutFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncOutFrs.setStatus("current")
_SwFCPortRxBadOs_Type = Counter32
_SwFCPortRxBadOs_Object = MibTableColumn
swFCPortRxBadOs = _SwFCPortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 27),
    _SwFCPortRxBadOs_Type()
)
swFCPortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadOs.setStatus("current")
_SwFCPortC3Discards_Type = Counter32
_SwFCPortC3Discards_Object = MibTableColumn
swFCPortC3Discards = _SwFCPortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 28),
    _SwFCPortC3Discards_Type()
)
swFCPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortC3Discards.setStatus("current")
_SwFCPortMcastTimedOuts_Type = Counter32
_SwFCPortMcastTimedOuts_Object = MibTableColumn
swFCPortMcastTimedOuts = _SwFCPortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 29),
    _SwFCPortMcastTimedOuts_Type()
)
swFCPortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortMcastTimedOuts.setStatus("current")
_SwFCPortTxMcasts_Type = Counter32
_SwFCPortTxMcasts_Object = MibTableColumn
swFCPortTxMcasts = _SwFCPortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 30),
    _SwFCPortTxMcasts_Type()
)
swFCPortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxMcasts.setStatus("current")
_SwFCPortLipIns_Type = Counter32
_SwFCPortLipIns_Object = MibTableColumn
swFCPortLipIns = _SwFCPortLipIns_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 31),
    _SwFCPortLipIns_Type()
)
swFCPortLipIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipIns.setStatus("current")
_SwFCPortLipOuts_Type = Counter32
_SwFCPortLipOuts_Object = MibTableColumn
swFCPortLipOuts = _SwFCPortLipOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 32),
    _SwFCPortLipOuts_Type()
)
swFCPortLipOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipOuts.setStatus("current")


class _SwFCPortLipLastAlpa_Type(OctetString):
    """Custom type swFCPortLipLastAlpa based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwFCPortLipLastAlpa_Type.__name__ = "OctetString"
_SwFCPortLipLastAlpa_Object = MibTableColumn
swFCPortLipLastAlpa = _SwFCPortLipLastAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 33),
    _SwFCPortLipLastAlpa_Type()
)
swFCPortLipLastAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipLastAlpa.setStatus("current")


class _SwFCPortWwn_Type(OctetString):
    """Custom type swFCPortWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwFCPortWwn_Type.__name__ = "OctetString"
_SwFCPortWwn_Object = MibTableColumn
swFCPortWwn = _SwFCPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 34),
    _SwFCPortWwn_Type()
)
swFCPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortWwn.setStatus("current")


class _SwFCPortSpeed_Type(Integer32):
    """Custom type swFCPortSpeed based on Integer32"""
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
        *(("one-GB", 1),
          ("two-GB", 2),
          ("auto-Negotiate", 3),
          ("four-GB", 4),
          ("eight-GB", 5),
          ("ten-GB", 6))
    )


_SwFCPortSpeed_Type.__name__ = "Integer32"
_SwFCPortSpeed_Object = MibTableColumn
swFCPortSpeed = _SwFCPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 35),
    _SwFCPortSpeed_Type()
)
swFCPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFCPortSpeed.setStatus("current")


class _SwFCPortName_Type(DisplayString):
    """Custom type swFCPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFCPortName_Type.__name__ = "DisplayString"
_SwFCPortName_Object = MibTableColumn
swFCPortName = _SwFCPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 36),
    _SwFCPortName_Type()
)
swFCPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortName.setStatus("current")
_SwFCPortSpecifier_Type = DisplayString
_SwFCPortSpecifier_Object = MibTableColumn
swFCPortSpecifier = _SwFCPortSpecifier_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 37),
    _SwFCPortSpecifier_Type()
)
swFCPortSpecifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortSpecifier.setStatus("current")
_SwFCPortFlag_Type = FcPortFlag
_SwFCPortFlag_Object = MibTableColumn
swFCPortFlag = _SwFCPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 38),
    _SwFCPortFlag_Type()
)
swFCPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortFlag.setStatus("current")


class _SwFCPortBrcdType_Type(Integer32):
    """Custom type swFCPortBrcdType based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("fl-port", 3),
          ("f-port", 4),
          ("e-port", 5),
          ("g-port", 6),
          ("ex-port", 7))
    )


_SwFCPortBrcdType_Type.__name__ = "Integer32"
_SwFCPortBrcdType_Object = MibTableColumn
swFCPortBrcdType = _SwFCPortBrcdType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 39),
    _SwFCPortBrcdType_Type()
)
swFCPortBrcdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortBrcdType.setStatus("current")
_SwNs_ObjectIdentity = ObjectIdentity
swNs = _SwNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    swNs.setStatus("current")


class _SwNsLocalNumEntry_Type(Integer32):
    """Custom type swNsLocalNumEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNsLocalNumEntry_Type.__name__ = "Integer32"
_SwNsLocalNumEntry_Object = MibScalar
swNsLocalNumEntry = _SwNsLocalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 1),
    _SwNsLocalNumEntry_Type()
)
swNsLocalNumEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsLocalNumEntry.setStatus("current")
_SwNsLocalTable_Object = MibTable
swNsLocalTable = _SwNsLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    swNsLocalTable.setStatus("current")
_SwNsLocalEntry_Object = MibTableRow
swNsLocalEntry = _SwNsLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1)
)
swNsLocalEntry.setIndexNames(
    (0, "SW57-MIB", "swNsEntryIndex"),
)
if mibBuilder.loadTexts:
    swNsLocalEntry.setStatus("current")


class _SwNsEntryIndex_Type(Integer32):
    """Custom type swNsEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwNsEntryIndex_Type.__name__ = "Integer32"
_SwNsEntryIndex_Object = MibTableColumn
swNsEntryIndex = _SwNsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 1),
    _SwNsEntryIndex_Type()
)
swNsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsEntryIndex.setStatus("current")


class _SwNsPortID_Type(OctetString):
    """Custom type swNsPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwNsPortID_Type.__name__ = "OctetString"
_SwNsPortID_Object = MibTableColumn
swNsPortID = _SwNsPortID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 2),
    _SwNsPortID_Type()
)
swNsPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortID.setStatus("current")


class _SwNsPortType_Type(Integer32):
    """Custom type swNsPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nPort", 1),
          ("nlPort", 2))
    )


_SwNsPortType_Type.__name__ = "Integer32"
_SwNsPortType_Object = MibTableColumn
swNsPortType = _SwNsPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 3),
    _SwNsPortType_Type()
)
swNsPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortType.setStatus("current")
_SwNsPortName_Type = FcWwn
_SwNsPortName_Object = MibTableColumn
swNsPortName = _SwNsPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 4),
    _SwNsPortName_Type()
)
swNsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortName.setStatus("current")


class _SwNsPortSymb_Type(OctetString):
    """Custom type swNsPortSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwNsPortSymb_Type.__name__ = "OctetString"
_SwNsPortSymb_Object = MibTableColumn
swNsPortSymb = _SwNsPortSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 5),
    _SwNsPortSymb_Type()
)
swNsPortSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortSymb.setStatus("current")
_SwNsNodeName_Type = FcWwn
_SwNsNodeName_Object = MibTableColumn
swNsNodeName = _SwNsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 6),
    _SwNsNodeName_Type()
)
swNsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeName.setStatus("current")


class _SwNsNodeSymb_Type(OctetString):
    """Custom type swNsNodeSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwNsNodeSymb_Type.__name__ = "OctetString"
_SwNsNodeSymb_Object = MibTableColumn
swNsNodeSymb = _SwNsNodeSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 7),
    _SwNsNodeSymb_Type()
)
swNsNodeSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeSymb.setStatus("current")


class _SwNsIPA_Type(OctetString):
    """Custom type swNsIPA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwNsIPA_Type.__name__ = "OctetString"
_SwNsIPA_Object = MibTableColumn
swNsIPA = _SwNsIPA_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 8),
    _SwNsIPA_Type()
)
swNsIPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIPA.setStatus("current")


class _SwNsIpAddress_Type(OctetString):
    """Custom type swNsIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SwNsIpAddress_Type.__name__ = "OctetString"
_SwNsIpAddress_Object = MibTableColumn
swNsIpAddress = _SwNsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 9),
    _SwNsIpAddress_Type()
)
swNsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIpAddress.setStatus("current")


class _SwNsCos_Type(Integer32):
    """Custom type swNsCos based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("class-F", 1),
          ("class-1", 2),
          ("class-F-1", 3),
          ("class-2", 4),
          ("class-F-2", 5),
          ("class-1-2", 6),
          ("class-F-1-2", 7),
          ("class-3", 8),
          ("class-F-3", 9),
          ("class-1-3", 10),
          ("class-F-1-3", 11),
          ("class-2-3", 12),
          ("class-F-2-3", 13),
          ("class-1-2-3", 14),
          ("class-F-1-2-3", 15))
    )


_SwNsCos_Type.__name__ = "Integer32"
_SwNsCos_Object = MibTableColumn
swNsCos = _SwNsCos_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 10),
    _SwNsCos_Type()
)
swNsCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsCos.setStatus("current")


class _SwNsFc4_Type(OctetString):
    """Custom type swNsFc4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_SwNsFc4_Type.__name__ = "OctetString"
_SwNsFc4_Object = MibTableColumn
swNsFc4 = _SwNsFc4_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 11),
    _SwNsFc4_Type()
)
swNsFc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsFc4.setStatus("current")


class _SwNsIpNxPort_Type(OctetString):
    """Custom type swNsIpNxPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SwNsIpNxPort_Type.__name__ = "OctetString"
_SwNsIpNxPort_Object = MibTableColumn
swNsIpNxPort = _SwNsIpNxPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 12),
    _SwNsIpNxPort_Type()
)
swNsIpNxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsIpNxPort.setStatus("current")


class _SwNsWwn_Type(OctetString):
    """Custom type swNsWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwNsWwn_Type.__name__ = "OctetString"
_SwNsWwn_Object = MibTableColumn
swNsWwn = _SwNsWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 13),
    _SwNsWwn_Type()
)
swNsWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsWwn.setStatus("current")


class _SwNsHardAddr_Type(OctetString):
    """Custom type swNsHardAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_SwNsHardAddr_Type.__name__ = "OctetString"
_SwNsHardAddr_Object = MibTableColumn
swNsHardAddr = _SwNsHardAddr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 14),
    _SwNsHardAddr_Type()
)
swNsHardAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsHardAddr.setStatus("current")
_SwEvent_ObjectIdentity = ObjectIdentity
swEvent = _SwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swEvent.setStatus("current")


class _SwEventTrapLevel_Type(Integer32):
    """Custom type swEventTrapLevel based on Integer32"""
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
        *(("none", 0),
          ("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SwEventTrapLevel_Type.__name__ = "Integer32"
_SwEventTrapLevel_Object = MibScalar
swEventTrapLevel = _SwEventTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 1),
    _SwEventTrapLevel_Type()
)
swEventTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEventTrapLevel.setStatus("deprecated")


class _SwEventNumEntries_Type(Integer32):
    """Custom type swEventNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventNumEntries_Type.__name__ = "Integer32"
_SwEventNumEntries_Object = MibScalar
swEventNumEntries = _SwEventNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 4),
    _SwEventNumEntries_Type()
)
swEventNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventNumEntries.setStatus("current")
_SwEventTable_Object = MibTable
swEventTable = _SwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    swEventTable.setStatus("current")
_SwEventEntry_Object = MibTableRow
swEventEntry = _SwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1)
)
swEventEntry.setIndexNames(
    (0, "SW57-MIB", "swEventIndex"),
)
if mibBuilder.loadTexts:
    swEventEntry.setStatus("current")


class _SwEventIndex_Type(Integer32):
    """Custom type swEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventIndex_Type.__name__ = "Integer32"
_SwEventIndex_Object = MibTableColumn
swEventIndex = _SwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 1),
    _SwEventIndex_Type()
)
swEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventIndex.setStatus("current")


class _SwEventTimeInfo_Type(DisplayString):
    """Custom type swEventTimeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwEventTimeInfo_Type.__name__ = "DisplayString"
_SwEventTimeInfo_Object = MibTableColumn
swEventTimeInfo = _SwEventTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 2),
    _SwEventTimeInfo_Type()
)
swEventTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventTimeInfo.setStatus("current")


class _SwEventLevel_Type(Integer32):
    """Custom type swEventLevel based on Integer32"""
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
        *(("critical", 1),
          ("error", 2),
          ("warning", 3),
          ("informational", 4),
          ("debug", 5))
    )


_SwEventLevel_Type.__name__ = "Integer32"
_SwEventLevel_Object = MibTableColumn
swEventLevel = _SwEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 3),
    _SwEventLevel_Type()
)
swEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventLevel.setStatus("current")


class _SwEventRepeatCount_Type(Integer32):
    """Custom type swEventRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEventRepeatCount_Type.__name__ = "Integer32"
_SwEventRepeatCount_Object = MibTableColumn
swEventRepeatCount = _SwEventRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 4),
    _SwEventRepeatCount_Type()
)
swEventRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventRepeatCount.setStatus("current")
_SwEventDescr_Type = DisplayString
_SwEventDescr_Object = MibTableColumn
swEventDescr = _SwEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 5),
    _SwEventDescr_Type()
)
swEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventDescr.setStatus("current")
_SwFwSystem_ObjectIdentity = ObjectIdentity
swFwSystem = _SwFwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    swFwSystem.setStatus("current")
_SwFwFabricWatchLicense_Type = SwFwLicense
_SwFwFabricWatchLicense_Object = MibScalar
swFwFabricWatchLicense = _SwFwFabricWatchLicense_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 1),
    _SwFwFabricWatchLicense_Type()
)
swFwFabricWatchLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwFabricWatchLicense.setStatus("current")
_SwFwClassAreaTable_Object = MibTable
swFwClassAreaTable = _SwFwClassAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    swFwClassAreaTable.setStatus("current")
_SwFwClassAreaEntry_Object = MibTableRow
swFwClassAreaEntry = _SwFwClassAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1)
)
swFwClassAreaEntry.setIndexNames(
    (0, "SW57-MIB", "swFwClassAreaIndex"),
)
if mibBuilder.loadTexts:
    swFwClassAreaEntry.setStatus("current")
_SwFwClassAreaIndex_Type = SwFwClassesAreas
_SwFwClassAreaIndex_Object = MibTableColumn
swFwClassAreaIndex = _SwFwClassAreaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 1),
    _SwFwClassAreaIndex_Type()
)
swFwClassAreaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwClassAreaIndex.setStatus("current")
_SwFwWriteThVals_Type = SwFwWriteVals
_SwFwWriteThVals_Object = MibTableColumn
swFwWriteThVals = _SwFwWriteThVals_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 2),
    _SwFwWriteThVals_Type()
)
swFwWriteThVals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwWriteThVals.setStatus("current")
_SwFwDefaultUnit_Type = DisplayString
_SwFwDefaultUnit_Object = MibTableColumn
swFwDefaultUnit = _SwFwDefaultUnit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 3),
    _SwFwDefaultUnit_Type()
)
swFwDefaultUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultUnit.setStatus("current")
_SwFwDefaultTimebase_Type = SwFwTimebase
_SwFwDefaultTimebase_Object = MibTableColumn
swFwDefaultTimebase = _SwFwDefaultTimebase_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 4),
    _SwFwDefaultTimebase_Type()
)
swFwDefaultTimebase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultTimebase.setStatus("current")


class _SwFwDefaultLow_Type(Integer32):
    """Custom type swFwDefaultLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultLow_Type.__name__ = "Integer32"
_SwFwDefaultLow_Object = MibTableColumn
swFwDefaultLow = _SwFwDefaultLow_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 5),
    _SwFwDefaultLow_Type()
)
swFwDefaultLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultLow.setStatus("current")


class _SwFwDefaultHigh_Type(Integer32):
    """Custom type swFwDefaultHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultHigh_Type.__name__ = "Integer32"
_SwFwDefaultHigh_Object = MibTableColumn
swFwDefaultHigh = _SwFwDefaultHigh_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 6),
    _SwFwDefaultHigh_Type()
)
swFwDefaultHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultHigh.setStatus("current")


class _SwFwDefaultBufSize_Type(Integer32):
    """Custom type swFwDefaultBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwDefaultBufSize_Type.__name__ = "Integer32"
_SwFwDefaultBufSize_Object = MibTableColumn
swFwDefaultBufSize = _SwFwDefaultBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 7),
    _SwFwDefaultBufSize_Type()
)
swFwDefaultBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultBufSize.setStatus("current")
_SwFwCustUnit_Type = DisplayString
_SwFwCustUnit_Object = MibTableColumn
swFwCustUnit = _SwFwCustUnit_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 8),
    _SwFwCustUnit_Type()
)
swFwCustUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustUnit.setStatus("current")
_SwFwCustTimebase_Type = SwFwTimebase
_SwFwCustTimebase_Object = MibTableColumn
swFwCustTimebase = _SwFwCustTimebase_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 9),
    _SwFwCustTimebase_Type()
)
swFwCustTimebase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustTimebase.setStatus("current")


class _SwFwCustLow_Type(Integer32):
    """Custom type swFwCustLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustLow_Type.__name__ = "Integer32"
_SwFwCustLow_Object = MibTableColumn
swFwCustLow = _SwFwCustLow_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 10),
    _SwFwCustLow_Type()
)
swFwCustLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustLow.setStatus("current")


class _SwFwCustHigh_Type(Integer32):
    """Custom type swFwCustHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustHigh_Type.__name__ = "Integer32"
_SwFwCustHigh_Object = MibTableColumn
swFwCustHigh = _SwFwCustHigh_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 11),
    _SwFwCustHigh_Type()
)
swFwCustHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustHigh.setStatus("current")


class _SwFwCustBufSize_Type(Integer32):
    """Custom type swFwCustBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCustBufSize_Type.__name__ = "Integer32"
_SwFwCustBufSize_Object = MibTableColumn
swFwCustBufSize = _SwFwCustBufSize_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 12),
    _SwFwCustBufSize_Type()
)
swFwCustBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustBufSize.setStatus("current")
_SwFwThLevel_Type = SwFwLevels
_SwFwThLevel_Object = MibTableColumn
swFwThLevel = _SwFwThLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 13),
    _SwFwThLevel_Type()
)
swFwThLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwThLevel.setStatus("current")
_SwFwWriteActVals_Type = SwFwWriteVals
_SwFwWriteActVals_Object = MibTableColumn
swFwWriteActVals = _SwFwWriteActVals_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 14),
    _SwFwWriteActVals_Type()
)
swFwWriteActVals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwWriteActVals.setStatus("current")
_SwFwDefaultChangedActs_Type = SwFwActs
_SwFwDefaultChangedActs_Object = MibTableColumn
swFwDefaultChangedActs = _SwFwDefaultChangedActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 15),
    _SwFwDefaultChangedActs_Type()
)
swFwDefaultChangedActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultChangedActs.setStatus("current")
_SwFwDefaultExceededActs_Type = SwFwActs
_SwFwDefaultExceededActs_Object = MibTableColumn
swFwDefaultExceededActs = _SwFwDefaultExceededActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 16),
    _SwFwDefaultExceededActs_Type()
)
swFwDefaultExceededActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultExceededActs.setStatus("current")
_SwFwDefaultBelowActs_Type = SwFwActs
_SwFwDefaultBelowActs_Object = MibTableColumn
swFwDefaultBelowActs = _SwFwDefaultBelowActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 17),
    _SwFwDefaultBelowActs_Type()
)
swFwDefaultBelowActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultBelowActs.setStatus("current")
_SwFwDefaultAboveActs_Type = SwFwActs
_SwFwDefaultAboveActs_Object = MibTableColumn
swFwDefaultAboveActs = _SwFwDefaultAboveActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 18),
    _SwFwDefaultAboveActs_Type()
)
swFwDefaultAboveActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultAboveActs.setStatus("current")
_SwFwDefaultInBetweenActs_Type = SwFwActs
_SwFwDefaultInBetweenActs_Object = MibTableColumn
swFwDefaultInBetweenActs = _SwFwDefaultInBetweenActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 19),
    _SwFwDefaultInBetweenActs_Type()
)
swFwDefaultInBetweenActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwDefaultInBetweenActs.setStatus("current")
_SwFwCustChangedActs_Type = SwFwActs
_SwFwCustChangedActs_Object = MibTableColumn
swFwCustChangedActs = _SwFwCustChangedActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 20),
    _SwFwCustChangedActs_Type()
)
swFwCustChangedActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustChangedActs.setStatus("current")
_SwFwCustExceededActs_Type = SwFwActs
_SwFwCustExceededActs_Object = MibTableColumn
swFwCustExceededActs = _SwFwCustExceededActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 21),
    _SwFwCustExceededActs_Type()
)
swFwCustExceededActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustExceededActs.setStatus("current")
_SwFwCustBelowActs_Type = SwFwActs
_SwFwCustBelowActs_Object = MibTableColumn
swFwCustBelowActs = _SwFwCustBelowActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 22),
    _SwFwCustBelowActs_Type()
)
swFwCustBelowActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustBelowActs.setStatus("current")
_SwFwCustAboveActs_Type = SwFwActs
_SwFwCustAboveActs_Object = MibTableColumn
swFwCustAboveActs = _SwFwCustAboveActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 23),
    _SwFwCustAboveActs_Type()
)
swFwCustAboveActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustAboveActs.setStatus("current")
_SwFwCustInBetweenActs_Type = SwFwActs
_SwFwCustInBetweenActs_Object = MibTableColumn
swFwCustInBetweenActs = _SwFwCustInBetweenActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 24),
    _SwFwCustInBetweenActs_Type()
)
swFwCustInBetweenActs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwCustInBetweenActs.setStatus("current")
_SwFwValidActs_Type = SwFwActs
_SwFwValidActs_Object = MibTableColumn
swFwValidActs = _SwFwValidActs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 25),
    _SwFwValidActs_Type()
)
swFwValidActs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwValidActs.setStatus("current")
_SwFwActLevel_Type = SwFwLevels
_SwFwActLevel_Object = MibTableColumn
swFwActLevel = _SwFwActLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 2, 1, 26),
    _SwFwActLevel_Type()
)
swFwActLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwActLevel.setStatus("current")
_SwFwThresholdTable_Object = MibTable
swFwThresholdTable = _SwFwThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    swFwThresholdTable.setStatus("current")
_SwFwThresholdEntry_Object = MibTableRow
swFwThresholdEntry = _SwFwThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1)
)
swFwThresholdEntry.setIndexNames(
    (0, "SW57-MIB", "swFwClassAreaIndex"),
    (0, "SW57-MIB", "swFwThresholdIndex"),
)
if mibBuilder.loadTexts:
    swFwThresholdEntry.setStatus("current")


class _SwFwThresholdIndex_Type(Integer32):
    """Custom type swFwThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwThresholdIndex_Type.__name__ = "Integer32"
_SwFwThresholdIndex_Object = MibTableColumn
swFwThresholdIndex = _SwFwThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 1),
    _SwFwThresholdIndex_Type()
)
swFwThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwThresholdIndex.setStatus("current")
_SwFwStatus_Type = SwFwStatus
_SwFwStatus_Object = MibTableColumn
swFwStatus = _SwFwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 2),
    _SwFwStatus_Type()
)
swFwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwStatus.setStatus("current")


class _SwFwName_Type(DisplayString):
    """Custom type swFwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFwName_Type.__name__ = "DisplayString"
_SwFwName_Object = MibTableColumn
swFwName = _SwFwName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 3),
    _SwFwName_Type()
)
swFwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwName.setStatus("current")


class _SwFwLabel_Type(DisplayString):
    """Custom type swFwLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_SwFwLabel_Type.__name__ = "DisplayString"
_SwFwLabel_Object = MibTableColumn
swFwLabel = _SwFwLabel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 4),
    _SwFwLabel_Type()
)
swFwLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLabel.setStatus("current")


class _SwFwCurVal_Type(Integer32):
    """Custom type swFwCurVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwCurVal_Type.__name__ = "Integer32"
_SwFwCurVal_Object = MibTableColumn
swFwCurVal = _SwFwCurVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 5),
    _SwFwCurVal_Type()
)
swFwCurVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwCurVal.setStatus("current")
_SwFwLastEvent_Type = SwFwEvent
_SwFwLastEvent_Object = MibTableColumn
swFwLastEvent = _SwFwLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 6),
    _SwFwLastEvent_Type()
)
swFwLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEvent.setStatus("current")


class _SwFwLastEventVal_Type(Integer32):
    """Custom type swFwLastEventVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwLastEventVal_Type.__name__ = "Integer32"
_SwFwLastEventVal_Object = MibTableColumn
swFwLastEventVal = _SwFwLastEventVal_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 7),
    _SwFwLastEventVal_Type()
)
swFwLastEventVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEventVal.setStatus("current")


class _SwFwLastEventTime_Type(DisplayString):
    """Custom type swFwLastEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwFwLastEventTime_Type.__name__ = "DisplayString"
_SwFwLastEventTime_Object = MibTableColumn
swFwLastEventTime = _SwFwLastEventTime_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 8),
    _SwFwLastEventTime_Type()
)
swFwLastEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastEventTime.setStatus("current")
_SwFwLastState_Type = SwFwState
_SwFwLastState_Object = MibTableColumn
swFwLastState = _SwFwLastState_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 9),
    _SwFwLastState_Type()
)
swFwLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastState.setStatus("current")
_SwFwBehaviorType_Type = SwFwBehavior
_SwFwBehaviorType_Object = MibTableColumn
swFwBehaviorType = _SwFwBehaviorType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 10),
    _SwFwBehaviorType_Type()
)
swFwBehaviorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwBehaviorType.setStatus("current")


class _SwFwBehaviorInt_Type(Integer32):
    """Custom type swFwBehaviorInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwFwBehaviorInt_Type.__name__ = "Integer32"
_SwFwBehaviorInt_Object = MibTableColumn
swFwBehaviorInt = _SwFwBehaviorInt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 11),
    _SwFwBehaviorInt_Type()
)
swFwBehaviorInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFwBehaviorInt.setStatus("current")
_SwFwLastSeverityLevel_Type = SwSevType
_SwFwLastSeverityLevel_Object = MibTableColumn
swFwLastSeverityLevel = _SwFwLastSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 10, 3, 1, 12),
    _SwFwLastSeverityLevel_Type()
)
swFwLastSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFwLastSeverityLevel.setStatus("current")
_SwEndDevice_ObjectIdentity = ObjectIdentity
swEndDevice = _SwEndDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    swEndDevice.setStatus("current")
_SwEndDeviceRlsTable_Object = MibTable
swEndDeviceRlsTable = _SwEndDeviceRlsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1)
)
if mibBuilder.loadTexts:
    swEndDeviceRlsTable.setStatus("current")
_SwEndDeviceRlsEntry_Object = MibTableRow
swEndDeviceRlsEntry = _SwEndDeviceRlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1)
)
swEndDeviceRlsEntry.setIndexNames(
    (0, "SW57-MIB", "swEndDevicePort"),
    (0, "SW57-MIB", "swEndDeviceAlpa"),
)
if mibBuilder.loadTexts:
    swEndDeviceRlsEntry.setStatus("current")


class _SwEndDevicePort_Type(Integer32):
    """Custom type swEndDevicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDevicePort_Type.__name__ = "Integer32"
_SwEndDevicePort_Object = MibTableColumn
swEndDevicePort = _SwEndDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 1),
    _SwEndDevicePort_Type()
)
swEndDevicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEndDevicePort.setStatus("current")


class _SwEndDeviceAlpa_Type(Integer32):
    """Custom type swEndDeviceAlpa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceAlpa_Type.__name__ = "Integer32"
_SwEndDeviceAlpa_Object = MibTableColumn
swEndDeviceAlpa = _SwEndDeviceAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 2),
    _SwEndDeviceAlpa_Type()
)
swEndDeviceAlpa.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swEndDeviceAlpa.setStatus("current")


class _SwEndDevicePortID_Type(OctetString):
    """Custom type swEndDevicePortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwEndDevicePortID_Type.__name__ = "OctetString"
_SwEndDevicePortID_Object = MibTableColumn
swEndDevicePortID = _SwEndDevicePortID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 3),
    _SwEndDevicePortID_Type()
)
swEndDevicePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDevicePortID.setStatus("current")


class _SwEndDeviceLinkFailure_Type(Integer32):
    """Custom type swEndDeviceLinkFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceLinkFailure_Type.__name__ = "Integer32"
_SwEndDeviceLinkFailure_Object = MibTableColumn
swEndDeviceLinkFailure = _SwEndDeviceLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 4),
    _SwEndDeviceLinkFailure_Type()
)
swEndDeviceLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceLinkFailure.setStatus("current")


class _SwEndDeviceSyncLoss_Type(Integer32):
    """Custom type swEndDeviceSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceSyncLoss_Type.__name__ = "Integer32"
_SwEndDeviceSyncLoss_Object = MibTableColumn
swEndDeviceSyncLoss = _SwEndDeviceSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 5),
    _SwEndDeviceSyncLoss_Type()
)
swEndDeviceSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceSyncLoss.setStatus("current")


class _SwEndDeviceSigLoss_Type(Integer32):
    """Custom type swEndDeviceSigLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceSigLoss_Type.__name__ = "Integer32"
_SwEndDeviceSigLoss_Object = MibTableColumn
swEndDeviceSigLoss = _SwEndDeviceSigLoss_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 6),
    _SwEndDeviceSigLoss_Type()
)
swEndDeviceSigLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceSigLoss.setStatus("current")


class _SwEndDeviceProtoErr_Type(Integer32):
    """Custom type swEndDeviceProtoErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceProtoErr_Type.__name__ = "Integer32"
_SwEndDeviceProtoErr_Object = MibTableColumn
swEndDeviceProtoErr = _SwEndDeviceProtoErr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 7),
    _SwEndDeviceProtoErr_Type()
)
swEndDeviceProtoErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceProtoErr.setStatus("current")


class _SwEndDeviceInvalidWord_Type(Integer32):
    """Custom type swEndDeviceInvalidWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceInvalidWord_Type.__name__ = "Integer32"
_SwEndDeviceInvalidWord_Object = MibTableColumn
swEndDeviceInvalidWord = _SwEndDeviceInvalidWord_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 8),
    _SwEndDeviceInvalidWord_Type()
)
swEndDeviceInvalidWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceInvalidWord.setStatus("current")


class _SwEndDeviceInvalidCRC_Type(Integer32):
    """Custom type swEndDeviceInvalidCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwEndDeviceInvalidCRC_Type.__name__ = "Integer32"
_SwEndDeviceInvalidCRC_Object = MibTableColumn
swEndDeviceInvalidCRC = _SwEndDeviceInvalidCRC_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 21, 1, 1, 9),
    _SwEndDeviceInvalidCRC_Type()
)
swEndDeviceInvalidCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEndDeviceInvalidCRC.setStatus("current")
_SwGroup_ObjectIdentity = ObjectIdentity
swGroup = _SwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swGroup.setStatus("current")
_SwGroupTable_Object = MibTable
swGroupTable = _SwGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    swGroupTable.setStatus("current")
_SwGroupEntry_Object = MibTableRow
swGroupEntry = _SwGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1)
)
swGroupEntry.setIndexNames(
    (0, "SW57-MIB", "swGroupIndex"),
)
if mibBuilder.loadTexts:
    swGroupEntry.setStatus("current")


class _SwGroupIndex_Type(Integer32):
    """Custom type swGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupIndex_Type.__name__ = "Integer32"
_SwGroupIndex_Object = MibTableColumn
swGroupIndex = _SwGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 1),
    _SwGroupIndex_Type()
)
swGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupIndex.setStatus("current")


class _SwGroupName_Type(OctetString):
    """Custom type swGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwGroupName_Type.__name__ = "OctetString"
_SwGroupName_Object = MibTableColumn
swGroupName = _SwGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 2),
    _SwGroupName_Type()
)
swGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupName.setStatus("current")


class _SwGroupType_Type(OctetString):
    """Custom type swGroupType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwGroupType_Type.__name__ = "OctetString"
_SwGroupType_Object = MibTableColumn
swGroupType = _SwGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 1, 1, 3),
    _SwGroupType_Type()
)
swGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupType.setStatus("current")
_SwGroupMemTable_Object = MibTable
swGroupMemTable = _SwGroupMemTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    swGroupMemTable.setStatus("current")
_SwGroupMemEntry_Object = MibTableRow
swGroupMemEntry = _SwGroupMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1)
)
swGroupMemEntry.setIndexNames(
    (0, "SW57-MIB", "swGroupId"),
    (0, "SW57-MIB", "swGroupMemWwn"),
)
if mibBuilder.loadTexts:
    swGroupMemEntry.setStatus("current")


class _SwGroupId_Type(Integer32):
    """Custom type swGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupId_Type.__name__ = "Integer32"
_SwGroupId_Object = MibTableColumn
swGroupId = _SwGroupId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 1),
    _SwGroupId_Type()
)
swGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupId.setStatus("current")
_SwGroupMemWwn_Type = FcWwn
_SwGroupMemWwn_Object = MibTableColumn
swGroupMemWwn = _SwGroupMemWwn_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 2),
    _SwGroupMemWwn_Type()
)
swGroupMemWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupMemWwn.setStatus("current")


class _SwGroupMemPos_Type(Integer32):
    """Custom type swGroupMemPos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwGroupMemPos_Type.__name__ = "Integer32"
_SwGroupMemPos_Object = MibTableColumn
swGroupMemPos = _SwGroupMemPos_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 22, 2, 1, 3),
    _SwGroupMemPos_Type()
)
swGroupMemPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGroupMemPos.setStatus("current")
_SwBlmPerfMnt_ObjectIdentity = ObjectIdentity
swBlmPerfMnt = _SwBlmPerfMnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23)
)
if mibBuilder.loadTexts:
    swBlmPerfMnt.setStatus("current")
_SwBlmPerfALPAMntTable_Object = MibTable
swBlmPerfALPAMntTable = _SwBlmPerfALPAMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    swBlmPerfALPAMntTable.setStatus("current")
_SwBlmPerfALPAMntEntry_Object = MibTableRow
swBlmPerfALPAMntEntry = _SwBlmPerfALPAMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1)
)
swBlmPerfALPAMntEntry.setIndexNames(
    (0, "SW57-MIB", "swBlmPerfAlpaPort"),
    (0, "SW57-MIB", "swBlmPerfAlpaIndx"),
)
if mibBuilder.loadTexts:
    swBlmPerfALPAMntEntry.setStatus("current")
_SwBlmPerfAlpaPort_Type = SwPortIndex
_SwBlmPerfAlpaPort_Object = MibTableColumn
swBlmPerfAlpaPort = _SwBlmPerfAlpaPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 1),
    _SwBlmPerfAlpaPort_Type()
)
swBlmPerfAlpaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaPort.setStatus("current")


class _SwBlmPerfAlpaIndx_Type(Integer32):
    """Custom type swBlmPerfAlpaIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_SwBlmPerfAlpaIndx_Type.__name__ = "Integer32"
_SwBlmPerfAlpaIndx_Object = MibTableColumn
swBlmPerfAlpaIndx = _SwBlmPerfAlpaIndx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 2),
    _SwBlmPerfAlpaIndx_Type()
)
swBlmPerfAlpaIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaIndx.setStatus("current")


class _SwBlmPerfAlpa_Type(Integer32):
    """Custom type swBlmPerfAlpa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfAlpa_Type.__name__ = "Integer32"
_SwBlmPerfAlpa_Object = MibTableColumn
swBlmPerfAlpa = _SwBlmPerfAlpa_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 3),
    _SwBlmPerfAlpa_Type()
)
swBlmPerfAlpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpa.setStatus("current")


class _SwBlmPerfAlpaCRCCnt_Type(OctetString):
    """Custom type swBlmPerfAlpaCRCCnt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwBlmPerfAlpaCRCCnt_Type.__name__ = "OctetString"
_SwBlmPerfAlpaCRCCnt_Object = MibTableColumn
swBlmPerfAlpaCRCCnt = _SwBlmPerfAlpaCRCCnt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 1, 1, 4),
    _SwBlmPerfAlpaCRCCnt_Type()
)
swBlmPerfAlpaCRCCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfAlpaCRCCnt.setStatus("current")
_SwBlmPerfEEMntTable_Object = MibTable
swBlmPerfEEMntTable = _SwBlmPerfEEMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2)
)
if mibBuilder.loadTexts:
    swBlmPerfEEMntTable.setStatus("current")
_SwBlmPerfEEMntEntry_Object = MibTableRow
swBlmPerfEEMntEntry = _SwBlmPerfEEMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1)
)
swBlmPerfEEMntEntry.setIndexNames(
    (0, "SW57-MIB", "swBlmPerfEEPort"),
    (0, "SW57-MIB", "swBlmPerfEERefKey"),
)
if mibBuilder.loadTexts:
    swBlmPerfEEMntEntry.setStatus("current")
_SwBlmPerfEEPort_Type = SwPortIndex
_SwBlmPerfEEPort_Object = MibTableColumn
swBlmPerfEEPort = _SwBlmPerfEEPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 1),
    _SwBlmPerfEEPort_Type()
)
swBlmPerfEEPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEPort.setStatus("current")


class _SwBlmPerfEERefKey_Type(Integer32):
    """Custom type swBlmPerfEERefKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwBlmPerfEERefKey_Type.__name__ = "Integer32"
_SwBlmPerfEERefKey_Object = MibTableColumn
swBlmPerfEERefKey = _SwBlmPerfEERefKey_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 2),
    _SwBlmPerfEERefKey_Type()
)
swBlmPerfEERefKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEERefKey.setStatus("current")


class _SwBlmPerfEECRC_Type(OctetString):
    """Custom type swBlmPerfEECRC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwBlmPerfEECRC_Type.__name__ = "OctetString"
_SwBlmPerfEECRC_Object = MibTableColumn
swBlmPerfEECRC = _SwBlmPerfEECRC_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 3),
    _SwBlmPerfEECRC_Type()
)
swBlmPerfEECRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEECRC.setStatus("current")


class _SwBlmPerfEEFCWRx_Type(OctetString):
    """Custom type swBlmPerfEEFCWRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwBlmPerfEEFCWRx_Type.__name__ = "OctetString"
_SwBlmPerfEEFCWRx_Object = MibTableColumn
swBlmPerfEEFCWRx = _SwBlmPerfEEFCWRx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 4),
    _SwBlmPerfEEFCWRx_Type()
)
swBlmPerfEEFCWRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEFCWRx.setStatus("current")


class _SwBlmPerfEEFCWTx_Type(OctetString):
    """Custom type swBlmPerfEEFCWTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwBlmPerfEEFCWTx_Type.__name__ = "OctetString"
_SwBlmPerfEEFCWTx_Object = MibTableColumn
swBlmPerfEEFCWTx = _SwBlmPerfEEFCWTx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 5),
    _SwBlmPerfEEFCWTx_Type()
)
swBlmPerfEEFCWTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEFCWTx.setStatus("current")


class _SwBlmPerfEESid_Type(Integer32):
    """Custom type swBlmPerfEESid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfEESid_Type.__name__ = "Integer32"
_SwBlmPerfEESid_Object = MibTableColumn
swBlmPerfEESid = _SwBlmPerfEESid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 6),
    _SwBlmPerfEESid_Type()
)
swBlmPerfEESid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEESid.setStatus("current")


class _SwBlmPerfEEDid_Type(Integer32):
    """Custom type swBlmPerfEEDid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwBlmPerfEEDid_Type.__name__ = "Integer32"
_SwBlmPerfEEDid_Object = MibTableColumn
swBlmPerfEEDid = _SwBlmPerfEEDid_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 2, 1, 7),
    _SwBlmPerfEEDid_Type()
)
swBlmPerfEEDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfEEDid.setStatus("current")
_SwBlmPerfFltMntTable_Object = MibTable
swBlmPerfFltMntTable = _SwBlmPerfFltMntTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3)
)
if mibBuilder.loadTexts:
    swBlmPerfFltMntTable.setStatus("current")
_SwBlmPerfFltMntEntry_Object = MibTableRow
swBlmPerfFltMntEntry = _SwBlmPerfFltMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1)
)
swBlmPerfFltMntEntry.setIndexNames(
    (0, "SW57-MIB", "swBlmPerfFltPort"),
    (0, "SW57-MIB", "swBlmPerfFltRefkey"),
)
if mibBuilder.loadTexts:
    swBlmPerfFltMntEntry.setStatus("current")
_SwBlmPerfFltPort_Type = SwPortIndex
_SwBlmPerfFltPort_Object = MibTableColumn
swBlmPerfFltPort = _SwBlmPerfFltPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 1),
    _SwBlmPerfFltPort_Type()
)
swBlmPerfFltPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltPort.setStatus("current")


class _SwBlmPerfFltRefkey_Type(Integer32):
    """Custom type swBlmPerfFltRefkey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SwBlmPerfFltRefkey_Type.__name__ = "Integer32"
_SwBlmPerfFltRefkey_Object = MibTableColumn
swBlmPerfFltRefkey = _SwBlmPerfFltRefkey_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 2),
    _SwBlmPerfFltRefkey_Type()
)
swBlmPerfFltRefkey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltRefkey.setStatus("current")


class _SwBlmPerfFltCnt_Type(OctetString):
    """Custom type swBlmPerfFltCnt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwBlmPerfFltCnt_Type.__name__ = "OctetString"
_SwBlmPerfFltCnt_Object = MibTableColumn
swBlmPerfFltCnt = _SwBlmPerfFltCnt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 3),
    _SwBlmPerfFltCnt_Type()
)
swBlmPerfFltCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltCnt.setStatus("current")


class _SwBlmPerfFltAlias_Type(DisplayString):
    """Custom type swBlmPerfFltAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBlmPerfFltAlias_Type.__name__ = "DisplayString"
_SwBlmPerfFltAlias_Object = MibTableColumn
swBlmPerfFltAlias = _SwBlmPerfFltAlias_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 23, 3, 1, 4),
    _SwBlmPerfFltAlias_Type()
)
swBlmPerfFltAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBlmPerfFltAlias.setStatus("current")
_SwTrunk_ObjectIdentity = ObjectIdentity
swTrunk = _SwTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    swTrunk.setStatus("current")


class _SwSwitchTrunkable_Type(Integer32):
    """Custom type swSwitchTrunkable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 8))
    )


_SwSwitchTrunkable_Type.__name__ = "Integer32"
_SwSwitchTrunkable_Object = MibScalar
swSwitchTrunkable = _SwSwitchTrunkable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 1),
    _SwSwitchTrunkable_Type()
)
swSwitchTrunkable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSwitchTrunkable.setStatus("current")
_SwTrunkTable_Object = MibTable
swTrunkTable = _SwTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2)
)
if mibBuilder.loadTexts:
    swTrunkTable.setStatus("current")
_SwTrunkEntry_Object = MibTableRow
swTrunkEntry = _SwTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1)
)
swTrunkEntry.setIndexNames(
    (0, "SW57-MIB", "swTrunkPortIndex"),
)
if mibBuilder.loadTexts:
    swTrunkEntry.setStatus("current")
_SwTrunkPortIndex_Type = SwPortIndex
_SwTrunkPortIndex_Object = MibTableColumn
swTrunkPortIndex = _SwTrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 1),
    _SwTrunkPortIndex_Type()
)
swTrunkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkPortIndex.setStatus("current")


class _SwTrunkGroupNumber_Type(Integer32):
    """Custom type swTrunkGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwTrunkGroupNumber_Type.__name__ = "Integer32"
_SwTrunkGroupNumber_Object = MibTableColumn
swTrunkGroupNumber = _SwTrunkGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 2),
    _SwTrunkGroupNumber_Type()
)
swTrunkGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGroupNumber.setStatus("current")
_SwTrunkMaster_Type = SwTrunkMaster
_SwTrunkMaster_Object = MibTableColumn
swTrunkMaster = _SwTrunkMaster_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 3),
    _SwTrunkMaster_Type()
)
swTrunkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkMaster.setStatus("current")


class _SwPortTrunked_Type(Integer32):
    """Custom type swPortTrunked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SwPortTrunked_Type.__name__ = "Integer32"
_SwPortTrunked_Object = MibTableColumn
swPortTrunked = _SwPortTrunked_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 2, 1, 4),
    _SwPortTrunked_Type()
)
swPortTrunked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunked.setStatus("current")
_SwTrunkGrpTable_Object = MibTable
swTrunkGrpTable = _SwTrunkGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3)
)
if mibBuilder.loadTexts:
    swTrunkGrpTable.setStatus("current")
_SwTrunkGrpEntry_Object = MibTableRow
swTrunkGrpEntry = _SwTrunkGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1)
)
swTrunkGrpEntry.setIndexNames(
    (0, "SW57-MIB", "swTrunkGrpNumber"),
)
if mibBuilder.loadTexts:
    swTrunkGrpEntry.setStatus("current")


class _SwTrunkGrpNumber_Type(Integer32):
    """Custom type swTrunkGrpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwTrunkGrpNumber_Type.__name__ = "Integer32"
_SwTrunkGrpNumber_Object = MibTableColumn
swTrunkGrpNumber = _SwTrunkGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 1),
    _SwTrunkGrpNumber_Type()
)
swTrunkGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpNumber.setStatus("current")
_SwTrunkGrpMaster_Type = SwTrunkMaster
_SwTrunkGrpMaster_Object = MibTableColumn
swTrunkGrpMaster = _SwTrunkGrpMaster_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 2),
    _SwTrunkGrpMaster_Type()
)
swTrunkGrpMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpMaster.setStatus("current")


class _SwTrunkGrpTx_Type(OctetString):
    """Custom type swTrunkGrpTx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwTrunkGrpTx_Type.__name__ = "OctetString"
_SwTrunkGrpTx_Object = MibTableColumn
swTrunkGrpTx = _SwTrunkGrpTx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 3),
    _SwTrunkGrpTx_Type()
)
swTrunkGrpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpTx.setStatus("current")


class _SwTrunkGrpRx_Type(OctetString):
    """Custom type swTrunkGrpRx based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SwTrunkGrpRx_Type.__name__ = "OctetString"
_SwTrunkGrpRx_Object = MibTableColumn
swTrunkGrpRx = _SwTrunkGrpRx_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 24, 3, 1, 4),
    _SwTrunkGrpRx_Type()
)
swTrunkGrpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTrunkGrpRx.setStatus("current")
_Sw28k_ObjectIdentity = ObjectIdentity
sw28k = _Sw28k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sw28k.setStatus("current")
_Sw21kN24k_ObjectIdentity = ObjectIdentity
sw21kN24k = _Sw21kN24k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sw21kN24k.setStatus("current")
_Sw20x0_ObjectIdentity = ObjectIdentity
sw20x0 = _Sw20x0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sw20x0.setStatus("current")

# Managed Objects groups


# Notification objects

swFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 1)
)
swFault.setObjects(
      *(("SW57-MIB", "swDiagResult"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swFault.setStatus(
        "obsolete"
    )

swSensorScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 2)
)
swSensorScn.setObjects(
      *(("SW57-MIB", "swSensorStatus"),
        ("SW57-MIB", "swSensorIndex"),
        ("SW57-MIB", "swSensorType"),
        ("SW57-MIB", "swSensorValue"),
        ("SW57-MIB", "swSensorInfo"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swSensorScn.setStatus(
        "current"
    )

swFCPortScn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 3)
)
swFCPortScn.setObjects(
      *(("SW57-MIB", "swFCPortOpStatus"),
        ("SW57-MIB", "swFCPortIndex"),
        ("SW57-MIB", "swFCPortName"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swFCPortFlag"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swFCPortScn.setStatus(
        "current"
    )

swEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 4)
)
swEventTrap.setObjects(
      *(("SW57-MIB", "swEventIndex"),
        ("SW57-MIB", "swEventTimeInfo"),
        ("SW57-MIB", "swEventLevel"),
        ("SW57-MIB", "swEventRepeatCount"),
        ("SW57-MIB", "swEventDescr"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swEventTrap.setStatus(
        "current"
    )

swFabricWatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 5)
)
swFabricWatchTrap.setObjects(
      *(("SW57-MIB", "swFwClassAreaIndex"),
        ("SW57-MIB", "swFwThresholdIndex"),
        ("SW57-MIB", "swFwName"),
        ("SW57-MIB", "swFwLabel"),
        ("SW57-MIB", "swFwLastEventVal"),
        ("SW57-MIB", "swFwLastEventTime"),
        ("SW57-MIB", "swFwLastEvent"),
        ("SW57-MIB", "swFwLastState"),
        ("SW57-MIB", "swFwLastSeverityLevel"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swFabricWatchTrap.setStatus(
        "current"
    )

swTrackChangesTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 0, 6)
)
swTrackChangesTrap.setObjects(
      *(("SW57-MIB", "swTrackChangesInfo"),
        ("SW57-MIB", "swSsn"),
        ("SW57-MIB", "swGroupName"),
        ("SW57-MIB", "swGroupType"),
        ("SW57-MIB", "swGroupMemPos"))
)
if mibBuilder.loadTexts:
    swTrackChangesTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW57-MIB",
    **{"SwSevType": SwSevType,
       "FcPortFlag": FcPortFlag,
       "SwFwActs": SwFwActs,
       "SwFwLevels": SwFwLevels,
       "SwFwClassesAreas": SwFwClassesAreas,
       "SwFwWriteVals": SwFwWriteVals,
       "SwFwTimebase": SwFwTimebase,
       "SwFwStatus": SwFwStatus,
       "SwFwEvent": SwFwEvent,
       "SwFwBehavior": SwFwBehavior,
       "SwFwState": SwFwState,
       "SwFwLicense": SwFwLicense,
       "sw": sw,
       "swTrapsV2": swTrapsV2,
       "swFault": swFault,
       "swSensorScn": swSensorScn,
       "swFCPortScn": swFCPortScn,
       "swEventTrap": swEventTrap,
       "swFabricWatchTrap": swFabricWatchTrap,
       "swTrackChangesTrap": swTrackChangesTrap,
       "swSystem": swSystem,
       "swCurrentDate": swCurrentDate,
       "swBootDate": swBootDate,
       "swFWLastUpdated": swFWLastUpdated,
       "swFlashLastUpdated": swFlashLastUpdated,
       "swBootPromLastUpdated": swBootPromLastUpdated,
       "swFirmwareVersion": swFirmwareVersion,
       "swOperStatus": swOperStatus,
       "swAdmStatus": swAdmStatus,
       "swTelnetShellAdmStatus": swTelnetShellAdmStatus,
       "swSsn": swSsn,
       "swFlashDLOperStatus": swFlashDLOperStatus,
       "swFlashDLAdmStatus": swFlashDLAdmStatus,
       "swFlashDLHost": swFlashDLHost,
       "swFlashDLUser": swFlashDLUser,
       "swFlashDLFile": swFlashDLFile,
       "swFlashDLPassword": swFlashDLPassword,
       "swBeaconOperStatus": swBeaconOperStatus,
       "swBeaconAdmStatus": swBeaconAdmStatus,
       "swDiagResult": swDiagResult,
       "swNumSensors": swNumSensors,
       "swSensorTable": swSensorTable,
       "swSensorEntry": swSensorEntry,
       "swSensorIndex": swSensorIndex,
       "swSensorType": swSensorType,
       "swSensorStatus": swSensorStatus,
       "swSensorValue": swSensorValue,
       "swSensorInfo": swSensorInfo,
       "swTrackChangesInfo": swTrackChangesInfo,
       "swID": swID,
       "swEtherIPAddress": swEtherIPAddress,
       "swEtherIPMask": swEtherIPMask,
       "swFCIPAddress": swFCIPAddress,
       "swFCIPMask": swFCIPMask,
       "swFabric": swFabric,
       "swDomainID": swDomainID,
       "swPrincipalSwitch": swPrincipalSwitch,
       "swNumNbs": swNumNbs,
       "swNbTable": swNbTable,
       "swNbEntry": swNbEntry,
       "swNbIndex": swNbIndex,
       "swNbMyPort": swNbMyPort,
       "swNbRemDomain": swNbRemDomain,
       "swNbRemPort": swNbRemPort,
       "swNbBaudRate": swNbBaudRate,
       "swNbIslState": swNbIslState,
       "swNbIslCost": swNbIslCost,
       "swNbRemPortName": swNbRemPortName,
       "swFabricMemTable": swFabricMemTable,
       "swFabricMemEntry": swFabricMemEntry,
       "swFabricMemWwn": swFabricMemWwn,
       "swFabricMemDid": swFabricMemDid,
       "swFabricMemName": swFabricMemName,
       "swFabricMemEIP": swFabricMemEIP,
       "swFabricMemFCIP": swFabricMemFCIP,
       "swFabricMemGWIP": swFabricMemGWIP,
       "swFabricMemType": swFabricMemType,
       "swFabricMemShortVersion": swFabricMemShortVersion,
       "swIDIDMode": swIDIDMode,
       "swModule": swModule,
       "swAgtCfg": swAgtCfg,
       "swAgtCmtyTable": swAgtCmtyTable,
       "swAgtCmtyEntry": swAgtCmtyEntry,
       "swAgtCmtyIdx": swAgtCmtyIdx,
       "swAgtCmtyStr": swAgtCmtyStr,
       "swAgtTrapRcp": swAgtTrapRcp,
       "swAgtTrapSeverityLevel": swAgtTrapSeverityLevel,
       "swFCport": swFCport,
       "swFCPortCapacity": swFCPortCapacity,
       "swFCPortTable": swFCPortTable,
       "swFCPortEntry": swFCPortEntry,
       "swFCPortIndex": swFCPortIndex,
       "swFCPortType": swFCPortType,
       "swFCPortPhyState": swFCPortPhyState,
       "swFCPortOpStatus": swFCPortOpStatus,
       "swFCPortAdmStatus": swFCPortAdmStatus,
       "swFCPortLinkState": swFCPortLinkState,
       "swFCPortTxType": swFCPortTxType,
       "swFCPortTxWords": swFCPortTxWords,
       "swFCPortRxWords": swFCPortRxWords,
       "swFCPortTxFrames": swFCPortTxFrames,
       "swFCPortRxFrames": swFCPortRxFrames,
       "swFCPortRxC2Frames": swFCPortRxC2Frames,
       "swFCPortRxC3Frames": swFCPortRxC3Frames,
       "swFCPortRxLCs": swFCPortRxLCs,
       "swFCPortRxMcasts": swFCPortRxMcasts,
       "swFCPortTooManyRdys": swFCPortTooManyRdys,
       "swFCPortNoTxCredits": swFCPortNoTxCredits,
       "swFCPortRxEncInFrs": swFCPortRxEncInFrs,
       "swFCPortRxCrcs": swFCPortRxCrcs,
       "swFCPortRxTruncs": swFCPortRxTruncs,
       "swFCPortRxTooLongs": swFCPortRxTooLongs,
       "swFCPortRxBadEofs": swFCPortRxBadEofs,
       "swFCPortRxEncOutFrs": swFCPortRxEncOutFrs,
       "swFCPortRxBadOs": swFCPortRxBadOs,
       "swFCPortC3Discards": swFCPortC3Discards,
       "swFCPortMcastTimedOuts": swFCPortMcastTimedOuts,
       "swFCPortTxMcasts": swFCPortTxMcasts,
       "swFCPortLipIns": swFCPortLipIns,
       "swFCPortLipOuts": swFCPortLipOuts,
       "swFCPortLipLastAlpa": swFCPortLipLastAlpa,
       "swFCPortWwn": swFCPortWwn,
       "swFCPortSpeed": swFCPortSpeed,
       "swFCPortName": swFCPortName,
       "swFCPortSpecifier": swFCPortSpecifier,
       "swFCPortFlag": swFCPortFlag,
       "swFCPortBrcdType": swFCPortBrcdType,
       "swNs": swNs,
       "swNsLocalNumEntry": swNsLocalNumEntry,
       "swNsLocalTable": swNsLocalTable,
       "swNsLocalEntry": swNsLocalEntry,
       "swNsEntryIndex": swNsEntryIndex,
       "swNsPortID": swNsPortID,
       "swNsPortType": swNsPortType,
       "swNsPortName": swNsPortName,
       "swNsPortSymb": swNsPortSymb,
       "swNsNodeName": swNsNodeName,
       "swNsNodeSymb": swNsNodeSymb,
       "swNsIPA": swNsIPA,
       "swNsIpAddress": swNsIpAddress,
       "swNsCos": swNsCos,
       "swNsFc4": swNsFc4,
       "swNsIpNxPort": swNsIpNxPort,
       "swNsWwn": swNsWwn,
       "swNsHardAddr": swNsHardAddr,
       "swEvent": swEvent,
       "swEventTrapLevel": swEventTrapLevel,
       "swEventNumEntries": swEventNumEntries,
       "swEventTable": swEventTable,
       "swEventEntry": swEventEntry,
       "swEventIndex": swEventIndex,
       "swEventTimeInfo": swEventTimeInfo,
       "swEventLevel": swEventLevel,
       "swEventRepeatCount": swEventRepeatCount,
       "swEventDescr": swEventDescr,
       "swFwSystem": swFwSystem,
       "swFwFabricWatchLicense": swFwFabricWatchLicense,
       "swFwClassAreaTable": swFwClassAreaTable,
       "swFwClassAreaEntry": swFwClassAreaEntry,
       "swFwClassAreaIndex": swFwClassAreaIndex,
       "swFwWriteThVals": swFwWriteThVals,
       "swFwDefaultUnit": swFwDefaultUnit,
       "swFwDefaultTimebase": swFwDefaultTimebase,
       "swFwDefaultLow": swFwDefaultLow,
       "swFwDefaultHigh": swFwDefaultHigh,
       "swFwDefaultBufSize": swFwDefaultBufSize,
       "swFwCustUnit": swFwCustUnit,
       "swFwCustTimebase": swFwCustTimebase,
       "swFwCustLow": swFwCustLow,
       "swFwCustHigh": swFwCustHigh,
       "swFwCustBufSize": swFwCustBufSize,
       "swFwThLevel": swFwThLevel,
       "swFwWriteActVals": swFwWriteActVals,
       "swFwDefaultChangedActs": swFwDefaultChangedActs,
       "swFwDefaultExceededActs": swFwDefaultExceededActs,
       "swFwDefaultBelowActs": swFwDefaultBelowActs,
       "swFwDefaultAboveActs": swFwDefaultAboveActs,
       "swFwDefaultInBetweenActs": swFwDefaultInBetweenActs,
       "swFwCustChangedActs": swFwCustChangedActs,
       "swFwCustExceededActs": swFwCustExceededActs,
       "swFwCustBelowActs": swFwCustBelowActs,
       "swFwCustAboveActs": swFwCustAboveActs,
       "swFwCustInBetweenActs": swFwCustInBetweenActs,
       "swFwValidActs": swFwValidActs,
       "swFwActLevel": swFwActLevel,
       "swFwThresholdTable": swFwThresholdTable,
       "swFwThresholdEntry": swFwThresholdEntry,
       "swFwThresholdIndex": swFwThresholdIndex,
       "swFwStatus": swFwStatus,
       "swFwName": swFwName,
       "swFwLabel": swFwLabel,
       "swFwCurVal": swFwCurVal,
       "swFwLastEvent": swFwLastEvent,
       "swFwLastEventVal": swFwLastEventVal,
       "swFwLastEventTime": swFwLastEventTime,
       "swFwLastState": swFwLastState,
       "swFwBehaviorType": swFwBehaviorType,
       "swFwBehaviorInt": swFwBehaviorInt,
       "swFwLastSeverityLevel": swFwLastSeverityLevel,
       "swEndDevice": swEndDevice,
       "swEndDeviceRlsTable": swEndDeviceRlsTable,
       "swEndDeviceRlsEntry": swEndDeviceRlsEntry,
       "swEndDevicePort": swEndDevicePort,
       "swEndDeviceAlpa": swEndDeviceAlpa,
       "swEndDevicePortID": swEndDevicePortID,
       "swEndDeviceLinkFailure": swEndDeviceLinkFailure,
       "swEndDeviceSyncLoss": swEndDeviceSyncLoss,
       "swEndDeviceSigLoss": swEndDeviceSigLoss,
       "swEndDeviceProtoErr": swEndDeviceProtoErr,
       "swEndDeviceInvalidWord": swEndDeviceInvalidWord,
       "swEndDeviceInvalidCRC": swEndDeviceInvalidCRC,
       "swGroup": swGroup,
       "swGroupTable": swGroupTable,
       "swGroupEntry": swGroupEntry,
       "swGroupIndex": swGroupIndex,
       "swGroupName": swGroupName,
       "swGroupType": swGroupType,
       "swGroupMemTable": swGroupMemTable,
       "swGroupMemEntry": swGroupMemEntry,
       "swGroupId": swGroupId,
       "swGroupMemWwn": swGroupMemWwn,
       "swGroupMemPos": swGroupMemPos,
       "swBlmPerfMnt": swBlmPerfMnt,
       "swBlmPerfALPAMntTable": swBlmPerfALPAMntTable,
       "swBlmPerfALPAMntEntry": swBlmPerfALPAMntEntry,
       "swBlmPerfAlpaPort": swBlmPerfAlpaPort,
       "swBlmPerfAlpaIndx": swBlmPerfAlpaIndx,
       "swBlmPerfAlpa": swBlmPerfAlpa,
       "swBlmPerfAlpaCRCCnt": swBlmPerfAlpaCRCCnt,
       "swBlmPerfEEMntTable": swBlmPerfEEMntTable,
       "swBlmPerfEEMntEntry": swBlmPerfEEMntEntry,
       "swBlmPerfEEPort": swBlmPerfEEPort,
       "swBlmPerfEERefKey": swBlmPerfEERefKey,
       "swBlmPerfEECRC": swBlmPerfEECRC,
       "swBlmPerfEEFCWRx": swBlmPerfEEFCWRx,
       "swBlmPerfEEFCWTx": swBlmPerfEEFCWTx,
       "swBlmPerfEESid": swBlmPerfEESid,
       "swBlmPerfEEDid": swBlmPerfEEDid,
       "swBlmPerfFltMntTable": swBlmPerfFltMntTable,
       "swBlmPerfFltMntEntry": swBlmPerfFltMntEntry,
       "swBlmPerfFltPort": swBlmPerfFltPort,
       "swBlmPerfFltRefkey": swBlmPerfFltRefkey,
       "swBlmPerfFltCnt": swBlmPerfFltCnt,
       "swBlmPerfFltAlias": swBlmPerfFltAlias,
       "swTrunk": swTrunk,
       "swSwitchTrunkable": swSwitchTrunkable,
       "swTrunkTable": swTrunkTable,
       "swTrunkEntry": swTrunkEntry,
       "swTrunkPortIndex": swTrunkPortIndex,
       "swTrunkGroupNumber": swTrunkGroupNumber,
       "swTrunkMaster": swTrunkMaster,
       "swPortTrunked": swPortTrunked,
       "swTrunkGrpTable": swTrunkGrpTable,
       "swTrunkGrpEntry": swTrunkGrpEntry,
       "swTrunkGrpNumber": swTrunkGrpNumber,
       "swTrunkGrpMaster": swTrunkGrpMaster,
       "swTrunkGrpTx": swTrunkGrpTx,
       "swTrunkGrpRx": swTrunkGrpRx,
       "sw28k": sw28k,
       "sw21kN24k": sw21kN24k,
       "sw20x0": sw20x0,
       "swMibModule": swMibModule}
)
