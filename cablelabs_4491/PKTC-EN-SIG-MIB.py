# SNMP MIB module (PKTC-EN-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/PKTC-EN-SIG-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:41:18 2025
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

(pktcEnhancements,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEnhancements")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pktcNcsEndPntConfigEntry,) = mibBuilder.importSymbols(
    "PKTC-SIG-MIB",
    "pktcNcsEndPntConfigEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

pktcEnSigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pktcEnSigMib.setRevisions(
        ("2012-10-30 00:00",
         "2009-06-15 00:00",
         "2007-04-12 00:00",
         "2005-08-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PktcEnSigMibObjects_ObjectIdentity = ObjectIdentity
pktcEnSigMibObjects = _PktcEnSigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1)
)
_PktcEnSigDevConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnSigDevConfigObjects = _PktcEnSigDevConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 1)
)


class _PktcEnNcsMinimumDtmfPlayout_Type(Unsigned32):
    """Custom type pktcEnNcsMinimumDtmfPlayout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 100),
    )


_PktcEnNcsMinimumDtmfPlayout_Type.__name__ = "Unsigned32"
_PktcEnNcsMinimumDtmfPlayout_Object = MibScalar
pktcEnNcsMinimumDtmfPlayout = _PktcEnNcsMinimumDtmfPlayout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 1, 1),
    _PktcEnNcsMinimumDtmfPlayout_Type()
)
pktcEnNcsMinimumDtmfPlayout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsMinimumDtmfPlayout.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsMinimumDtmfPlayout.setUnits("milliseconds")
_PktcEnNcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnNcsEndPntConfigObjects = _PktcEnNcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2)
)
_PktcEnNcsEndPntConfigTable_Object = MibTable
pktcEnNcsEndPntConfigTable = _PktcEnNcsEndPntConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntConfigTable.setStatus("current")
_PktcEnNcsEndPntConfigEntry_Object = MibTableRow
pktcEnNcsEndPntConfigEntry = _PktcEnNcsEndPntConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntConfigEntry.setStatus("current")


class _PktcEnNcsEndPntQuarantineState_Type(Integer32):
    """Custom type pktcEnNcsEndPntQuarantineState based on Integer32"""
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
        *(("normal", 1),
          ("notification", 2),
          ("lockstep", 3),
          ("extendedlockstep", 4))
    )


_PktcEnNcsEndPntQuarantineState_Type.__name__ = "Integer32"
_PktcEnNcsEndPntQuarantineState_Object = MibTableColumn
pktcEnNcsEndPntQuarantineState = _PktcEnNcsEndPntQuarantineState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1, 1, 1),
    _PktcEnNcsEndPntQuarantineState_Type()
)
pktcEnNcsEndPntQuarantineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntQuarantineState.setStatus("current")


class _PktcEnNcsEndPntHookState_Type(Integer32):
    """Custom type pktcEnNcsEndPntHookState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onHook", 1),
          ("onHookPlusNCSActivity", 2),
          ("offHook", 3))
    )


_PktcEnNcsEndPntHookState_Type.__name__ = "Integer32"
_PktcEnNcsEndPntHookState_Object = MibTableColumn
pktcEnNcsEndPntHookState = _PktcEnNcsEndPntHookState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1, 1, 2),
    _PktcEnNcsEndPntHookState_Type()
)
pktcEnNcsEndPntHookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntHookState.setStatus("current")


class _PktcEnNcsEndPntFaxDetection_Type(TruthValue):
    """Custom type pktcEnNcsEndPntFaxDetection based on TruthValue"""
    defaultValue = 2


_PktcEnNcsEndPntFaxDetection_Type.__name__ = "TruthValue"
_PktcEnNcsEndPntFaxDetection_Object = MibTableColumn
pktcEnNcsEndPntFaxDetection = _PktcEnNcsEndPntFaxDetection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1, 1, 3),
    _PktcEnNcsEndPntFaxDetection_Type()
)
pktcEnNcsEndPntFaxDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntFaxDetection.setStatus("current")


class _PktcEnNcsEndPntStatusReportCtrl_Type(Integer32):
    """Custom type pktcEnNcsEndPntStatusReportCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("reportActualStatus", 2),
          ("reportEndPointAsActive", 3))
    )


_PktcEnNcsEndPntStatusReportCtrl_Type.__name__ = "Integer32"
_PktcEnNcsEndPntStatusReportCtrl_Object = MibTableColumn
pktcEnNcsEndPntStatusReportCtrl = _PktcEnNcsEndPntStatusReportCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 1, 1, 4),
    _PktcEnNcsEndPntStatusReportCtrl_Type()
)
pktcEnNcsEndPntStatusReportCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntStatusReportCtrl.setStatus("deprecated")
_PktcEnEndPntInfoTable_Object = MibTable
pktcEnEndPntInfoTable = _PktcEnEndPntInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pktcEnEndPntInfoTable.setStatus("current")
_PktcEnEndPntInfoTableEntry_Object = MibTableRow
pktcEnEndPntInfoTableEntry = _PktcEnEndPntInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1)
)
pktcEnEndPntInfoTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEnEndPntInfoTableEntry.setStatus("current")


class _PktcEnEndPntFgnPotSupport_Type(Bits):
    """Custom type pktcEnEndPntFgnPotSupport based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotDetection", 0),
          ("hazardousFgnPotDetection", 1))
    )

_PktcEnEndPntFgnPotSupport_Type.__name__ = "Bits"
_PktcEnEndPntFgnPotSupport_Object = MibTableColumn
pktcEnEndPntFgnPotSupport = _PktcEnEndPntFgnPotSupport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 1),
    _PktcEnEndPntFgnPotSupport_Type()
)
pktcEnEndPntFgnPotSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnPotSupport.setStatus("current")
_PktcEnEndPntFgnPotDescr_Type = SnmpAdminString
_PktcEnEndPntFgnPotDescr_Object = MibTableColumn
pktcEnEndPntFgnPotDescr = _PktcEnEndPntFgnPotDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 2),
    _PktcEnEndPntFgnPotDescr_Type()
)
pktcEnEndPntFgnPotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnPotDescr.setStatus("current")


class _PktcEnEndPntClrFgnPotTsts_Type(Bits):
    """Custom type pktcEnEndPntClrFgnPotTsts based on Bits"""
    namedValues = NamedValues(
        *(("clrFgnPotentialResults", 0),
          ("clrHazardousPotResults", 1))
    )

_PktcEnEndPntClrFgnPotTsts_Type.__name__ = "Bits"
_PktcEnEndPntClrFgnPotTsts_Object = MibTableColumn
pktcEnEndPntClrFgnPotTsts = _PktcEnEndPntClrFgnPotTsts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 3),
    _PktcEnEndPntClrFgnPotTsts_Type()
)
pktcEnEndPntClrFgnPotTsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnEndPntClrFgnPotTsts.setStatus("current")


class _PktcEnEndPntRunFgnPotTsts_Type(Bits):
    """Custom type pktcEnEndPntRunFgnPotTsts based on Bits"""
    namedValues = NamedValues(
        *(("runFgnPotentialTsts", 0),
          ("runHazardousPotTsts", 1))
    )

_PktcEnEndPntRunFgnPotTsts_Type.__name__ = "Bits"
_PktcEnEndPntRunFgnPotTsts_Object = MibTableColumn
pktcEnEndPntRunFgnPotTsts = _PktcEnEndPntRunFgnPotTsts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 4),
    _PktcEnEndPntRunFgnPotTsts_Type()
)
pktcEnEndPntRunFgnPotTsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnEndPntRunFgnPotTsts.setStatus("current")


class _PktcEnEndPntFgnTestValidity_Type(Bits):
    """Custom type pktcEnEndPntFgnTestValidity based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotTstValidity", 0),
          ("hazardousPotTstValidity", 1))
    )

_PktcEnEndPntFgnTestValidity_Type.__name__ = "Bits"
_PktcEnEndPntFgnTestValidity_Object = MibTableColumn
pktcEnEndPntFgnTestValidity = _PktcEnEndPntFgnTestValidity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 5),
    _PktcEnEndPntFgnTestValidity_Type()
)
pktcEnEndPntFgnTestValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnTestValidity.setStatus("current")


class _PktcEnEndPntFgnTestResults_Type(Bits):
    """Custom type pktcEnEndPntFgnTestResults based on Bits"""
    namedValues = NamedValues(
        *(("fgnPotentialResults", 0),
          ("hazardousPotResults", 1))
    )

_PktcEnEndPntFgnTestResults_Type.__name__ = "Bits"
_PktcEnEndPntFgnTestResults_Object = MibTableColumn
pktcEnEndPntFgnTestResults = _PktcEnEndPntFgnTestResults_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 2, 1, 6),
    _PktcEnEndPntFgnTestResults_Type()
)
pktcEnEndPntFgnTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEnEndPntFgnTestResults.setStatus("current")
_PktcEnNcsEndPntLVMgmtTable_Object = MibTable
pktcEnNcsEndPntLVMgmtTable = _PktcEnNcsEndPntLVMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtTable.setStatus("current")
_PktcEnNcsEndPntLVMgmtTableEntry_Object = MibTableRow
pktcEnNcsEndPntLVMgmtTableEntry = _PktcEnNcsEndPntLVMgmtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 3, 1)
)
pktcEnNcsEndPntLVMgmtTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtTableEntry.setStatus("current")


class _PktcEnNcsEndPntLVMgmtPolicy_Type(Integer32):
    """Custom type pktcEnNcsEndPntLVMgmtPolicy based on Integer32"""
    defaultValue = 4

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
        *(("voltageAtAllTimes", 1),
          ("voltageUnlessRFQAMAbsent", 2),
          ("voltageBasedOnServiceOrTimers", 3),
          ("voltageBasedOnService", 4))
    )


_PktcEnNcsEndPntLVMgmtPolicy_Type.__name__ = "Integer32"
_PktcEnNcsEndPntLVMgmtPolicy_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtPolicy = _PktcEnNcsEndPntLVMgmtPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 3, 1, 1),
    _PktcEnNcsEndPntLVMgmtPolicy_Type()
)
pktcEnNcsEndPntLVMgmtPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtPolicy.setStatus("current")


class _PktcEnNcsEndPntLVMgmtResetTimer_Type(Unsigned32):
    """Custom type pktcEnNcsEndPntLVMgmtResetTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PktcEnNcsEndPntLVMgmtResetTimer_Type.__name__ = "Unsigned32"
_PktcEnNcsEndPntLVMgmtResetTimer_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtResetTimer = _PktcEnNcsEndPntLVMgmtResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 3, 1, 2),
    _PktcEnNcsEndPntLVMgmtResetTimer_Type()
)
pktcEnNcsEndPntLVMgmtResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtResetTimer.setUnits("minutes")


class _PktcEnNcsEndPntLVMgmtMaintTimer_Type(Unsigned32):
    """Custom type pktcEnNcsEndPntLVMgmtMaintTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PktcEnNcsEndPntLVMgmtMaintTimer_Type.__name__ = "Unsigned32"
_PktcEnNcsEndPntLVMgmtMaintTimer_Object = MibTableColumn
pktcEnNcsEndPntLVMgmtMaintTimer = _PktcEnNcsEndPntLVMgmtMaintTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 3, 1, 3),
    _PktcEnNcsEndPntLVMgmtMaintTimer_Type()
)
pktcEnNcsEndPntLVMgmtMaintTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtMaintTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLVMgmtMaintTimer.setUnits("minutes")
_PktcEnNcsEndPntLossTable_Object = MibTable
pktcEnNcsEndPntLossTable = _PktcEnNcsEndPntLossTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossTable.setStatus("current")
_PktcEnNcsEndPntLossEntry_Object = MibTableRow
pktcEnNcsEndPntLossEntry = _PktcEnNcsEndPntLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 4, 1)
)
pktcEnNcsEndPntLossEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossEntry.setStatus("current")


class _PktcEnNcsEndPntLossDA_Type(Integer32):
    """Custom type pktcEnNcsEndPntLossDA based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_PktcEnNcsEndPntLossDA_Type.__name__ = "Integer32"
_PktcEnNcsEndPntLossDA_Object = MibTableColumn
pktcEnNcsEndPntLossDA = _PktcEnNcsEndPntLossDA_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 4, 1, 1),
    _PktcEnNcsEndPntLossDA_Type()
)
pktcEnNcsEndPntLossDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossDA.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossDA.setUnits("dB")


class _PktcEnNcsEndPntLossAD_Type(Integer32):
    """Custom type pktcEnNcsEndPntLossAD based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_PktcEnNcsEndPntLossAD_Type.__name__ = "Integer32"
_PktcEnNcsEndPntLossAD_Object = MibTableColumn
pktcEnNcsEndPntLossAD = _PktcEnNcsEndPntLossAD_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 2, 4, 1, 2),
    _PktcEnNcsEndPntLossAD_Type()
)
pktcEnNcsEndPntLossAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossAD.setStatus("current")
if mibBuilder.loadTexts:
    pktcEnNcsEndPntLossAD.setUnits("dB")
_PktcEnSigEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnSigEndPntConfigObjects = _PktcEnSigEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 3)
)
_PktcEnDcsEndPntConfigObjects_ObjectIdentity = ObjectIdentity
pktcEnDcsEndPntConfigObjects = _PktcEnDcsEndPntConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 1, 4)
)
_PktcEnSigNotificationPrefix_ObjectIdentity = ObjectIdentity
pktcEnSigNotificationPrefix = _PktcEnSigNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 2)
)
_PktcEnSigNotification_ObjectIdentity = ObjectIdentity
pktcEnSigNotification = _PktcEnSigNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 2, 0)
)
_PktcEnSigConformance_ObjectIdentity = ObjectIdentity
pktcEnSigConformance = _PktcEnSigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3)
)
_PktcEnSigCompliances_ObjectIdentity = ObjectIdentity
pktcEnSigCompliances = _PktcEnSigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 1)
)
_PktcEnSigGroups_ObjectIdentity = ObjectIdentity
pktcEnSigGroups = _PktcEnSigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 2)
)
pktcNcsEndPntConfigEntry.registerAugmentions(
    ("PKTC-EN-SIG-MIB",
     "pktcEnNcsEndPntConfigEntry")
)
pktcEnNcsEndPntConfigEntry.setIndexNames(*pktcNcsEndPntConfigEntry.getIndexNames())

# Managed Objects groups

pktcEnSigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 2, 1)
)
pktcEnSigGroup.setObjects(
    ("PKTC-EN-SIG-MIB", "pktcEnNcsMinimumDtmfPlayout")
)
if mibBuilder.loadTexts:
    pktcEnSigGroup.setStatus("current")

pktcEnNcsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 2, 2)
)
pktcEnNcsGroup.setObjects(
      *(("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntQuarantineState"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntHookState"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntFaxDetection"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntFgnPotSupport"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntFgnPotDescr"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntClrFgnPotTsts"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntRunFgnPotTsts"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntFgnTestValidity"),
        ("PKTC-EN-SIG-MIB", "pktcEnEndPntFgnTestResults"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntLossDA"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntLossAD"))
)
if mibBuilder.loadTexts:
    pktcEnNcsGroup.setStatus("current")

pktcEnNcsLVMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 2, 3)
)
pktcEnNcsLVMgmtGroup.setObjects(
      *(("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtPolicy"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtResetTimer"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntLVMgmtMaintTimer"))
)
if mibBuilder.loadTexts:
    pktcEnNcsLVMgmtGroup.setStatus("current")

pktcEnNcsDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 2, 4)
)
pktcEnNcsDeprecatedGroup.setObjects(
    ("PKTC-EN-SIG-MIB", "pktcEnNcsEndPntStatusReportCtrl")
)
if mibBuilder.loadTexts:
    pktcEnNcsDeprecatedGroup.setStatus("deprecated")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcEnSigBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 6, 2, 3, 1, 1)
)
pktcEnSigBasicCompliance.setObjects(
      *(("PKTC-EN-SIG-MIB", "pktcEnSigGroup"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsGroup"),
        ("PKTC-EN-SIG-MIB", "pktcEnNcsLVMgmtGroup"))
)
if mibBuilder.loadTexts:
    pktcEnSigBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-EN-SIG-MIB",
    **{"pktcEnSigMib": pktcEnSigMib,
       "pktcEnSigMibObjects": pktcEnSigMibObjects,
       "pktcEnSigDevConfigObjects": pktcEnSigDevConfigObjects,
       "pktcEnNcsMinimumDtmfPlayout": pktcEnNcsMinimumDtmfPlayout,
       "pktcEnNcsEndPntConfigObjects": pktcEnNcsEndPntConfigObjects,
       "pktcEnNcsEndPntConfigTable": pktcEnNcsEndPntConfigTable,
       "pktcEnNcsEndPntConfigEntry": pktcEnNcsEndPntConfigEntry,
       "pktcEnNcsEndPntQuarantineState": pktcEnNcsEndPntQuarantineState,
       "pktcEnNcsEndPntHookState": pktcEnNcsEndPntHookState,
       "pktcEnNcsEndPntFaxDetection": pktcEnNcsEndPntFaxDetection,
       "pktcEnNcsEndPntStatusReportCtrl": pktcEnNcsEndPntStatusReportCtrl,
       "pktcEnEndPntInfoTable": pktcEnEndPntInfoTable,
       "pktcEnEndPntInfoTableEntry": pktcEnEndPntInfoTableEntry,
       "pktcEnEndPntFgnPotSupport": pktcEnEndPntFgnPotSupport,
       "pktcEnEndPntFgnPotDescr": pktcEnEndPntFgnPotDescr,
       "pktcEnEndPntClrFgnPotTsts": pktcEnEndPntClrFgnPotTsts,
       "pktcEnEndPntRunFgnPotTsts": pktcEnEndPntRunFgnPotTsts,
       "pktcEnEndPntFgnTestValidity": pktcEnEndPntFgnTestValidity,
       "pktcEnEndPntFgnTestResults": pktcEnEndPntFgnTestResults,
       "pktcEnNcsEndPntLVMgmtTable": pktcEnNcsEndPntLVMgmtTable,
       "pktcEnNcsEndPntLVMgmtTableEntry": pktcEnNcsEndPntLVMgmtTableEntry,
       "pktcEnNcsEndPntLVMgmtPolicy": pktcEnNcsEndPntLVMgmtPolicy,
       "pktcEnNcsEndPntLVMgmtResetTimer": pktcEnNcsEndPntLVMgmtResetTimer,
       "pktcEnNcsEndPntLVMgmtMaintTimer": pktcEnNcsEndPntLVMgmtMaintTimer,
       "pktcEnNcsEndPntLossTable": pktcEnNcsEndPntLossTable,
       "pktcEnNcsEndPntLossEntry": pktcEnNcsEndPntLossEntry,
       "pktcEnNcsEndPntLossDA": pktcEnNcsEndPntLossDA,
       "pktcEnNcsEndPntLossAD": pktcEnNcsEndPntLossAD,
       "pktcEnSigEndPntConfigObjects": pktcEnSigEndPntConfigObjects,
       "pktcEnDcsEndPntConfigObjects": pktcEnDcsEndPntConfigObjects,
       "pktcEnSigNotificationPrefix": pktcEnSigNotificationPrefix,
       "pktcEnSigNotification": pktcEnSigNotification,
       "pktcEnSigConformance": pktcEnSigConformance,
       "pktcEnSigCompliances": pktcEnSigCompliances,
       "pktcEnSigBasicCompliance": pktcEnSigBasicCompliance,
       "pktcEnSigGroups": pktcEnSigGroups,
       "pktcEnSigGroup": pktcEnSigGroup,
       "pktcEnNcsGroup": pktcEnNcsGroup,
       "pktcEnNcsLVMgmtGroup": pktcEnNcsLVMgmtGroup,
       "pktcEnNcsDeprecatedGroup": pktcEnNcsDeprecatedGroup}
)
