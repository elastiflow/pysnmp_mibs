# SNMP MIB module (GMS-ELEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/esa_162/GMS-ELEMENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:16:25 2025
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

(gms,) = mibBuilder.importSymbols(
    "GALILEO-SMI",
    "gms")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

gmsElementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1)
)
if mibBuilder.loadTexts:
    gmsElementMIB.setRevisions(
        ("2011-11-09 00:00",
         "2011-10-10 00:00",
         "2011-06-17 00:00",
         "2011-05-02 00:00",
         "2010-11-25 00:00",
         "2010-11-10 00:00",
         "2010-10-01 00:00",
         "2010-09-30 00:00",
         "2010-09-29 00:00",
         "2010-09-27 00:00",
         "2007-05-23 00:00",
         "2007-05-22 00:00",
         "2007-05-03 00:00",
         "2007-03-14 00:00",
         "2007-02-20 00:00",
         "2007-02-12 00:00",
         "2006-09-20 01:00",
         "2006-09-20 00:00",
         "2006-09-19 00:00",
         "2006-09-01 00:00",
         "2006-06-08 00:00",
         "2006-04-21 00:00",
         "2006-03-28 00:00",
         "2006-03-24 00:00",
         "2006-03-10 00:00",
         "2006-02-15 22:00",
         "2006-01-31 00:00",
         "2006-01-18 00:00",
         "2005-10-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CommandId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


class CommandState(TextualConvention, Integer32):
    status = "current"
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
        *(("notActive", 1),
          ("notAccepted", 2),
          ("active", 3),
          ("failed", 4),
          ("cancelled", 5),
          ("completed", 6),
          ("requiresConfirmation", 7))
    )



class CommandSource(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              10)
        )
    )
    namedValues = NamedValues(
        *(("gcc11", 1),
          ("gcc12", 2),
          ("gcc21", 3),
          ("gcc22", 4),
          ("gcc31", 5),
          ("gcc32", 6),
          ("lme", 10))
    )



class ElementSite(TextualConvention, OctetString):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class ElementState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 1),
          ("operational", 2),
          ("notApplicable", 3))
    )



class ConnectionState(TextualConvention, Integer32):
    status = "current"
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
        *(("notConnected", 1),
          ("connected", 2),
          ("standby", 3),
          ("notApplicable", 4),
          ("failed", 5))
    )



class ConnectionMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("notApplicable", 3))
    )



class MIBVersion(TextualConvention, OctetString):
    status = "current"
    displayHint = "13a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )
    fixed_length = 13



class OptionalMIBVersion(TextualConvention, OctetString):
    status = "current"
    displayHint = "13a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(13, 13),
    )



class ElementMode(TextualConvention, Integer32):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("loaded", 2),
          ("running", 3),
          ("failed", 4),
          ("test", 5),
          ("operational", 6),
          ("operationalSlave", 7),
          ("initialised", 8),
          ("operationalAutonomous", 9),
          ("runningSlave", 10),
          ("runningAutonomous", 11),
          ("emulation", 12),
          ("notApplicable", 13))
    )



class ElementIntegrity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("successful", 1),
          ("warnings", 2),
          ("failed", 3))
    )



class CommandType(TextualConvention, Integer32):
    status = "current"
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("cmdElmtModeChg", 1),
          ("cmdElmtAlertFilter", 2),
          ("cmdLogFileExtract", 3),
          ("cmdTestPortActivateRqst", 4),
          ("cmdTestCmd", 5),
          ("cmdSwDownloadRqst", 6),
          ("archMigrRqst", 7),
          ("cmdSwIntegrityRqst", 8),
          ("secFtpKeyChange", 10),
          ("cmdInstall", 11),
          ("cmdElmtModeChgOpe", 12))
    )



class Boolean(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class SWRUType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("executable", 0),
          ("configurationFile", 1),
          ("configurationDatabase", 2))
    )



class SWRUStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("statusUnknown", -1),
          ("statusOff", 0),
          ("statusStarting", 1),
          ("statusOn", 2),
          ("statusStopping", 3),
          ("statusDegraded", 4),
          ("statusStandby", 5),
          ("statusSwitch", 6))
    )



class SWRUVersion(TextualConvention, OctetString):
    status = "current"
    displayHint = "12a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12



class BITType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bitTypeUnknown", -1),
          ("bitTypePowerOn", 0),
          ("bitTypeContinuous", 1),
          ("bitTypeOnDemand", 2))
    )



class BITResultType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bitTypeResultUnknown", -1),
          ("bitTypeEnumeration", 0),
          ("bitTypeTimestamp", 1))
    )



class OSIdentifierType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("osTypeUnknown", -1),
          ("osRHEL4", 0),
          ("osRHEL5", 1),
          ("osRHEL6", 2),
          ("osLynxOS178", 3),
          ("osOther", 4))
    )



# MIB Managed Objects in the order of their OIDs

_MibVersions_ObjectIdentity = ObjectIdentity
mibVersions = _MibVersions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 1)
)
_ElemMibVersion_Type = MIBVersion
_ElemMibVersion_Object = MibScalar
elemMibVersion = _ElemMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 1, 1),
    _ElemMibVersion_Type()
)
elemMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemMibVersion.setStatus("current")
_ElemMibVersionSpecific_Type = OptionalMIBVersion
_ElemMibVersionSpecific_Object = MibScalar
elemMibVersionSpecific = _ElemMibVersionSpecific_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 1, 2),
    _ElemMibVersionSpecific_Type()
)
elemMibVersionSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemMibVersionSpecific.setStatus("current")
_ElemStatus_ObjectIdentity = ObjectIdentity
elemStatus = _ElemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2)
)
_ElemStatusState_Type = ElementState
_ElemStatusState_Object = MibScalar
elemStatusState = _ElemStatusState_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 1),
    _ElemStatusState_Type()
)
elemStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusState.setStatus("current")
_ElemStatusLastStateChange_Type = DateAndTime
_ElemStatusLastStateChange_Object = MibScalar
elemStatusLastStateChange = _ElemStatusLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 2),
    _ElemStatusLastStateChange_Type()
)
elemStatusLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusLastStateChange.setStatus("current")
_ElemStatusMode_Type = ElementMode
_ElemStatusMode_Object = MibScalar
elemStatusMode = _ElemStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 3),
    _ElemStatusMode_Type()
)
elemStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusMode.setStatus("current")
_ElemStatusLastModeChange_Type = DateAndTime
_ElemStatusLastModeChange_Object = MibScalar
elemStatusLastModeChange = _ElemStatusLastModeChange_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 4),
    _ElemStatusLastModeChange_Type()
)
elemStatusLastModeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusLastModeChange.setStatus("current")
_ElemStatusIntegrity_Type = ElementIntegrity
_ElemStatusIntegrity_Object = MibScalar
elemStatusIntegrity = _ElemStatusIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 5),
    _ElemStatusIntegrity_Type()
)
elemStatusIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusIntegrity.setStatus("current")
_ElemStatusLastIntegrityCheck_Type = DateAndTime
_ElemStatusLastIntegrityCheck_Object = MibScalar
elemStatusLastIntegrityCheck = _ElemStatusLastIntegrityCheck_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 6),
    _ElemStatusLastIntegrityCheck_Type()
)
elemStatusLastIntegrityCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusLastIntegrityCheck.setStatus("current")
_ElemStatusIntegrityLowLevel_Type = ElementIntegrity
_ElemStatusIntegrityLowLevel_Object = MibScalar
elemStatusIntegrityLowLevel = _ElemStatusIntegrityLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 7),
    _ElemStatusIntegrityLowLevel_Type()
)
elemStatusIntegrityLowLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusIntegrityLowLevel.setStatus("current")
_ElemStatusLastIntegrityLowLevelCheck_Type = DateAndTime
_ElemStatusLastIntegrityLowLevelCheck_Object = MibScalar
elemStatusLastIntegrityLowLevelCheck = _ElemStatusLastIntegrityLowLevelCheck_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 2, 8),
    _ElemStatusLastIntegrityLowLevelCheck_Type()
)
elemStatusLastIntegrityLowLevelCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemStatusLastIntegrityLowLevelCheck.setStatus("current")
_ElemInfo_ObjectIdentity = ObjectIdentity
elemInfo = _ElemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 3)
)
_ElemInfoSite_Type = ElementSite
_ElemInfoSite_Object = MibScalar
elemInfoSite = _ElemInfoSite_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 3, 1),
    _ElemInfoSite_Type()
)
elemInfoSite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemInfoSite.setStatus("current")
_ElemInfoInstance_Type = Unsigned32
_ElemInfoInstance_Object = MibScalar
elemInfoInstance = _ElemInfoInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 3, 2),
    _ElemInfoInstance_Type()
)
elemInfoInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemInfoInstance.setStatus("current")


class _ElemInfoName_Type(DisplayString):
    """Custom type elemInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElemInfoName_Type.__name__ = "DisplayString"
_ElemInfoName_Object = MibScalar
elemInfoName = _ElemInfoName_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 3, 3),
    _ElemInfoName_Type()
)
elemInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemInfoName.setStatus("current")
_ElemSw_ObjectIdentity = ObjectIdentity
elemSw = _ElemSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4)
)
_ElemConfigParameters_ObjectIdentity = ObjectIdentity
elemConfigParameters = _ElemConfigParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1)
)
_ElemConfigParamTable_Object = MibTable
elemConfigParamTable = _ElemConfigParamTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    elemConfigParamTable.setStatus("current")
_ElemConfigParamEntry_Object = MibTableRow
elemConfigParamEntry = _ElemConfigParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1, 1, 1)
)
elemConfigParamEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemConfigParamId"),
    (0, "GMS-ELEMENT-MIB", "elemConfigParamInstance"),
)
if mibBuilder.loadTexts:
    elemConfigParamEntry.setStatus("current")


class _ElemConfigParamInstance_Type(Integer32):
    """Custom type elemConfigParamInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemConfigParamInstance_Type.__name__ = "Integer32"
_ElemConfigParamInstance_Object = MibTableColumn
elemConfigParamInstance = _ElemConfigParamInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1, 1, 1, 1),
    _ElemConfigParamInstance_Type()
)
elemConfigParamInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemConfigParamInstance.setStatus("current")


class _ElemConfigParamId_Type(DisplayString):
    """Custom type elemConfigParamId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ElemConfigParamId_Type.__name__ = "DisplayString"
_ElemConfigParamId_Object = MibTableColumn
elemConfigParamId = _ElemConfigParamId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1, 1, 1, 2),
    _ElemConfigParamId_Type()
)
elemConfigParamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemConfigParamId.setStatus("current")
_ElemConfigParamValue_Type = DisplayString
_ElemConfigParamValue_Object = MibTableColumn
elemConfigParamValue = _ElemConfigParamValue_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 1, 1, 1, 4),
    _ElemConfigParamValue_Type()
)
elemConfigParamValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemConfigParamValue.setStatus("current")
_ElemComponentInfo_ObjectIdentity = ObjectIdentity
elemComponentInfo = _ElemComponentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2)
)
_ElemComponentInfoTable_Object = MibTable
elemComponentInfoTable = _ElemComponentInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    elemComponentInfoTable.setStatus("current")
_ElemComponentInfoEntry_Object = MibTableRow
elemComponentInfoEntry = _ElemComponentInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1)
)
elemComponentInfoEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemComponentId"),
    (0, "GMS-ELEMENT-MIB", "elemComponentInstance"),
)
if mibBuilder.loadTexts:
    elemComponentInfoEntry.setStatus("current")


class _ElemComponentInstance_Type(Integer32):
    """Custom type elemComponentInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemComponentInstance_Type.__name__ = "Integer32"
_ElemComponentInstance_Object = MibTableColumn
elemComponentInstance = _ElemComponentInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 1),
    _ElemComponentInstance_Type()
)
elemComponentInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemComponentInstance.setStatus("current")


class _ElemComponentId_Type(DisplayString):
    """Custom type elemComponentId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ElemComponentId_Type.__name__ = "DisplayString"
_ElemComponentId_Object = MibTableColumn
elemComponentId = _ElemComponentId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 2),
    _ElemComponentId_Type()
)
elemComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemComponentId.setStatus("current")
_ElemComponentState_Type = ElementState
_ElemComponentState_Object = MibTableColumn
elemComponentState = _ElemComponentState_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 3),
    _ElemComponentState_Type()
)
elemComponentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemComponentState.setStatus("current")
_ElemComponentLastStateChange_Type = DateAndTime
_ElemComponentLastStateChange_Object = MibTableColumn
elemComponentLastStateChange = _ElemComponentLastStateChange_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 4),
    _ElemComponentLastStateChange_Type()
)
elemComponentLastStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemComponentLastStateChange.setStatus("current")
_ElemComponentMode_Type = ElementMode
_ElemComponentMode_Object = MibTableColumn
elemComponentMode = _ElemComponentMode_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 5),
    _ElemComponentMode_Type()
)
elemComponentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemComponentMode.setStatus("current")
_ElemComponentLastModeChange_Type = DateAndTime
_ElemComponentLastModeChange_Object = MibTableColumn
elemComponentLastModeChange = _ElemComponentLastModeChange_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 6),
    _ElemComponentLastModeChange_Type()
)
elemComponentLastModeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemComponentLastModeChange.setStatus("current")
_ElemComponentVersion_Type = DisplayString
_ElemComponentVersion_Object = MibTableColumn
elemComponentVersion = _ElemComponentVersion_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 2, 1, 1, 7),
    _ElemComponentVersion_Type()
)
elemComponentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemComponentVersion.setStatus("current")
_ElemSWRUActive_ObjectIdentity = ObjectIdentity
elemSWRUActive = _ElemSWRUActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3)
)
_ElemSWRUActiveTable_Object = MibTable
elemSWRUActiveTable = _ElemSWRUActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    elemSWRUActiveTable.setStatus("current")
_ElemSWRUActiveEntry_Object = MibTableRow
elemSWRUActiveEntry = _ElemSWRUActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1)
)
elemSWRUActiveEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemSWRUActiveId"),
    (0, "GMS-ELEMENT-MIB", "elemSWRUActiveInstance"),
)
if mibBuilder.loadTexts:
    elemSWRUActiveEntry.setStatus("current")


class _ElemSWRUActiveInstance_Type(Integer32):
    """Custom type elemSWRUActiveInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemSWRUActiveInstance_Type.__name__ = "Integer32"
_ElemSWRUActiveInstance_Object = MibTableColumn
elemSWRUActiveInstance = _ElemSWRUActiveInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 1),
    _ElemSWRUActiveInstance_Type()
)
elemSWRUActiveInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemSWRUActiveInstance.setStatus("current")


class _ElemSWRUActiveId_Type(DisplayString):
    """Custom type elemSWRUActiveId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ElemSWRUActiveId_Type.__name__ = "DisplayString"
_ElemSWRUActiveId_Object = MibTableColumn
elemSWRUActiveId = _ElemSWRUActiveId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 2),
    _ElemSWRUActiveId_Type()
)
elemSWRUActiveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemSWRUActiveId.setStatus("current")
_ElemSWRUActiveVersion_Type = SWRUVersion
_ElemSWRUActiveVersion_Object = MibTableColumn
elemSWRUActiveVersion = _ElemSWRUActiveVersion_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 3),
    _ElemSWRUActiveVersion_Type()
)
elemSWRUActiveVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSWRUActiveVersion.setStatus("current")
_ElemSWRUActiveUpTime_Type = TimeTicks
_ElemSWRUActiveUpTime_Object = MibTableColumn
elemSWRUActiveUpTime = _ElemSWRUActiveUpTime_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 4),
    _ElemSWRUActiveUpTime_Type()
)
elemSWRUActiveUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSWRUActiveUpTime.setStatus("current")
_ElemSWRUActiveType_Type = SWRUType
_ElemSWRUActiveType_Object = MibTableColumn
elemSWRUActiveType = _ElemSWRUActiveType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 5),
    _ElemSWRUActiveType_Type()
)
elemSWRUActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSWRUActiveType.setStatus("current")
_ElemSWRUActiveStatus_Type = SWRUStatus
_ElemSWRUActiveStatus_Object = MibTableColumn
elemSWRUActiveStatus = _ElemSWRUActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 3, 1, 1, 6),
    _ElemSWRUActiveStatus_Type()
)
elemSWRUActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSWRUActiveStatus.setStatus("current")
_ElemSWRUAvailable_ObjectIdentity = ObjectIdentity
elemSWRUAvailable = _ElemSWRUAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4)
)
_ElemSWRUAvailableTable_Object = MibTable
elemSWRUAvailableTable = _ElemSWRUAvailableTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    elemSWRUAvailableTable.setStatus("current")
_ElemSWRUAvailableEntry_Object = MibTableRow
elemSWRUAvailableEntry = _ElemSWRUAvailableEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2, 1)
)
elemSWRUAvailableEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemSWRUAvailableId"),
    (0, "GMS-ELEMENT-MIB", "elemSWRUAvailableVersion"),
    (0, "GMS-ELEMENT-MIB", "elemSWRUAvailableInstance"),
)
if mibBuilder.loadTexts:
    elemSWRUAvailableEntry.setStatus("current")


class _ElemSWRUAvailableId_Type(DisplayString):
    """Custom type elemSWRUAvailableId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ElemSWRUAvailableId_Type.__name__ = "DisplayString"
_ElemSWRUAvailableId_Object = MibTableColumn
elemSWRUAvailableId = _ElemSWRUAvailableId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2, 1, 1),
    _ElemSWRUAvailableId_Type()
)
elemSWRUAvailableId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemSWRUAvailableId.setStatus("current")
_ElemSWRUAvailableVersion_Type = SWRUVersion
_ElemSWRUAvailableVersion_Object = MibTableColumn
elemSWRUAvailableVersion = _ElemSWRUAvailableVersion_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2, 1, 2),
    _ElemSWRUAvailableVersion_Type()
)
elemSWRUAvailableVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemSWRUAvailableVersion.setStatus("current")


class _ElemSWRUAvailableInstance_Type(Integer32):
    """Custom type elemSWRUAvailableInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ElemSWRUAvailableInstance_Type.__name__ = "Integer32"
_ElemSWRUAvailableInstance_Object = MibTableColumn
elemSWRUAvailableInstance = _ElemSWRUAvailableInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2, 1, 3),
    _ElemSWRUAvailableInstance_Type()
)
elemSWRUAvailableInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemSWRUAvailableInstance.setStatus("current")
_ElemSWRUAvailableType_Type = SWRUType
_ElemSWRUAvailableType_Object = MibTableColumn
elemSWRUAvailableType = _ElemSWRUAvailableType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 4, 2, 1, 4),
    _ElemSWRUAvailableType_Type()
)
elemSWRUAvailableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSWRUAvailableType.setStatus("current")
_ElemConnectionsTable_Object = MibTable
elemConnectionsTable = _ElemConnectionsTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    elemConnectionsTable.setStatus("current")
_ElemConnectionsEntry_Object = MibTableRow
elemConnectionsEntry = _ElemConnectionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1)
)
elemConnectionsEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemConnectionId"),
    (0, "GMS-ELEMENT-MIB", "elemConnectionInstance"),
)
if mibBuilder.loadTexts:
    elemConnectionsEntry.setStatus("current")


class _ElemConnectionInstance_Type(Integer32):
    """Custom type elemConnectionInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemConnectionInstance_Type.__name__ = "Integer32"
_ElemConnectionInstance_Object = MibTableColumn
elemConnectionInstance = _ElemConnectionInstance_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 1),
    _ElemConnectionInstance_Type()
)
elemConnectionInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemConnectionInstance.setStatus("current")


class _ElemConnectionId_Type(DisplayString):
    """Custom type elemConnectionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ElemConnectionId_Type.__name__ = "DisplayString"
_ElemConnectionId_Object = MibTableColumn
elemConnectionId = _ElemConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 2),
    _ElemConnectionId_Type()
)
elemConnectionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemConnectionId.setStatus("current")
_ElemConnectionState_Type = ConnectionState
_ElemConnectionState_Object = MibTableColumn
elemConnectionState = _ElemConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 3),
    _ElemConnectionState_Type()
)
elemConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemConnectionState.setStatus("current")
_ElemConnectionMode_Type = ConnectionMode
_ElemConnectionMode_Object = MibTableColumn
elemConnectionMode = _ElemConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 4),
    _ElemConnectionMode_Type()
)
elemConnectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemConnectionMode.setStatus("current")
_ElemConnectionUpTime_Type = TimeTicks
_ElemConnectionUpTime_Object = MibTableColumn
elemConnectionUpTime = _ElemConnectionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 5),
    _ElemConnectionUpTime_Type()
)
elemConnectionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemConnectionUpTime.setStatus("current")
_ElemConnectionDataRate_Type = Unsigned32
_ElemConnectionDataRate_Object = MibTableColumn
elemConnectionDataRate = _ElemConnectionDataRate_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 4, 5, 1, 6),
    _ElemConnectionDataRate_Type()
)
elemConnectionDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemConnectionDataRate.setStatus("current")
_ElemHw_ObjectIdentity = ObjectIdentity
elemHw = _ElemHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5)
)
_ElemHwPlatTable_Object = MibTable
elemHwPlatTable = _ElemHwPlatTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    elemHwPlatTable.setStatus("current")
_ElemHwPlatEntry_Object = MibTableRow
elemHwPlatEntry = _ElemHwPlatEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1)
)
elemHwPlatEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemHwPlatIndex"),
)
if mibBuilder.loadTexts:
    elemHwPlatEntry.setStatus("current")


class _ElemHwPlatIndex_Type(Integer32):
    """Custom type elemHwPlatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ElemHwPlatIndex_Type.__name__ = "Integer32"
_ElemHwPlatIndex_Object = MibTableColumn
elemHwPlatIndex = _ElemHwPlatIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 1),
    _ElemHwPlatIndex_Type()
)
elemHwPlatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemHwPlatIndex.setStatus("current")
_ElemHwPlatHrSystemUptime_Type = TimeTicks
_ElemHwPlatHrSystemUptime_Object = MibTableColumn
elemHwPlatHrSystemUptime = _ElemHwPlatHrSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 2),
    _ElemHwPlatHrSystemUptime_Type()
)
elemHwPlatHrSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatHrSystemUptime.setStatus("current")
_ElemHwPlatHrSystemDate_Type = DateAndTime
_ElemHwPlatHrSystemDate_Object = MibTableColumn
elemHwPlatHrSystemDate = _ElemHwPlatHrSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 3),
    _ElemHwPlatHrSystemDate_Type()
)
elemHwPlatHrSystemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatHrSystemDate.setStatus("current")
_ElemHwPlatHrSystemNumUsers_Type = Gauge32
_ElemHwPlatHrSystemNumUsers_Object = MibTableColumn
elemHwPlatHrSystemNumUsers = _ElemHwPlatHrSystemNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 4),
    _ElemHwPlatHrSystemNumUsers_Type()
)
elemHwPlatHrSystemNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatHrSystemNumUsers.setStatus("current")
_ElemHwPlatHrSystemProcesses_Type = Gauge32
_ElemHwPlatHrSystemProcesses_Object = MibTableColumn
elemHwPlatHrSystemProcesses = _ElemHwPlatHrSystemProcesses_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 5),
    _ElemHwPlatHrSystemProcesses_Type()
)
elemHwPlatHrSystemProcesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatHrSystemProcesses.setStatus("current")


class _ElemHwPlatSysName_Type(DisplayString):
    """Custom type elemHwPlatSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElemHwPlatSysName_Type.__name__ = "DisplayString"
_ElemHwPlatSysName_Object = MibTableColumn
elemHwPlatSysName = _ElemHwPlatSysName_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 6),
    _ElemHwPlatSysName_Type()
)
elemHwPlatSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatSysName.setStatus("current")


class _ElemHwPlatSysContact_Type(DisplayString):
    """Custom type elemHwPlatSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ElemHwPlatSysContact_Type.__name__ = "DisplayString"
_ElemHwPlatSysContact_Object = MibTableColumn
elemHwPlatSysContact = _ElemHwPlatSysContact_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 7),
    _ElemHwPlatSysContact_Type()
)
elemHwPlatSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatSysContact.setStatus("current")
_ElemHwPlatHrLastReachable_Type = DateAndTime
_ElemHwPlatHrLastReachable_Object = MibTableColumn
elemHwPlatHrLastReachable = _ElemHwPlatHrLastReachable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 8),
    _ElemHwPlatHrLastReachable_Type()
)
elemHwPlatHrLastReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatHrLastReachable.setStatus("current")
_ElemHwPlatCpuUser_Type = Counter32
_ElemHwPlatCpuUser_Object = MibTableColumn
elemHwPlatCpuUser = _ElemHwPlatCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 9),
    _ElemHwPlatCpuUser_Type()
)
elemHwPlatCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatCpuUser.setStatus("current")
_ElemHwPlatCpuNice_Type = Counter32
_ElemHwPlatCpuNice_Object = MibTableColumn
elemHwPlatCpuNice = _ElemHwPlatCpuNice_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 10),
    _ElemHwPlatCpuNice_Type()
)
elemHwPlatCpuNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatCpuNice.setStatus("current")
_ElemHwPlatCpuSystem_Type = Counter32
_ElemHwPlatCpuSystem_Object = MibTableColumn
elemHwPlatCpuSystem = _ElemHwPlatCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 11),
    _ElemHwPlatCpuSystem_Type()
)
elemHwPlatCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatCpuSystem.setStatus("current")
_ElemHwPlatCpuIdle_Type = Counter32
_ElemHwPlatCpuIdle_Object = MibTableColumn
elemHwPlatCpuIdle = _ElemHwPlatCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 12),
    _ElemHwPlatCpuIdle_Type()
)
elemHwPlatCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatCpuIdle.setStatus("current")
_ElemHwPlatMemSize_Type = Unsigned32
_ElemHwPlatMemSize_Object = MibTableColumn
elemHwPlatMemSize = _ElemHwPlatMemSize_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 13),
    _ElemHwPlatMemSize_Type()
)
elemHwPlatMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatMemSize.setStatus("current")
_ElemHwPlatMemUsed_Type = Unsigned32
_ElemHwPlatMemUsed_Object = MibTableColumn
elemHwPlatMemUsed = _ElemHwPlatMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 14),
    _ElemHwPlatMemUsed_Type()
)
elemHwPlatMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatMemUsed.setStatus("current")
_ElemHwPlatMemAvail_Type = Unsigned32
_ElemHwPlatMemAvail_Object = MibTableColumn
elemHwPlatMemAvail = _ElemHwPlatMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 15),
    _ElemHwPlatMemAvail_Type()
)
elemHwPlatMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatMemAvail.setStatus("current")


class _ElemHwPlatMemUsedPercent_Type(Integer32):
    """Custom type elemHwPlatMemUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwPlatMemUsedPercent_Type.__name__ = "Integer32"
_ElemHwPlatMemUsedPercent_Object = MibTableColumn
elemHwPlatMemUsedPercent = _ElemHwPlatMemUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 16),
    _ElemHwPlatMemUsedPercent_Type()
)
elemHwPlatMemUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatMemUsedPercent.setStatus("current")


class _ElemHwPlatMemAvailPercent_Type(Integer32):
    """Custom type elemHwPlatMemAvailPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwPlatMemAvailPercent_Type.__name__ = "Integer32"
_ElemHwPlatMemAvailPercent_Object = MibTableColumn
elemHwPlatMemAvailPercent = _ElemHwPlatMemAvailPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 17),
    _ElemHwPlatMemAvailPercent_Type()
)
elemHwPlatMemAvailPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatMemAvailPercent.setStatus("current")
_ElemHwPlatVirtualMemSize_Type = Unsigned32
_ElemHwPlatVirtualMemSize_Object = MibTableColumn
elemHwPlatVirtualMemSize = _ElemHwPlatVirtualMemSize_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 18),
    _ElemHwPlatVirtualMemSize_Type()
)
elemHwPlatVirtualMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatVirtualMemSize.setStatus("current")
_ElemHwPlatVirtualMemUsed_Type = Unsigned32
_ElemHwPlatVirtualMemUsed_Object = MibTableColumn
elemHwPlatVirtualMemUsed = _ElemHwPlatVirtualMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 19),
    _ElemHwPlatVirtualMemUsed_Type()
)
elemHwPlatVirtualMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatVirtualMemUsed.setStatus("current")
_ElemHwPlatVirtualMemAvail_Type = Unsigned32
_ElemHwPlatVirtualMemAvail_Object = MibTableColumn
elemHwPlatVirtualMemAvail = _ElemHwPlatVirtualMemAvail_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 20),
    _ElemHwPlatVirtualMemAvail_Type()
)
elemHwPlatVirtualMemAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatVirtualMemAvail.setStatus("current")


class _ElemHwPlatVirtualMemUsedPercent_Type(Integer32):
    """Custom type elemHwPlatVirtualMemUsedPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwPlatVirtualMemUsedPercent_Type.__name__ = "Integer32"
_ElemHwPlatVirtualMemUsedPercent_Object = MibTableColumn
elemHwPlatVirtualMemUsedPercent = _ElemHwPlatVirtualMemUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 21),
    _ElemHwPlatVirtualMemUsedPercent_Type()
)
elemHwPlatVirtualMemUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatVirtualMemUsedPercent.setStatus("current")


class _ElemHwPlatVirtualMemAvailPercent_Type(Integer32):
    """Custom type elemHwPlatVirtualMemAvailPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwPlatVirtualMemAvailPercent_Type.__name__ = "Integer32"
_ElemHwPlatVirtualMemAvailPercent_Object = MibTableColumn
elemHwPlatVirtualMemAvailPercent = _ElemHwPlatVirtualMemAvailPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 22),
    _ElemHwPlatVirtualMemAvailPercent_Type()
)
elemHwPlatVirtualMemAvailPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatVirtualMemAvailPercent.setStatus("current")


class _ElemHwPlatSystemLoad1_Type(Integer32):
    """Custom type elemHwPlatSystemLoad1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ElemHwPlatSystemLoad1_Type.__name__ = "Integer32"
_ElemHwPlatSystemLoad1_Object = MibTableColumn
elemHwPlatSystemLoad1 = _ElemHwPlatSystemLoad1_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 23),
    _ElemHwPlatSystemLoad1_Type()
)
elemHwPlatSystemLoad1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatSystemLoad1.setStatus("current")


class _ElemHwPlatSystemLoad2_Type(Integer32):
    """Custom type elemHwPlatSystemLoad2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ElemHwPlatSystemLoad2_Type.__name__ = "Integer32"
_ElemHwPlatSystemLoad2_Object = MibTableColumn
elemHwPlatSystemLoad2 = _ElemHwPlatSystemLoad2_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 24),
    _ElemHwPlatSystemLoad2_Type()
)
elemHwPlatSystemLoad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatSystemLoad2.setStatus("current")


class _ElemHwPlatSystemLoad3_Type(Integer32):
    """Custom type elemHwPlatSystemLoad3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ElemHwPlatSystemLoad3_Type.__name__ = "Integer32"
_ElemHwPlatSystemLoad3_Object = MibTableColumn
elemHwPlatSystemLoad3 = _ElemHwPlatSystemLoad3_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 25),
    _ElemHwPlatSystemLoad3_Type()
)
elemHwPlatSystemLoad3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatSystemLoad3.setStatus("current")
_ElemHwPlatOsIdentifier_Type = OSIdentifierType
_ElemHwPlatOsIdentifier_Object = MibTableColumn
elemHwPlatOsIdentifier = _ElemHwPlatOsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 1, 1, 26),
    _ElemHwPlatOsIdentifier_Type()
)
elemHwPlatOsIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwPlatOsIdentifier.setStatus("current")
_ElemHwDskTable_Object = MibTable
elemHwDskTable = _ElemHwDskTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    elemHwDskTable.setStatus("current")
_ElemHwDskEntry_Object = MibTableRow
elemHwDskEntry = _ElemHwDskEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1)
)
elemHwDskEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemHwDskIndex"),
)
if mibBuilder.loadTexts:
    elemHwDskEntry.setStatus("current")


class _ElemHwDskIndex_Type(Integer32):
    """Custom type elemHwDskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ElemHwDskIndex_Type.__name__ = "Integer32"
_ElemHwDskIndex_Object = MibTableColumn
elemHwDskIndex = _ElemHwDskIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 1),
    _ElemHwDskIndex_Type()
)
elemHwDskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemHwDskIndex.setStatus("current")
_ElemHwDskPath_Type = DisplayString
_ElemHwDskPath_Object = MibTableColumn
elemHwDskPath = _ElemHwDskPath_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 2),
    _ElemHwDskPath_Type()
)
elemHwDskPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskPath.setStatus("current")
_ElemHwDskDevice_Type = DisplayString
_ElemHwDskDevice_Object = MibTableColumn
elemHwDskDevice = _ElemHwDskDevice_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 3),
    _ElemHwDskDevice_Type()
)
elemHwDskDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskDevice.setStatus("current")


class _ElemHwDskMinPercent_Type(Integer32):
    """Custom type elemHwDskMinPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwDskMinPercent_Type.__name__ = "Integer32"
_ElemHwDskMinPercent_Object = MibTableColumn
elemHwDskMinPercent = _ElemHwDskMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 5),
    _ElemHwDskMinPercent_Type()
)
elemHwDskMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskMinPercent.setStatus("current")
_ElemHwDskTotal_Type = Integer32
_ElemHwDskTotal_Object = MibTableColumn
elemHwDskTotal = _ElemHwDskTotal_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 6),
    _ElemHwDskTotal_Type()
)
elemHwDskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskTotal.setStatus("current")
_ElemHwDskAvail_Type = Integer32
_ElemHwDskAvail_Object = MibTableColumn
elemHwDskAvail = _ElemHwDskAvail_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 7),
    _ElemHwDskAvail_Type()
)
elemHwDskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskAvail.setStatus("current")
_ElemHwDskUsed_Type = Integer32
_ElemHwDskUsed_Object = MibTableColumn
elemHwDskUsed = _ElemHwDskUsed_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 8),
    _ElemHwDskUsed_Type()
)
elemHwDskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskUsed.setStatus("current")


class _ElemHwDskPercent_Type(Integer32):
    """Custom type elemHwDskPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwDskPercent_Type.__name__ = "Integer32"
_ElemHwDskPercent_Object = MibTableColumn
elemHwDskPercent = _ElemHwDskPercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 9),
    _ElemHwDskPercent_Type()
)
elemHwDskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskPercent.setStatus("current")


class _ElemHwDskPercentNode_Type(Integer32):
    """Custom type elemHwDskPercentNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwDskPercentNode_Type.__name__ = "Integer32"
_ElemHwDskPercentNode_Object = MibTableColumn
elemHwDskPercentNode = _ElemHwDskPercentNode_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 10),
    _ElemHwDskPercentNode_Type()
)
elemHwDskPercentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskPercentNode.setStatus("current")
_ElemHwDskSysName_Type = DisplayString
_ElemHwDskSysName_Object = MibTableColumn
elemHwDskSysName = _ElemHwDskSysName_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 11),
    _ElemHwDskSysName_Type()
)
elemHwDskSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskSysName.setStatus("current")


class _ElemHwDskFreePercent_Type(Integer32):
    """Custom type elemHwDskFreePercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ElemHwDskFreePercent_Type.__name__ = "Integer32"
_ElemHwDskFreePercent_Object = MibTableColumn
elemHwDskFreePercent = _ElemHwDskFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 12),
    _ElemHwDskFreePercent_Type()
)
elemHwDskFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskFreePercent.setStatus("current")
_ElemHwDskBlocks_Type = Unsigned32
_ElemHwDskBlocks_Object = MibTableColumn
elemHwDskBlocks = _ElemHwDskBlocks_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 13),
    _ElemHwDskBlocks_Type()
)
elemHwDskBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskBlocks.setStatus("current")


class _ElemHwDskBlocksSize_Type(Integer32):
    """Custom type elemHwDskBlocksSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemHwDskBlocksSize_Type.__name__ = "Integer32"
_ElemHwDskBlocksSize_Object = MibTableColumn
elemHwDskBlocksSize = _ElemHwDskBlocksSize_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 14),
    _ElemHwDskBlocksSize_Type()
)
elemHwDskBlocksSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskBlocksSize.setStatus("current")
if mibBuilder.loadTexts:
    elemHwDskBlocksSize.setUnits("Bytes")
_ElemHwDskUsedBlocks_Type = Unsigned32
_ElemHwDskUsedBlocks_Object = MibTableColumn
elemHwDskUsedBlocks = _ElemHwDskUsedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 15),
    _ElemHwDskUsedBlocks_Type()
)
elemHwDskUsedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskUsedBlocks.setStatus("current")
_ElemHwDskFreeBlocks_Type = Unsigned32
_ElemHwDskFreeBlocks_Object = MibTableColumn
elemHwDskFreeBlocks = _ElemHwDskFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 16),
    _ElemHwDskFreeBlocks_Type()
)
elemHwDskFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskFreeBlocks.setStatus("current")
_ElemHwDskAllocationFailures_Type = Counter32
_ElemHwDskAllocationFailures_Object = MibTableColumn
elemHwDskAllocationFailures = _ElemHwDskAllocationFailures_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 17),
    _ElemHwDskAllocationFailures_Type()
)
elemHwDskAllocationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskAllocationFailures.setStatus("current")
_ElemHwDskErrorFlag_Type = Integer32
_ElemHwDskErrorFlag_Object = MibTableColumn
elemHwDskErrorFlag = _ElemHwDskErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 100),
    _ElemHwDskErrorFlag_Type()
)
elemHwDskErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskErrorFlag.setStatus("current")
_ElemHwDskErrorMsg_Type = DisplayString
_ElemHwDskErrorMsg_Object = MibTableColumn
elemHwDskErrorMsg = _ElemHwDskErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 5, 2, 1, 101),
    _ElemHwDskErrorMsg_Type()
)
elemHwDskErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemHwDskErrorMsg.setStatus("current")
_ElemCommands_ObjectIdentity = ObjectIdentity
elemCommands = _ElemCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6)
)
_ElemActiveCommands_ObjectIdentity = ObjectIdentity
elemActiveCommands = _ElemActiveCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1)
)
_ElemActiveCmdTable_Object = MibTable
elemActiveCmdTable = _ElemActiveCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    elemActiveCmdTable.setStatus("current")
_ElemActiveCmdEntry_Object = MibTableRow
elemActiveCmdEntry = _ElemActiveCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1)
)
elemActiveCmdEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemActiveCmdSource"),
    (0, "GMS-ELEMENT-MIB", "elemActiveCmdType"),
    (0, "GMS-ELEMENT-MIB", "elemActiveCmdId"),
)
if mibBuilder.loadTexts:
    elemActiveCmdEntry.setStatus("current")
_ElemActiveCmdSource_Type = CommandSource
_ElemActiveCmdSource_Object = MibTableColumn
elemActiveCmdSource = _ElemActiveCmdSource_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 1),
    _ElemActiveCmdSource_Type()
)
elemActiveCmdSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemActiveCmdSource.setStatus("current")
_ElemActiveCmdType_Type = CommandType
_ElemActiveCmdType_Object = MibTableColumn
elemActiveCmdType = _ElemActiveCmdType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 3),
    _ElemActiveCmdType_Type()
)
elemActiveCmdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemActiveCmdType.setStatus("current")
_ElemActiveCmdId_Type = CommandId
_ElemActiveCmdId_Object = MibTableColumn
elemActiveCmdId = _ElemActiveCmdId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 4),
    _ElemActiveCmdId_Type()
)
elemActiveCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemActiveCmdId.setStatus("current")
_ElemActiveCmdState_Type = CommandState
_ElemActiveCmdState_Object = MibTableColumn
elemActiveCmdState = _ElemActiveCmdState_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 5),
    _ElemActiveCmdState_Type()
)
elemActiveCmdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemActiveCmdState.setStatus("current")
_ElemActiveCmdChallenge_Type = Integer32
_ElemActiveCmdChallenge_Object = MibTableColumn
elemActiveCmdChallenge = _ElemActiveCmdChallenge_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 6),
    _ElemActiveCmdChallenge_Type()
)
elemActiveCmdChallenge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemActiveCmdChallenge.setStatus("current")
_ElemActiveCmdProgressCounter_Type = Counter32
_ElemActiveCmdProgressCounter_Object = MibTableColumn
elemActiveCmdProgressCounter = _ElemActiveCmdProgressCounter_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 7),
    _ElemActiveCmdProgressCounter_Type()
)
elemActiveCmdProgressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemActiveCmdProgressCounter.setStatus("current")
_ElemActiveCmdInfo_Type = DisplayString
_ElemActiveCmdInfo_Object = MibTableColumn
elemActiveCmdInfo = _ElemActiveCmdInfo_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 8),
    _ElemActiveCmdInfo_Type()
)
elemActiveCmdInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemActiveCmdInfo.setStatus("current")
_ElemActiveCmdRemoveFlag_Type = Boolean
_ElemActiveCmdRemoveFlag_Object = MibTableColumn
elemActiveCmdRemoveFlag = _ElemActiveCmdRemoveFlag_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 9),
    _ElemActiveCmdRemoveFlag_Type()
)
elemActiveCmdRemoveFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elemActiveCmdRemoveFlag.setStatus("current")
_ElemActiveCmdInterruptFlag_Type = Boolean
_ElemActiveCmdInterruptFlag_Object = MibTableColumn
elemActiveCmdInterruptFlag = _ElemActiveCmdInterruptFlag_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 1, 1, 1, 10),
    _ElemActiveCmdInterruptFlag_Type()
)
elemActiveCmdInterruptFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elemActiveCmdInterruptFlag.setStatus("current")
_ElemCommanding_ObjectIdentity = ObjectIdentity
elemCommanding = _ElemCommanding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2)
)
_ElemCommandingTable_Object = MibTable
elemCommandingTable = _ElemCommandingTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    elemCommandingTable.setStatus("current")
_ElemCommandingTableEntry_Object = MibTableRow
elemCommandingTableEntry = _ElemCommandingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1, 1)
)
elemCommandingTableEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemCommandSource"),
    (0, "GMS-ELEMENT-MIB", "elemCommandType"),
)
if mibBuilder.loadTexts:
    elemCommandingTableEntry.setStatus("current")
_ElemCommandSource_Type = CommandSource
_ElemCommandSource_Object = MibTableColumn
elemCommandSource = _ElemCommandSource_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1, 1, 1),
    _ElemCommandSource_Type()
)
elemCommandSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemCommandSource.setStatus("current")
_ElemCommandType_Type = CommandType
_ElemCommandType_Object = MibTableColumn
elemCommandType = _ElemCommandType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1, 1, 2),
    _ElemCommandType_Type()
)
elemCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemCommandType.setStatus("current")
_ElemCommandId_Type = CommandId
_ElemCommandId_Object = MibTableColumn
elemCommandId = _ElemCommandId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1, 1, 3),
    _ElemCommandId_Type()
)
elemCommandId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elemCommandId.setStatus("current")
_ElemCommandChallenge_Type = Integer32
_ElemCommandChallenge_Object = MibTableColumn
elemCommandChallenge = _ElemCommandChallenge_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 1, 1, 4),
    _ElemCommandChallenge_Type()
)
elemCommandChallenge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    elemCommandChallenge.setStatus("current")
_ElemCommandParameterTable_Object = MibTable
elemCommandParameterTable = _ElemCommandParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    elemCommandParameterTable.setStatus("current")
_ElemCommandParameterEntry_Object = MibTableRow
elemCommandParameterEntry = _ElemCommandParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1)
)
elemCommandParameterEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemCommandParameterSource"),
    (0, "GMS-ELEMENT-MIB", "elemCommandParameterCmdId"),
    (0, "GMS-ELEMENT-MIB", "elemCommandParameterIndex"),
)
if mibBuilder.loadTexts:
    elemCommandParameterEntry.setStatus("current")
_ElemCommandParameterSource_Type = CommandSource
_ElemCommandParameterSource_Object = MibTableColumn
elemCommandParameterSource = _ElemCommandParameterSource_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 1),
    _ElemCommandParameterSource_Type()
)
elemCommandParameterSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemCommandParameterSource.setStatus("current")


class _ElemCommandParameterIndex_Type(Integer32):
    """Custom type elemCommandParameterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemCommandParameterIndex_Type.__name__ = "Integer32"
_ElemCommandParameterIndex_Object = MibTableColumn
elemCommandParameterIndex = _ElemCommandParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 2),
    _ElemCommandParameterIndex_Type()
)
elemCommandParameterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemCommandParameterIndex.setStatus("current")
_ElemCommandParameterRowStatus_Type = RowStatus
_ElemCommandParameterRowStatus_Object = MibTableColumn
elemCommandParameterRowStatus = _ElemCommandParameterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 3),
    _ElemCommandParameterRowStatus_Type()
)
elemCommandParameterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elemCommandParameterRowStatus.setStatus("current")
_ElemCommandParameterKey_Type = DisplayString
_ElemCommandParameterKey_Object = MibTableColumn
elemCommandParameterKey = _ElemCommandParameterKey_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 4),
    _ElemCommandParameterKey_Type()
)
elemCommandParameterKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elemCommandParameterKey.setStatus("current")
_ElemCommandParameterValue_Type = DisplayString
_ElemCommandParameterValue_Object = MibTableColumn
elemCommandParameterValue = _ElemCommandParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 5),
    _ElemCommandParameterValue_Type()
)
elemCommandParameterValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    elemCommandParameterValue.setStatus("current")
_ElemCommandParameterCmdId_Type = CommandId
_ElemCommandParameterCmdId_Object = MibTableColumn
elemCommandParameterCmdId = _ElemCommandParameterCmdId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 6, 2, 2, 1, 6),
    _ElemCommandParameterCmdId_Type()
)
elemCommandParameterCmdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemCommandParameterCmdId.setStatus("current")
_ElemAlerts_ObjectIdentity = ObjectIdentity
elemAlerts = _ElemAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7)
)
_ElemAlertsLastUpdate_ObjectIdentity = ObjectIdentity
elemAlertsLastUpdate = _ElemAlertsLastUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 1)
)


class _ElemAlertsLastAdded_Type(Integer32):
    """Custom type elemAlertsLastAdded based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemAlertsLastAdded_Type.__name__ = "Integer32"
_ElemAlertsLastAdded_Object = MibScalar
elemAlertsLastAdded = _ElemAlertsLastAdded_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 1, 1),
    _ElemAlertsLastAdded_Type()
)
elemAlertsLastAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsLastAdded.setStatus("current")


class _ElemAlertsLastNtRemoved_Type(Integer32):
    """Custom type elemAlertsLastNtRemoved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemAlertsLastNtRemoved_Type.__name__ = "Integer32"
_ElemAlertsLastNtRemoved_Object = MibScalar
elemAlertsLastNtRemoved = _ElemAlertsLastNtRemoved_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 1, 2),
    _ElemAlertsLastNtRemoved_Type()
)
elemAlertsLastNtRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsLastNtRemoved.setStatus("current")
_ElemAlertsTable_Object = MibTable
elemAlertsTable = _ElemAlertsTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    elemAlertsTable.setStatus("current")
_ElemAlertsEntry_Object = MibTableRow
elemAlertsEntry = _ElemAlertsEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1)
)
elemAlertsEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemAlertsIndex"),
)
if mibBuilder.loadTexts:
    elemAlertsEntry.setStatus("current")


class _ElemAlertsIndex_Type(Integer32):
    """Custom type elemAlertsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemAlertsIndex_Type.__name__ = "Integer32"
_ElemAlertsIndex_Object = MibTableColumn
elemAlertsIndex = _ElemAlertsIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 1),
    _ElemAlertsIndex_Type()
)
elemAlertsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemAlertsIndex.setStatus("current")
_ElemAlertsUnitIdentifier_Type = DisplayString
_ElemAlertsUnitIdentifier_Object = MibTableColumn
elemAlertsUnitIdentifier = _ElemAlertsUnitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 3),
    _ElemAlertsUnitIdentifier_Type()
)
elemAlertsUnitIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsUnitIdentifier.setStatus("current")
_ElemAlertsLocalisation_Type = DisplayString
_ElemAlertsLocalisation_Object = MibTableColumn
elemAlertsLocalisation = _ElemAlertsLocalisation_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 4),
    _ElemAlertsLocalisation_Type()
)
elemAlertsLocalisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsLocalisation.setStatus("current")


class _ElemAlertsCriticality_Type(Integer32):
    """Custom type elemAlertsCriticality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ElemAlertsCriticality_Type.__name__ = "Integer32"
_ElemAlertsCriticality_Object = MibTableColumn
elemAlertsCriticality = _ElemAlertsCriticality_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 5),
    _ElemAlertsCriticality_Type()
)
elemAlertsCriticality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsCriticality.setStatus("current")
_ElemAlertsTimestamp_Type = DateAndTime
_ElemAlertsTimestamp_Object = MibTableColumn
elemAlertsTimestamp = _ElemAlertsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 6),
    _ElemAlertsTimestamp_Type()
)
elemAlertsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsTimestamp.setStatus("current")
_ElemAlertsIdentifier_Type = DisplayString
_ElemAlertsIdentifier_Object = MibTableColumn
elemAlertsIdentifier = _ElemAlertsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 7),
    _ElemAlertsIdentifier_Type()
)
elemAlertsIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsIdentifier.setStatus("current")
_ElemAlertsTransient_Type = Boolean
_ElemAlertsTransient_Object = MibTableColumn
elemAlertsTransient = _ElemAlertsTransient_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 10),
    _ElemAlertsTransient_Type()
)
elemAlertsTransient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsTransient.setStatus("current")
_ElemAlertsArguments_Type = DisplayString
_ElemAlertsArguments_Object = MibTableColumn
elemAlertsArguments = _ElemAlertsArguments_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 7, 2, 1, 11),
    _ElemAlertsArguments_Type()
)
elemAlertsArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemAlertsArguments.setStatus("current")
_ElemBITResults_ObjectIdentity = ObjectIdentity
elemBITResults = _ElemBITResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8)
)
_ElemBITResultsTable_Object = MibTable
elemBITResultsTable = _ElemBITResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    elemBITResultsTable.setStatus("current")
_ElemBITResultsEntry_Object = MibTableRow
elemBITResultsEntry = _ElemBITResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1)
)
elemBITResultsEntry.setIndexNames(
    (0, "GMS-ELEMENT-MIB", "elemBITResultsIndex"),
)
if mibBuilder.loadTexts:
    elemBITResultsEntry.setStatus("current")


class _ElemBITResultsIndex_Type(Integer32):
    """Custom type elemBITResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ElemBITResultsIndex_Type.__name__ = "Integer32"
_ElemBITResultsIndex_Object = MibTableColumn
elemBITResultsIndex = _ElemBITResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 1),
    _ElemBITResultsIndex_Type()
)
elemBITResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    elemBITResultsIndex.setStatus("current")
_ElemBITResultsId_Type = DisplayString
_ElemBITResultsId_Object = MibTableColumn
elemBITResultsId = _ElemBITResultsId_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 2),
    _ElemBITResultsId_Type()
)
elemBITResultsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemBITResultsId.setStatus("current")
_ElemBITResultsType_Type = BITType
_ElemBITResultsType_Object = MibTableColumn
elemBITResultsType = _ElemBITResultsType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 3),
    _ElemBITResultsType_Type()
)
elemBITResultsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemBITResultsType.setStatus("current")
_ElemBITResultsLocation_Type = DisplayString
_ElemBITResultsLocation_Object = MibTableColumn
elemBITResultsLocation = _ElemBITResultsLocation_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 4),
    _ElemBITResultsLocation_Type()
)
elemBITResultsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemBITResultsLocation.setStatus("current")
_ElemBITResultsResult_Type = DisplayString
_ElemBITResultsResult_Object = MibTableColumn
elemBITResultsResult = _ElemBITResultsResult_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 5),
    _ElemBITResultsResult_Type()
)
elemBITResultsResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemBITResultsResult.setStatus("current")
_ElemBITResultsResultType_Type = BITResultType
_ElemBITResultsResultType_Object = MibTableColumn
elemBITResultsResultType = _ElemBITResultsResultType_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 8, 1, 1, 6),
    _ElemBITResultsResultType_Type()
)
elemBITResultsResultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemBITResultsResultType.setStatus("current")
_ElemSpecific_ObjectIdentity = ObjectIdentity
elemSpecific = _ElemSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 98)
)
_ElemSpecificSampleValue_Type = Integer32
_ElemSpecificSampleValue_Object = MibScalar
elemSpecificSampleValue = _ElemSpecificSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 98, 1),
    _ElemSpecificSampleValue_Type()
)
elemSpecificSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    elemSpecificSampleValue.setStatus("current")
_ElemTraps_ObjectIdentity = ObjectIdentity
elemTraps = _ElemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 99)
)
_ElementMIBConformance_ObjectIdentity = ObjectIdentity
elementMIBConformance = _ElementMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100)
)
_ElementMIBCompliances_ObjectIdentity = ObjectIdentity
elementMIBCompliances = _ElementMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 1)
)
_ElementMIBGroups_ObjectIdentity = ObjectIdentity
elementMIBGroups = _ElementMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 2)
)

# Managed Objects groups

elementMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 2, 1)
)
elementMIBBasicGroup.setObjects(
      *(("GMS-ELEMENT-MIB", "elemMibVersion"),
        ("GMS-ELEMENT-MIB", "elemMibVersionSpecific"),
        ("GMS-ELEMENT-MIB", "elemStatusState"),
        ("GMS-ELEMENT-MIB", "elemStatusMode"),
        ("GMS-ELEMENT-MIB", "elemStatusIntegrity"),
        ("GMS-ELEMENT-MIB", "elemStatusLastIntegrityCheck"),
        ("GMS-ELEMENT-MIB", "elemStatusLastStateChange"),
        ("GMS-ELEMENT-MIB", "elemStatusLastModeChange"),
        ("GMS-ELEMENT-MIB", "elemStatusIntegrityLowLevel"),
        ("GMS-ELEMENT-MIB", "elemStatusLastIntegrityLowLevelCheck"),
        ("GMS-ELEMENT-MIB", "elemInfoSite"),
        ("GMS-ELEMENT-MIB", "elemInfoInstance"),
        ("GMS-ELEMENT-MIB", "elemInfoName"),
        ("GMS-ELEMENT-MIB", "elemHwPlatHrSystemUptime"),
        ("GMS-ELEMENT-MIB", "elemHwPlatHrSystemDate"),
        ("GMS-ELEMENT-MIB", "elemHwPlatHrSystemNumUsers"),
        ("GMS-ELEMENT-MIB", "elemHwPlatHrSystemProcesses"),
        ("GMS-ELEMENT-MIB", "elemHwPlatSysName"),
        ("GMS-ELEMENT-MIB", "elemHwPlatSysContact"),
        ("GMS-ELEMENT-MIB", "elemHwPlatHrLastReachable"),
        ("GMS-ELEMENT-MIB", "elemHwPlatCpuUser"),
        ("GMS-ELEMENT-MIB", "elemHwPlatCpuNice"),
        ("GMS-ELEMENT-MIB", "elemHwPlatCpuSystem"),
        ("GMS-ELEMENT-MIB", "elemHwPlatCpuIdle"),
        ("GMS-ELEMENT-MIB", "elemHwPlatMemSize"),
        ("GMS-ELEMENT-MIB", "elemHwPlatMemUsed"),
        ("GMS-ELEMENT-MIB", "elemHwPlatMemAvail"),
        ("GMS-ELEMENT-MIB", "elemHwPlatMemUsedPercent"),
        ("GMS-ELEMENT-MIB", "elemHwPlatMemAvailPercent"),
        ("GMS-ELEMENT-MIB", "elemHwPlatVirtualMemSize"),
        ("GMS-ELEMENT-MIB", "elemHwPlatVirtualMemUsed"),
        ("GMS-ELEMENT-MIB", "elemHwPlatVirtualMemAvail"),
        ("GMS-ELEMENT-MIB", "elemHwPlatVirtualMemUsedPercent"),
        ("GMS-ELEMENT-MIB", "elemHwPlatVirtualMemAvailPercent"),
        ("GMS-ELEMENT-MIB", "elemHwPlatSystemLoad1"),
        ("GMS-ELEMENT-MIB", "elemHwPlatSystemLoad2"),
        ("GMS-ELEMENT-MIB", "elemHwPlatSystemLoad3"),
        ("GMS-ELEMENT-MIB", "elemHwPlatOsIdentifier"),
        ("GMS-ELEMENT-MIB", "elemConfigParamValue"),
        ("GMS-ELEMENT-MIB", "elemComponentState"),
        ("GMS-ELEMENT-MIB", "elemComponentMode"),
        ("GMS-ELEMENT-MIB", "elemSWRUActiveVersion"),
        ("GMS-ELEMENT-MIB", "elemSWRUActiveUpTime"),
        ("GMS-ELEMENT-MIB", "elemSWRUActiveType"),
        ("GMS-ELEMENT-MIB", "elemSWRUActiveStatus"),
        ("GMS-ELEMENT-MIB", "elemSWRUAvailableType"),
        ("GMS-ELEMENT-MIB", "elemConnectionState"),
        ("GMS-ELEMENT-MIB", "elemConnectionMode"),
        ("GMS-ELEMENT-MIB", "elemConnectionUpTime"),
        ("GMS-ELEMENT-MIB", "elemConnectionDataRate"),
        ("GMS-ELEMENT-MIB", "elemHwDskPath"),
        ("GMS-ELEMENT-MIB", "elemHwDskDevice"),
        ("GMS-ELEMENT-MIB", "elemHwDskMinPercent"),
        ("GMS-ELEMENT-MIB", "elemHwDskTotal"),
        ("GMS-ELEMENT-MIB", "elemHwDskAvail"),
        ("GMS-ELEMENT-MIB", "elemHwDskUsed"),
        ("GMS-ELEMENT-MIB", "elemHwDskPercent"),
        ("GMS-ELEMENT-MIB", "elemHwDskPercentNode"),
        ("GMS-ELEMENT-MIB", "elemHwDskSysName"),
        ("GMS-ELEMENT-MIB", "elemHwDskFreePercent"),
        ("GMS-ELEMENT-MIB", "elemHwDskBlocks"),
        ("GMS-ELEMENT-MIB", "elemHwDskBlocksSize"),
        ("GMS-ELEMENT-MIB", "elemHwDskUsedBlocks"),
        ("GMS-ELEMENT-MIB", "elemHwDskFreeBlocks"),
        ("GMS-ELEMENT-MIB", "elemHwDskAllocationFailures"),
        ("GMS-ELEMENT-MIB", "elemHwDskErrorFlag"),
        ("GMS-ELEMENT-MIB", "elemHwDskErrorMsg"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdState"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdChallenge"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdProgressCounter"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdInfo"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdRemoveFlag"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdInterruptFlag"),
        ("GMS-ELEMENT-MIB", "elemCommandId"),
        ("GMS-ELEMENT-MIB", "elemCommandChallenge"),
        ("GMS-ELEMENT-MIB", "elemCommandParameterRowStatus"),
        ("GMS-ELEMENT-MIB", "elemCommandParameterKey"),
        ("GMS-ELEMENT-MIB", "elemCommandParameterValue"),
        ("GMS-ELEMENT-MIB", "elemAlertsLastAdded"),
        ("GMS-ELEMENT-MIB", "elemAlertsLastNtRemoved"),
        ("GMS-ELEMENT-MIB", "elemAlertsUnitIdentifier"),
        ("GMS-ELEMENT-MIB", "elemAlertsLocalisation"),
        ("GMS-ELEMENT-MIB", "elemAlertsCriticality"),
        ("GMS-ELEMENT-MIB", "elemAlertsTimestamp"),
        ("GMS-ELEMENT-MIB", "elemAlertsIdentifier"),
        ("GMS-ELEMENT-MIB", "elemAlertsTransient"),
        ("GMS-ELEMENT-MIB", "elemAlertsArguments"),
        ("GMS-ELEMENT-MIB", "elemComponentLastStateChange"),
        ("GMS-ELEMENT-MIB", "elemComponentLastModeChange"),
        ("GMS-ELEMENT-MIB", "elemComponentVersion"))
)
if mibBuilder.loadTexts:
    elementMIBBasicGroup.setStatus("current")

elementMIBElementSpecificGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 2, 2)
)
elementMIBElementSpecificGroup.setObjects(
    ("GMS-ELEMENT-MIB", "elemSpecificSampleValue")
)
if mibBuilder.loadTexts:
    elementMIBElementSpecificGroup.setStatus("current")

elementBITTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 2, 3)
)
elementBITTestGroup.setObjects(
      *(("GMS-ELEMENT-MIB", "elemBITResultsId"),
        ("GMS-ELEMENT-MIB", "elemBITResultsType"),
        ("GMS-ELEMENT-MIB", "elemBITResultsLocation"),
        ("GMS-ELEMENT-MIB", "elemBITResultsResult"),
        ("GMS-ELEMENT-MIB", "elemBITResultsResultType"))
)
if mibBuilder.loadTexts:
    elementBITTestGroup.setStatus("current")


# Notification objects

elemCommandChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 99, 3)
)
elemCommandChange.setObjects(
      *(("GMS-ELEMENT-MIB", "elemActiveCmdState"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdChallenge"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdProgressCounter"),
        ("GMS-ELEMENT-MIB", "elemActiveCmdInfo"))
)
if mibBuilder.loadTexts:
    elemCommandChange.setStatus(
        "current"
    )

elemAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 99, 5)
)
elemAlert.setObjects(
    ("GMS-ELEMENT-MIB", "elemAlertsLastAdded")
)
if mibBuilder.loadTexts:
    elemAlert.setStatus(
        "current"
    )


# Notifications groups

elementMIBBasicNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 2, 4)
)
elementMIBBasicNotificationsGroup.setObjects(
      *(("GMS-ELEMENT-MIB", "elemCommandChange"),
        ("GMS-ELEMENT-MIB", "elemAlert"))
)
if mibBuilder.loadTexts:
    elementMIBBasicNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

elementMIBBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 162, 1, 1, 1, 100, 1, 1)
)
elementMIBBasicCompliance.setObjects(
      *(("GMS-ELEMENT-MIB", "elementMIBBasicGroup"),
        ("GMS-ELEMENT-MIB", "elementMIBBasicNotificationsGroup"),
        ("GMS-ELEMENT-MIB", "elementMIBElementSpecificGroup"),
        ("GMS-ELEMENT-MIB", "elementBITTestGroup"))
)
if mibBuilder.loadTexts:
    elementMIBBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GMS-ELEMENT-MIB",
    **{"CommandId": CommandId,
       "CommandState": CommandState,
       "CommandSource": CommandSource,
       "ElementSite": ElementSite,
       "ElementState": ElementState,
       "ConnectionState": ConnectionState,
       "ConnectionMode": ConnectionMode,
       "MIBVersion": MIBVersion,
       "OptionalMIBVersion": OptionalMIBVersion,
       "ElementMode": ElementMode,
       "ElementIntegrity": ElementIntegrity,
       "CommandType": CommandType,
       "Boolean": Boolean,
       "SWRUType": SWRUType,
       "SWRUStatus": SWRUStatus,
       "SWRUVersion": SWRUVersion,
       "BITType": BITType,
       "BITResultType": BITResultType,
       "OSIdentifierType": OSIdentifierType,
       "gmsElementMIB": gmsElementMIB,
       "mibVersions": mibVersions,
       "elemMibVersion": elemMibVersion,
       "elemMibVersionSpecific": elemMibVersionSpecific,
       "elemStatus": elemStatus,
       "elemStatusState": elemStatusState,
       "elemStatusLastStateChange": elemStatusLastStateChange,
       "elemStatusMode": elemStatusMode,
       "elemStatusLastModeChange": elemStatusLastModeChange,
       "elemStatusIntegrity": elemStatusIntegrity,
       "elemStatusLastIntegrityCheck": elemStatusLastIntegrityCheck,
       "elemStatusIntegrityLowLevel": elemStatusIntegrityLowLevel,
       "elemStatusLastIntegrityLowLevelCheck": elemStatusLastIntegrityLowLevelCheck,
       "elemInfo": elemInfo,
       "elemInfoSite": elemInfoSite,
       "elemInfoInstance": elemInfoInstance,
       "elemInfoName": elemInfoName,
       "elemSw": elemSw,
       "elemConfigParameters": elemConfigParameters,
       "elemConfigParamTable": elemConfigParamTable,
       "elemConfigParamEntry": elemConfigParamEntry,
       "elemConfigParamInstance": elemConfigParamInstance,
       "elemConfigParamId": elemConfigParamId,
       "elemConfigParamValue": elemConfigParamValue,
       "elemComponentInfo": elemComponentInfo,
       "elemComponentInfoTable": elemComponentInfoTable,
       "elemComponentInfoEntry": elemComponentInfoEntry,
       "elemComponentInstance": elemComponentInstance,
       "elemComponentId": elemComponentId,
       "elemComponentState": elemComponentState,
       "elemComponentLastStateChange": elemComponentLastStateChange,
       "elemComponentMode": elemComponentMode,
       "elemComponentLastModeChange": elemComponentLastModeChange,
       "elemComponentVersion": elemComponentVersion,
       "elemSWRUActive": elemSWRUActive,
       "elemSWRUActiveTable": elemSWRUActiveTable,
       "elemSWRUActiveEntry": elemSWRUActiveEntry,
       "elemSWRUActiveInstance": elemSWRUActiveInstance,
       "elemSWRUActiveId": elemSWRUActiveId,
       "elemSWRUActiveVersion": elemSWRUActiveVersion,
       "elemSWRUActiveUpTime": elemSWRUActiveUpTime,
       "elemSWRUActiveType": elemSWRUActiveType,
       "elemSWRUActiveStatus": elemSWRUActiveStatus,
       "elemSWRUAvailable": elemSWRUAvailable,
       "elemSWRUAvailableTable": elemSWRUAvailableTable,
       "elemSWRUAvailableEntry": elemSWRUAvailableEntry,
       "elemSWRUAvailableId": elemSWRUAvailableId,
       "elemSWRUAvailableVersion": elemSWRUAvailableVersion,
       "elemSWRUAvailableInstance": elemSWRUAvailableInstance,
       "elemSWRUAvailableType": elemSWRUAvailableType,
       "elemConnectionsTable": elemConnectionsTable,
       "elemConnectionsEntry": elemConnectionsEntry,
       "elemConnectionInstance": elemConnectionInstance,
       "elemConnectionId": elemConnectionId,
       "elemConnectionState": elemConnectionState,
       "elemConnectionMode": elemConnectionMode,
       "elemConnectionUpTime": elemConnectionUpTime,
       "elemConnectionDataRate": elemConnectionDataRate,
       "elemHw": elemHw,
       "elemHwPlatTable": elemHwPlatTable,
       "elemHwPlatEntry": elemHwPlatEntry,
       "elemHwPlatIndex": elemHwPlatIndex,
       "elemHwPlatHrSystemUptime": elemHwPlatHrSystemUptime,
       "elemHwPlatHrSystemDate": elemHwPlatHrSystemDate,
       "elemHwPlatHrSystemNumUsers": elemHwPlatHrSystemNumUsers,
       "elemHwPlatHrSystemProcesses": elemHwPlatHrSystemProcesses,
       "elemHwPlatSysName": elemHwPlatSysName,
       "elemHwPlatSysContact": elemHwPlatSysContact,
       "elemHwPlatHrLastReachable": elemHwPlatHrLastReachable,
       "elemHwPlatCpuUser": elemHwPlatCpuUser,
       "elemHwPlatCpuNice": elemHwPlatCpuNice,
       "elemHwPlatCpuSystem": elemHwPlatCpuSystem,
       "elemHwPlatCpuIdle": elemHwPlatCpuIdle,
       "elemHwPlatMemSize": elemHwPlatMemSize,
       "elemHwPlatMemUsed": elemHwPlatMemUsed,
       "elemHwPlatMemAvail": elemHwPlatMemAvail,
       "elemHwPlatMemUsedPercent": elemHwPlatMemUsedPercent,
       "elemHwPlatMemAvailPercent": elemHwPlatMemAvailPercent,
       "elemHwPlatVirtualMemSize": elemHwPlatVirtualMemSize,
       "elemHwPlatVirtualMemUsed": elemHwPlatVirtualMemUsed,
       "elemHwPlatVirtualMemAvail": elemHwPlatVirtualMemAvail,
       "elemHwPlatVirtualMemUsedPercent": elemHwPlatVirtualMemUsedPercent,
       "elemHwPlatVirtualMemAvailPercent": elemHwPlatVirtualMemAvailPercent,
       "elemHwPlatSystemLoad1": elemHwPlatSystemLoad1,
       "elemHwPlatSystemLoad2": elemHwPlatSystemLoad2,
       "elemHwPlatSystemLoad3": elemHwPlatSystemLoad3,
       "elemHwPlatOsIdentifier": elemHwPlatOsIdentifier,
       "elemHwDskTable": elemHwDskTable,
       "elemHwDskEntry": elemHwDskEntry,
       "elemHwDskIndex": elemHwDskIndex,
       "elemHwDskPath": elemHwDskPath,
       "elemHwDskDevice": elemHwDskDevice,
       "elemHwDskMinPercent": elemHwDskMinPercent,
       "elemHwDskTotal": elemHwDskTotal,
       "elemHwDskAvail": elemHwDskAvail,
       "elemHwDskUsed": elemHwDskUsed,
       "elemHwDskPercent": elemHwDskPercent,
       "elemHwDskPercentNode": elemHwDskPercentNode,
       "elemHwDskSysName": elemHwDskSysName,
       "elemHwDskFreePercent": elemHwDskFreePercent,
       "elemHwDskBlocks": elemHwDskBlocks,
       "elemHwDskBlocksSize": elemHwDskBlocksSize,
       "elemHwDskUsedBlocks": elemHwDskUsedBlocks,
       "elemHwDskFreeBlocks": elemHwDskFreeBlocks,
       "elemHwDskAllocationFailures": elemHwDskAllocationFailures,
       "elemHwDskErrorFlag": elemHwDskErrorFlag,
       "elemHwDskErrorMsg": elemHwDskErrorMsg,
       "elemCommands": elemCommands,
       "elemActiveCommands": elemActiveCommands,
       "elemActiveCmdTable": elemActiveCmdTable,
       "elemActiveCmdEntry": elemActiveCmdEntry,
       "elemActiveCmdSource": elemActiveCmdSource,
       "elemActiveCmdType": elemActiveCmdType,
       "elemActiveCmdId": elemActiveCmdId,
       "elemActiveCmdState": elemActiveCmdState,
       "elemActiveCmdChallenge": elemActiveCmdChallenge,
       "elemActiveCmdProgressCounter": elemActiveCmdProgressCounter,
       "elemActiveCmdInfo": elemActiveCmdInfo,
       "elemActiveCmdRemoveFlag": elemActiveCmdRemoveFlag,
       "elemActiveCmdInterruptFlag": elemActiveCmdInterruptFlag,
       "elemCommanding": elemCommanding,
       "elemCommandingTable": elemCommandingTable,
       "elemCommandingTableEntry": elemCommandingTableEntry,
       "elemCommandSource": elemCommandSource,
       "elemCommandType": elemCommandType,
       "elemCommandId": elemCommandId,
       "elemCommandChallenge": elemCommandChallenge,
       "elemCommandParameterTable": elemCommandParameterTable,
       "elemCommandParameterEntry": elemCommandParameterEntry,
       "elemCommandParameterSource": elemCommandParameterSource,
       "elemCommandParameterIndex": elemCommandParameterIndex,
       "elemCommandParameterRowStatus": elemCommandParameterRowStatus,
       "elemCommandParameterKey": elemCommandParameterKey,
       "elemCommandParameterValue": elemCommandParameterValue,
       "elemCommandParameterCmdId": elemCommandParameterCmdId,
       "elemAlerts": elemAlerts,
       "elemAlertsLastUpdate": elemAlertsLastUpdate,
       "elemAlertsLastAdded": elemAlertsLastAdded,
       "elemAlertsLastNtRemoved": elemAlertsLastNtRemoved,
       "elemAlertsTable": elemAlertsTable,
       "elemAlertsEntry": elemAlertsEntry,
       "elemAlertsIndex": elemAlertsIndex,
       "elemAlertsUnitIdentifier": elemAlertsUnitIdentifier,
       "elemAlertsLocalisation": elemAlertsLocalisation,
       "elemAlertsCriticality": elemAlertsCriticality,
       "elemAlertsTimestamp": elemAlertsTimestamp,
       "elemAlertsIdentifier": elemAlertsIdentifier,
       "elemAlertsTransient": elemAlertsTransient,
       "elemAlertsArguments": elemAlertsArguments,
       "elemBITResults": elemBITResults,
       "elemBITResultsTable": elemBITResultsTable,
       "elemBITResultsEntry": elemBITResultsEntry,
       "elemBITResultsIndex": elemBITResultsIndex,
       "elemBITResultsId": elemBITResultsId,
       "elemBITResultsType": elemBITResultsType,
       "elemBITResultsLocation": elemBITResultsLocation,
       "elemBITResultsResult": elemBITResultsResult,
       "elemBITResultsResultType": elemBITResultsResultType,
       "elemSpecific": elemSpecific,
       "elemSpecificSampleValue": elemSpecificSampleValue,
       "elemTraps": elemTraps,
       "elemCommandChange": elemCommandChange,
       "elemAlert": elemAlert,
       "elementMIBConformance": elementMIBConformance,
       "elementMIBCompliances": elementMIBCompliances,
       "elementMIBBasicCompliance": elementMIBBasicCompliance,
       "elementMIBGroups": elementMIBGroups,
       "elementMIBBasicGroup": elementMIBBasicGroup,
       "elementMIBElementSpecificGroup": elementMIBElementSpecificGroup,
       "elementBITTestGroup": elementBITTestGroup,
       "elementMIBBasicNotificationsGroup": elementMIBBasicNotificationsGroup}
)
