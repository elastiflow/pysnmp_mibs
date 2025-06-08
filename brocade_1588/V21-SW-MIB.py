# SNMP MIB module (V21-SW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1588/V21-SW-MIB.mib
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

(MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn) = mibBuilder.importSymbols(
    "RFC1212",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class FcWwn(OctetString):
    """Custom type FcWwn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class SwDomainIndex(Integer32):
    """Custom type SwDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )





class SwNbIndex(Integer32):
    """Custom type SwNbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )





class SwSensorIndex(Integer32):
    """Custom type SwSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bcsi_ObjectIdentity = ObjectIdentity
bcsi = _Bcsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588)
)
_CommDev_ObjectIdentity = ObjectIdentity
commDev = _CommDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2)
)
_Fibrechannel_ObjectIdentity = ObjectIdentity
fibrechannel = _Fibrechannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1)
)
_FcSwitch_ObjectIdentity = ObjectIdentity
fcSwitch = _FcSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1)
)
_Sw_ObjectIdentity = ObjectIdentity
sw = _Sw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1)
)
_SwSystem_ObjectIdentity = ObjectIdentity
swSystem = _SwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1)
)


class _SwCurrentDate_Type(DisplayString):
    """Custom type swCurrentDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwCurrentDate_Type.__name__ = "DisplayString"
_SwCurrentDate_Object = MibScalar
swCurrentDate = _SwCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 1),
    _SwCurrentDate_Type()
)
swCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentDate.setStatus("mandatory")


class _SwBootDate_Type(DisplayString):
    """Custom type swBootDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwBootDate_Type.__name__ = "DisplayString"
_SwBootDate_Object = MibScalar
swBootDate = _SwBootDate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 2),
    _SwBootDate_Type()
)
swBootDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootDate.setStatus("mandatory")


class _SwFWLastUpdated_Type(DisplayString):
    """Custom type swFWLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwFWLastUpdated_Type.__name__ = "DisplayString"
_SwFWLastUpdated_Object = MibScalar
swFWLastUpdated = _SwFWLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 3),
    _SwFWLastUpdated_Type()
)
swFWLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFWLastUpdated.setStatus("mandatory")
_SwFlashLastUpdated_Type = DisplayString
_SwFlashLastUpdated_Object = MibScalar
swFlashLastUpdated = _SwFlashLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 4),
    _SwFlashLastUpdated_Type()
)
swFlashLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashLastUpdated.setStatus("mandatory")


class _SwBootPromLastUpdated_Type(DisplayString):
    """Custom type swBootPromLastUpdated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_SwBootPromLastUpdated_Type.__name__ = "DisplayString"
_SwBootPromLastUpdated_Object = MibScalar
swBootPromLastUpdated = _SwBootPromLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 5),
    _SwBootPromLastUpdated_Type()
)
swBootPromLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootPromLastUpdated.setStatus("mandatory")


class _SwFirmwareVersion_Type(DisplayString):
    """Custom type swFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_SwFirmwareVersion_Type.__name__ = "DisplayString"
_SwFirmwareVersion_Object = MibScalar
swFirmwareVersion = _SwFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 6),
    _SwFirmwareVersion_Type()
)
swFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFirmwareVersion.setStatus("mandatory")


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
    swOperStatus.setStatus("mandatory")


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
              6)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2),
          ("testing", 3),
          ("faulty", 4),
          ("reboot", 5),
          ("fastboot", 6))
    )


_SwAdmStatus_Type.__name__ = "Integer32"
_SwAdmStatus_Object = MibScalar
swAdmStatus = _SwAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 8),
    _SwAdmStatus_Type()
)
swAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAdmStatus.setStatus("mandatory")


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
    swTelnetShellAdmStatus.setStatus("mandatory")


class _SwFlashDLOperStatus_Type(Integer32):
    """Custom type swFlashDLOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sw-current", 1),
          ("sw-upgraded", 2))
    )


_SwFlashDLOperStatus_Type.__name__ = "Integer32"
_SwFlashDLOperStatus_Object = MibScalar
swFlashDLOperStatus = _SwFlashDLOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 11),
    _SwFlashDLOperStatus_Type()
)
swFlashDLOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFlashDLOperStatus.setStatus("mandatory")


class _SwFlashDLAdmStatus_Type(Integer32):
    """Custom type swFlashDLAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sw-current", 1),
          ("sw-upgraded", 2))
    )


_SwFlashDLAdmStatus_Type.__name__ = "Integer32"
_SwFlashDLAdmStatus_Object = MibScalar
swFlashDLAdmStatus = _SwFlashDLAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 12),
    _SwFlashDLAdmStatus_Type()
)
swFlashDLAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLAdmStatus.setStatus("mandatory")


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
    swFlashDLHost.setStatus("mandatory")


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
    swFlashDLUser.setStatus("mandatory")


class _SwFlashDLFile_Type(DisplayString):
    """Custom type swFlashDLFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwFlashDLFile_Type.__name__ = "DisplayString"
_SwFlashDLFile_Object = MibScalar
swFlashDLFile = _SwFlashDLFile_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 15),
    _SwFlashDLFile_Type()
)
swFlashDLFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFlashDLFile.setStatus("mandatory")


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
          ("sw-central-memory-fault", 2),
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
    swDiagResult.setStatus("mandatory")
_SwNumSensors_Type = Integer32
_SwNumSensors_Object = MibScalar
swNumSensors = _SwNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 21),
    _SwNumSensors_Type()
)
swNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumSensors.setStatus("mandatory")
_SwSensorTable_Object = MibTable
swSensorTable = _SwSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    swSensorTable.setStatus("mandatory")
_SwSensorEntry_Object = MibTableRow
swSensorEntry = _SwSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1)
)
swSensorEntry.setIndexNames(
    (0, "V21-SW-MIB", "swSensorIndex"),
)
if mibBuilder.loadTexts:
    swSensorEntry.setStatus("mandatory")
_SwSensorIndex_Type = SwSensorIndex
_SwSensorIndex_Object = MibTableColumn
swSensorIndex = _SwSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 1),
    _SwSensorIndex_Type()
)
swSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorIndex.setStatus("mandatory")


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
    swSensorType.setStatus("mandatory")


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
    swSensorStatus.setStatus("mandatory")
_SwSensorValue_Type = Integer32
_SwSensorValue_Object = MibTableColumn
swSensorValue = _SwSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 4),
    _SwSensorValue_Type()
)
swSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorValue.setStatus("mandatory")


class _SwSensorInfo_Type(DisplayString):
    """Custom type swSensorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )
    fixed_length = 256


_SwSensorInfo_Type.__name__ = "DisplayString"
_SwSensorInfo_Object = MibTableColumn
swSensorInfo = _SwSensorInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 1, 22, 1, 5),
    _SwSensorInfo_Type()
)
swSensorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSensorInfo.setStatus("mandatory")
_SwFabric_ObjectIdentity = ObjectIdentity
swFabric = _SwFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2)
)
_SwDomainID_Type = SwDomainIndex
_SwDomainID_Object = MibScalar
swDomainID = _SwDomainID_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 1),
    _SwDomainID_Type()
)
swDomainID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDomainID.setStatus("mandatory")


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
    swPrincipalSwitch.setStatus("mandatory")
_SwNumNbs_Type = Integer32
_SwNumNbs_Object = MibScalar
swNumNbs = _SwNumNbs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 8),
    _SwNumNbs_Type()
)
swNumNbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNumNbs.setStatus("mandatory")
_SwNbTable_Object = MibTable
swNbTable = _SwNbTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    swNbTable.setStatus("mandatory")
_SwNbEntry_Object = MibTableRow
swNbEntry = _SwNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1)
)
swNbEntry.setIndexNames(
    (0, "V21-SW-MIB", "swNbIndex"),
)
if mibBuilder.loadTexts:
    swNbEntry.setStatus("mandatory")
_SwNbIndex_Type = SwNbIndex
_SwNbIndex_Object = MibTableColumn
swNbIndex = _SwNbIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 1),
    _SwNbIndex_Type()
)
swNbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbIndex.setStatus("mandatory")


class _SwNbMyPort_Type(Integer32):
    """Custom type swNbMyPort based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("portNum-0", 1),
          ("portNum-1", 2),
          ("portNum-2", 3),
          ("portNum-3", 4),
          ("portNum-4", 5),
          ("portNum-5", 6),
          ("portNum-6", 7),
          ("portNum-7", 8),
          ("portNum-8", 9),
          ("portNum-9", 10),
          ("portNum-10", 11),
          ("portNum-11", 12),
          ("portNum-12", 13),
          ("portNum-13", 14),
          ("portNum-14", 15),
          ("portNum-15", 16))
    )


_SwNbMyPort_Type.__name__ = "Integer32"
_SwNbMyPort_Object = MibTableColumn
swNbMyPort = _SwNbMyPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 2),
    _SwNbMyPort_Type()
)
swNbMyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbMyPort.setStatus("mandatory")
_SwNbRemDomain_Type = SwDomainIndex
_SwNbRemDomain_Object = MibTableColumn
swNbRemDomain = _SwNbRemDomain_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 3),
    _SwNbRemDomain_Type()
)
swNbRemDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemDomain.setStatus("mandatory")


class _SwNbRemPort_Type(Integer32):
    """Custom type swNbRemPort based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("portNum-0", 1),
          ("portNum-1", 2),
          ("portNum-2", 3),
          ("portNum-3", 4),
          ("portNum-4", 5),
          ("portNum-5", 6),
          ("portNum-6", 7),
          ("portNum-7", 8),
          ("portNum-8", 9),
          ("portNum-9", 10),
          ("portNum-10", 11),
          ("portNum-11", 12),
          ("portNum-12", 13),
          ("portNum-13", 14),
          ("portNum-14", 15),
          ("portNum-15", 16))
    )


_SwNbRemPort_Type.__name__ = "Integer32"
_SwNbRemPort_Object = MibTableColumn
swNbRemPort = _SwNbRemPort_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 4),
    _SwNbRemPort_Type()
)
swNbRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbRemPort.setStatus("mandatory")


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
              64)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("oneEighth", 2),
          ("quarter", 4),
          ("half", 8),
          ("full", 16),
          ("double", 32),
          ("quadruple", 64))
    )


_SwNbBaudRate_Type.__name__ = "Integer32"
_SwNbBaudRate_Object = MibTableColumn
swNbBaudRate = _SwNbBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 2, 9, 1, 5),
    _SwNbBaudRate_Type()
)
swNbBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNbBaudRate.setStatus("mandatory")


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
    swNbIslState.setStatus("mandatory")
_SwModule_ObjectIdentity = ObjectIdentity
swModule = _SwModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 3)
)
_SwAgtCfg_ObjectIdentity = ObjectIdentity
swAgtCfg = _SwAgtCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4)
)
_SwAgtCmtyTable_Object = MibTable
swAgtCmtyTable = _SwAgtCmtyTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11)
)
if mibBuilder.loadTexts:
    swAgtCmtyTable.setStatus("mandatory")
_SwAgtCmtyEntry_Object = MibTableRow
swAgtCmtyEntry = _SwAgtCmtyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1)
)
swAgtCmtyEntry.setIndexNames(
    (0, "V21-SW-MIB", "swAgtCmtyIdx"),
)
if mibBuilder.loadTexts:
    swAgtCmtyEntry.setStatus("mandatory")


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
    swAgtCmtyIdx.setStatus("mandatory")


class _SwAgtCmtyStr_Type(DisplayString):
    """Custom type swAgtCmtyStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_SwAgtCmtyStr_Type.__name__ = "DisplayString"
_SwAgtCmtyStr_Object = MibTableColumn
swAgtCmtyStr = _SwAgtCmtyStr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 2),
    _SwAgtCmtyStr_Type()
)
swAgtCmtyStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtCmtyStr.setStatus("mandatory")
_SwAgtTrapRcp_Type = IpAddress
_SwAgtTrapRcp_Object = MibTableColumn
swAgtTrapRcp = _SwAgtTrapRcp_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 4, 11, 1, 3),
    _SwAgtTrapRcp_Type()
)
swAgtTrapRcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAgtTrapRcp.setStatus("mandatory")
_SwFCport_ObjectIdentity = ObjectIdentity
swFCport = _SwFCport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6)
)
_SwFCPortCapacity_Type = Integer32
_SwFCPortCapacity_Object = MibScalar
swFCPortCapacity = _SwFCPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 1),
    _SwFCPortCapacity_Type()
)
swFCPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortCapacity.setStatus("mandatory")
_SwFCPortTable_Object = MibTable
swFCPortTable = _SwFCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    swFCPortTable.setStatus("mandatory")
_SwFCPortEntry_Object = MibTableRow
swFCPortEntry = _SwFCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1)
)
swFCPortEntry.setIndexNames(
    (0, "V21-SW-MIB", "swFCPortIndex"),
)
if mibBuilder.loadTexts:
    swFCPortEntry.setStatus("mandatory")


class _SwFCPortIndex_Type(Integer32):
    """Custom type swFCPortIndex based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("portNum-0", 1),
          ("portNum-1", 2),
          ("portNum-2", 3),
          ("portNum-3", 4),
          ("portNum-4", 5),
          ("portNum-5", 6),
          ("portNum-6", 7),
          ("portNum-7", 8),
          ("portNum-8", 9),
          ("portNum-9", 10),
          ("portNum-10", 11),
          ("portNum-11", 12),
          ("portNum-12", 13),
          ("portNum-13", 14),
          ("portNum-14", 15),
          ("portNum-15", 16))
    )


_SwFCPortIndex_Type.__name__ = "Integer32"
_SwFCPortIndex_Object = MibTableColumn
swFCPortIndex = _SwFCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 1),
    _SwFCPortIndex_Type()
)
swFCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortIndex.setStatus("mandatory")


class _SwFCPortType_Type(Integer32):
    """Custom type swFCPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stitch", 1),
          ("flannel", 2),
          ("loom", 3))
    )


_SwFCPortType_Type.__name__ = "Integer32"
_SwFCPortType_Object = MibTableColumn
swFCPortType = _SwFCPortType_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 2),
    _SwFCPortType_Type()
)
swFCPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortType.setStatus("mandatory")


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
          ("noGbic", 2),
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
    swFCPortPhyState.setStatus("mandatory")


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
    swFCPortOpStatus.setStatus("mandatory")


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
    swFCPortAdmStatus.setStatus("mandatory")


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
    swFCPortLinkState.setStatus("mandatory")


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
    swFCPortTxType.setStatus("mandatory")
_SwFCPortTxWords_Type = Counter32
_SwFCPortTxWords_Object = MibTableColumn
swFCPortTxWords = _SwFCPortTxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 11),
    _SwFCPortTxWords_Type()
)
swFCPortTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxWords.setStatus("mandatory")
_SwFCPortRxWords_Type = Counter32
_SwFCPortRxWords_Object = MibTableColumn
swFCPortRxWords = _SwFCPortRxWords_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 12),
    _SwFCPortRxWords_Type()
)
swFCPortRxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxWords.setStatus("mandatory")
_SwFCPortTxFrames_Type = Counter32
_SwFCPortTxFrames_Object = MibTableColumn
swFCPortTxFrames = _SwFCPortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 13),
    _SwFCPortTxFrames_Type()
)
swFCPortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxFrames.setStatus("mandatory")
_SwFCPortRxFrames_Type = Counter32
_SwFCPortRxFrames_Object = MibTableColumn
swFCPortRxFrames = _SwFCPortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 14),
    _SwFCPortRxFrames_Type()
)
swFCPortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxFrames.setStatus("mandatory")
_SwFCPortTxC2Frames_Type = Counter32
_SwFCPortTxC2Frames_Object = MibTableColumn
swFCPortTxC2Frames = _SwFCPortTxC2Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 15),
    _SwFCPortTxC2Frames_Type()
)
swFCPortTxC2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxC2Frames.setStatus("mandatory")
_SwFCPortRxC3Frames_Type = Counter32
_SwFCPortRxC3Frames_Object = MibTableColumn
swFCPortRxC3Frames = _SwFCPortRxC3Frames_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 16),
    _SwFCPortRxC3Frames_Type()
)
swFCPortRxC3Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxC3Frames.setStatus("mandatory")
_SwFCPortRxLCs_Type = Counter32
_SwFCPortRxLCs_Object = MibTableColumn
swFCPortRxLCs = _SwFCPortRxLCs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 17),
    _SwFCPortRxLCs_Type()
)
swFCPortRxLCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxLCs.setStatus("mandatory")
_SwFCPortRxMcasts_Type = Counter32
_SwFCPortRxMcasts_Object = MibTableColumn
swFCPortRxMcasts = _SwFCPortRxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 18),
    _SwFCPortRxMcasts_Type()
)
swFCPortRxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxMcasts.setStatus("mandatory")
_SwFCPortTooManyRdys_Type = Counter32
_SwFCPortTooManyRdys_Object = MibTableColumn
swFCPortTooManyRdys = _SwFCPortTooManyRdys_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 19),
    _SwFCPortTooManyRdys_Type()
)
swFCPortTooManyRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTooManyRdys.setStatus("mandatory")
_SwFCPortNoTxCredits_Type = Counter32
_SwFCPortNoTxCredits_Object = MibTableColumn
swFCPortNoTxCredits = _SwFCPortNoTxCredits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 20),
    _SwFCPortNoTxCredits_Type()
)
swFCPortNoTxCredits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortNoTxCredits.setStatus("mandatory")
_SwFCPortRxEncInFrs_Type = Counter32
_SwFCPortRxEncInFrs_Object = MibTableColumn
swFCPortRxEncInFrs = _SwFCPortRxEncInFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 21),
    _SwFCPortRxEncInFrs_Type()
)
swFCPortRxEncInFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncInFrs.setStatus("mandatory")
_SwFCPortRxCrcs_Type = Counter32
_SwFCPortRxCrcs_Object = MibTableColumn
swFCPortRxCrcs = _SwFCPortRxCrcs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 22),
    _SwFCPortRxCrcs_Type()
)
swFCPortRxCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxCrcs.setStatus("mandatory")
_SwFCPortRxTruncs_Type = Counter32
_SwFCPortRxTruncs_Object = MibTableColumn
swFCPortRxTruncs = _SwFCPortRxTruncs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 23),
    _SwFCPortRxTruncs_Type()
)
swFCPortRxTruncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTruncs.setStatus("mandatory")
_SwFCPortRxTooLongs_Type = Counter32
_SwFCPortRxTooLongs_Object = MibTableColumn
swFCPortRxTooLongs = _SwFCPortRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 24),
    _SwFCPortRxTooLongs_Type()
)
swFCPortRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxTooLongs.setStatus("mandatory")
_SwFCPortRxBadEofs_Type = Counter32
_SwFCPortRxBadEofs_Object = MibTableColumn
swFCPortRxBadEofs = _SwFCPortRxBadEofs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 25),
    _SwFCPortRxBadEofs_Type()
)
swFCPortRxBadEofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadEofs.setStatus("mandatory")
_SwFCPortRxEncOutFrs_Type = Counter32
_SwFCPortRxEncOutFrs_Object = MibTableColumn
swFCPortRxEncOutFrs = _SwFCPortRxEncOutFrs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 26),
    _SwFCPortRxEncOutFrs_Type()
)
swFCPortRxEncOutFrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxEncOutFrs.setStatus("mandatory")
_SwFCPortRxBadOs_Type = Counter32
_SwFCPortRxBadOs_Object = MibTableColumn
swFCPortRxBadOs = _SwFCPortRxBadOs_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 27),
    _SwFCPortRxBadOs_Type()
)
swFCPortRxBadOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortRxBadOs.setStatus("mandatory")
_SwFCPortC3Discards_Type = Counter32
_SwFCPortC3Discards_Object = MibTableColumn
swFCPortC3Discards = _SwFCPortC3Discards_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 28),
    _SwFCPortC3Discards_Type()
)
swFCPortC3Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortC3Discards.setStatus("mandatory")
_SwFCPortMcastTimedOuts_Type = Counter32
_SwFCPortMcastTimedOuts_Object = MibTableColumn
swFCPortMcastTimedOuts = _SwFCPortMcastTimedOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 29),
    _SwFCPortMcastTimedOuts_Type()
)
swFCPortMcastTimedOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortMcastTimedOuts.setStatus("mandatory")
_SwFCPortTxMcasts_Type = Counter32
_SwFCPortTxMcasts_Object = MibTableColumn
swFCPortTxMcasts = _SwFCPortTxMcasts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 30),
    _SwFCPortTxMcasts_Type()
)
swFCPortTxMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortTxMcasts.setStatus("mandatory")
_SwFCPortLipIns_Type = Counter32
_SwFCPortLipIns_Object = MibTableColumn
swFCPortLipIns = _SwFCPortLipIns_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 31),
    _SwFCPortLipIns_Type()
)
swFCPortLipIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipIns.setStatus("mandatory")
_SwFCPortLipOuts_Type = Counter32
_SwFCPortLipOuts_Object = MibTableColumn
swFCPortLipOuts = _SwFCPortLipOuts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 6, 2, 1, 32),
    _SwFCPortLipOuts_Type()
)
swFCPortLipOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFCPortLipOuts.setStatus("mandatory")


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
    swFCPortLipLastAlpa.setStatus("mandatory")


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
    swFCPortWwn.setStatus("mandatory")
_SwNs_ObjectIdentity = ObjectIdentity
swNs = _SwNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7)
)
_SwNsLocalNumEntry_Type = Integer32
_SwNsLocalNumEntry_Object = MibScalar
swNsLocalNumEntry = _SwNsLocalNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 1),
    _SwNsLocalNumEntry_Type()
)
swNsLocalNumEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsLocalNumEntry.setStatus("mandatory")
_SwNsLocalTable_Object = MibTable
swNsLocalTable = _SwNsLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    swNsLocalTable.setStatus("mandatory")
_SwNsLocalEntry_Object = MibTableRow
swNsLocalEntry = _SwNsLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1)
)
swNsLocalEntry.setIndexNames(
    (0, "V21-SW-MIB", "swNsEntryIndex"),
)
if mibBuilder.loadTexts:
    swNsLocalEntry.setStatus("mandatory")
_SwNsEntryIndex_Type = Integer32
_SwNsEntryIndex_Object = MibTableColumn
swNsEntryIndex = _SwNsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 1),
    _SwNsEntryIndex_Type()
)
swNsEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsEntryIndex.setStatus("mandatory")


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
    swNsPortID.setStatus("mandatory")


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
    swNsPortType.setStatus("mandatory")
_SwNsPortName_Type = FcWwn
_SwNsPortName_Object = MibTableColumn
swNsPortName = _SwNsPortName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 4),
    _SwNsPortName_Type()
)
swNsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortName.setStatus("mandatory")


class _SwNsPortSymb_Type(OctetString):
    """Custom type swNsPortSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwNsPortSymb_Type.__name__ = "OctetString"
_SwNsPortSymb_Object = MibTableColumn
swNsPortSymb = _SwNsPortSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 5),
    _SwNsPortSymb_Type()
)
swNsPortSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsPortSymb.setStatus("mandatory")
_SwNsNodeName_Type = FcWwn
_SwNsNodeName_Object = MibTableColumn
swNsNodeName = _SwNsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 6),
    _SwNsNodeName_Type()
)
swNsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeName.setStatus("mandatory")


class _SwNsNodeSymb_Type(OctetString):
    """Custom type swNsNodeSymb based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SwNsNodeSymb_Type.__name__ = "OctetString"
_SwNsNodeSymb_Object = MibTableColumn
swNsNodeSymb = _SwNsNodeSymb_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 7, 2, 1, 7),
    _SwNsNodeSymb_Type()
)
swNsNodeSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swNsNodeSymb.setStatus("mandatory")


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
    swNsIPA.setStatus("mandatory")


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
    swNsIpAddress.setStatus("mandatory")


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
    swNsCos.setStatus("mandatory")


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
    swNsFc4.setStatus("mandatory")
_SwEvent_ObjectIdentity = ObjectIdentity
swEvent = _SwEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8)
)


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
    swEventTrapLevel.setStatus("mandatory")


class _SwEventNumEntries_Type(Integer32):
    """Custom type swEventNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SwEventNumEntries_Type.__name__ = "Integer32"
_SwEventNumEntries_Object = MibScalar
swEventNumEntries = _SwEventNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 4),
    _SwEventNumEntries_Type()
)
swEventNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventNumEntries.setStatus("mandatory")
_SwEventTable_Object = MibTable
swEventTable = _SwEventTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    swEventTable.setStatus("mandatory")
_SwEventEntry_Object = MibTableRow
swEventEntry = _SwEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1)
)
swEventEntry.setIndexNames(
    (0, "V21-SW-MIB", "swEventIndex"),
)
if mibBuilder.loadTexts:
    swEventEntry.setStatus("mandatory")


class _SwEventIndex_Type(Integer32):
    """Custom type swEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SwEventIndex_Type.__name__ = "Integer32"
_SwEventIndex_Object = MibTableColumn
swEventIndex = _SwEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 1),
    _SwEventIndex_Type()
)
swEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventIndex.setStatus("mandatory")
_SwEventTimeInfo_Type = DisplayString
_SwEventTimeInfo_Object = MibTableColumn
swEventTimeInfo = _SwEventTimeInfo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 2),
    _SwEventTimeInfo_Type()
)
swEventTimeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventTimeInfo.setStatus("mandatory")


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
    swEventLevel.setStatus("mandatory")
_SwEventRepeatCount_Type = Integer32
_SwEventRepeatCount_Object = MibTableColumn
swEventRepeatCount = _SwEventRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 4),
    _SwEventRepeatCount_Type()
)
swEventRepeatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventRepeatCount.setStatus("mandatory")
_SwEventDescr_Type = DisplayString
_SwEventDescr_Object = MibTableColumn
swEventDescr = _SwEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1, 8, 5, 1, 5),
    _SwEventDescr_Type()
)
swEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEventDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "V21-SW-MIB",
    **{"DisplayString": DisplayString,
       "FcWwn": FcWwn,
       "SwDomainIndex": SwDomainIndex,
       "SwNbIndex": SwNbIndex,
       "SwSensorIndex": SwSensorIndex,
       "bcsi": bcsi,
       "commDev": commDev,
       "fibrechannel": fibrechannel,
       "fcSwitch": fcSwitch,
       "sw": sw,
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
       "swFlashDLOperStatus": swFlashDLOperStatus,
       "swFlashDLAdmStatus": swFlashDLAdmStatus,
       "swFlashDLHost": swFlashDLHost,
       "swFlashDLUser": swFlashDLUser,
       "swFlashDLFile": swFlashDLFile,
       "swDiagResult": swDiagResult,
       "swNumSensors": swNumSensors,
       "swSensorTable": swSensorTable,
       "swSensorEntry": swSensorEntry,
       "swSensorIndex": swSensorIndex,
       "swSensorType": swSensorType,
       "swSensorStatus": swSensorStatus,
       "swSensorValue": swSensorValue,
       "swSensorInfo": swSensorInfo,
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
       "swModule": swModule,
       "swAgtCfg": swAgtCfg,
       "swAgtCmtyTable": swAgtCmtyTable,
       "swAgtCmtyEntry": swAgtCmtyEntry,
       "swAgtCmtyIdx": swAgtCmtyIdx,
       "swAgtCmtyStr": swAgtCmtyStr,
       "swAgtTrapRcp": swAgtTrapRcp,
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
       "swFCPortTxC2Frames": swFCPortTxC2Frames,
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
       "swEvent": swEvent,
       "swEventTrapLevel": swEventTrapLevel,
       "swEventNumEntries": swEventNumEntries,
       "swEventTable": swEventTable,
       "swEventEntry": swEventEntry,
       "swEventIndex": swEventIndex,
       "swEventTimeInfo": swEventTimeInfo,
       "swEventLevel": swEventLevel,
       "swEventRepeatCount": swEventRepeatCount,
       "swEventDescr": swEventDescr}
)
